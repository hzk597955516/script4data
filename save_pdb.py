import logging
import os

import numpy as np

from Bio.PDB.Chain import Chain
from Bio.PDB.Atom import Atom
from Bio.PDB.Residue import Residue
from Bio.PDB.Model import Model as PDBModel
from Bio.PDB.PDBIO import PDBIO

import residue_constants


def make_chain(aa_types, coords, chain_id):
    chain = Chain(chain_id)

    serial_number = 0

    def make_residue(i, aatype, coord):
        nonlocal serial_number

        resname = residue_constants.restype_1to3.get(aatype, 'UNK')
        residue = Residue(id=(' ', i, ' '), resname=resname, segid='')
        for j, atom_name in enumerate(residue_constants.restype_name_to_atom14_names[resname]):
            if atom_name == '':
                continue

            atom = Atom(name=atom_name,
                        coord=coord[j],
                        bfactor=0, occupancy=1, altloc=' ',
                        fullname=str(f'{atom_name:<4s}'),
                        serial_number=serial_number, element=atom_name[:1])
            residue.add(atom)

            serial_number += 1

        return residue

    for i, (aa, coord) in enumerate(zip(aa_types, coords)):
        chain.add(make_residue(i, aa, coord))

    return chain


def make_chain_ignore0(aa_types, coords, chain_id):
    chain = Chain(chain_id)

    serial_number = 0

    def make_residue(i, aatype, coord):
        nonlocal serial_number

        resname = residue_constants.restype_1to3.get(aatype, 'UNK')
        residue = Residue(id=(' ', i, ' '), resname=resname, segid='')
        gt0 = 0
        for j, atom_name in enumerate(residue_constants.restype_name_to_atom14_names[resname]):
            if atom_name == '':
                continue

            atom = Atom(name=atom_name,
                        coord=coord[j],
                        bfactor=0, occupancy=1, altloc=' ',
                        fullname=str(f'{atom_name:<4s}'),
                        serial_number=serial_number, element=atom_name[:1])
            
            if coord[j][0] != 0 and coord[j][1] != 0 and coord[j][2] != 0:
                residue.add(atom)
                serial_number += 1
                gt0 += 1

        return residue, gt0 > 0
    
    res_num = 0

    for _, (aa, coord) in enumerate(zip(aa_types, coords)):

        res, isok = make_residue(res_num, aa, coord)
        if isok:
            chain.add(res)
            res_num += 1

    return chain


def save_general_pdb(str_seq, coord, pdb_path):
    assert len(str_seq) == coord.shape[0]

    chain = make_chain_ignore0(str_seq, coord[:len(str_seq)], 'A')

    model = PDBModel(id=0)
    model.add(chain)

    pdb = PDBIO()
    pdb.set_structure(model)
    pdb.save(pdb_path)