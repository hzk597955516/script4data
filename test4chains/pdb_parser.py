from Bio.PDB.PDBParser import PDBParser
from os.path import basename, splitext


import numpy as np

from Bio.PDB.Chain import Chain
from Bio.PDB.Atom import Atom
from Bio.PDB.Residue import Residue
from Bio.PDB.Model import Model as PDBModel
from Bio.PDB.PDBIO import PDBIO


def get_pdb_id(pdb_file_path):
    return splitext(basename(pdb_file_path))[0]


def parse_pdb(pdb_file, model=0):

    parser = PDBParser()
    
    structure = parser.get_structure('?', pdb_file)

    for chain in structure.get_chains():

        id_ = chain.id
        print(id_)
        model = PDBModel(id=0)
        model.add(chain)

        pdb = PDBIO()
        pdb.set_structure(model)
        pdb.save(id_ + '1.pdb')

    return structure

