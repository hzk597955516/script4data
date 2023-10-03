from Bio.PDB.PDBParser import PDBParser
from os.path import basename, splitext


import numpy as np

from Bio.PDB.Chain import Chain
from Bio.PDB.Atom import Atom
from Bio.PDB.Residue import Residue
from Bio.PDB.Model import Model as PDBModel
from Bio.PDB.PDBIO import PDBIO

from build_pdb import cut_mmcif

longToShort = {'GLY': 'G', 'ALA': 'A', 'VAL': 'V', 'LEU': 'L', 'ILE': 'I', 'PHE': 'F', 'TRP': 'W', 'TYR': 'Y','ASP': 'D' ,'HIS': 'H', 'ASN': 'N', 'GLU': 'E', 'LYS': 'K', 'GLN': 'Q', 'MET': 'M', 'ARG': 'R', 'SER': 'S', 'THR': 'T', 'CYS': 'C', 'PRO': 'P', 'SEC': 'U', 'PYL': 'O'}
pdb_root = 'C:/Research_Foundation/data/protein_data_bank'
mmcif_root = 'C:/Research_Foundation/data/mmcifs'

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


def get_seq_from_pdb(pdb_file_path):

    parser = PDBParser()
    structure = parser.get_structure("test", pdb_file_path)
    seqren = ''
    for model in structure:
        for chain in model:
            for residue in chain:
                seqren += longToShort[residue.get_resname()]
    return seqren


if __name__ == "__main__":
    print('begin_test')
    # cut_mmcif('6Z4U', mmcif_root, './test4chains')
    res1 = 'MDPKISEMHPALRLVDPQIQLAVTRPKVYPIILRLGSPLSLNMARKTLNSLEDKAFQLTPIAVQMTKLATTEELPDEFVVVTVK'
    res2 = get_seq_from_pdb('./test4chains/6Z4U/6Z4U_A.pdb')
    