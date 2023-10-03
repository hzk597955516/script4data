import load_csv
import comparison
import logging
import os

from mmcif_parsing import parse as mmcif_parse
from Bio.PDB.PDBExceptions import PDBConstructionException
from utlity import seq2pid_id_to_dict, pairs_to_nameidx
from comparison import iterate_all

logger = logging.getLogger()

pdb_root = 'C:/Research_Foundation/data/protein_data_bank'
mmcif_root = 'C:/Research_Foundation/data/mmcifs'


def nameidx_from_seq2pid_id(seq2pid_id_file_path, pdb_dir_path, name_idx_file_path):

    seq2pid_idx = seq2pid_id_to_dict(seq2pid_id_file_path)
    print('--- Loading is Over ! ---')
    pairs = iterate_all(seq2pid_idx, pdb_dir_path)
    print('--- Comparison is Over ! ---')
    pairs_to_nameidx(pairs, name_idx_file_path)


if __name__ == '__main__':
    nameidx_from_seq2pid_id(seq2pid_id_file_path='./seq2pid_id/gpcr_au.csv', 
                            pdb_dir_path=pdb_root, 
                            name_idx_file_path='./name_idxs/test_2_gpcr_tmscore_all.csv')
    print("OK")