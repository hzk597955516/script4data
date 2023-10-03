import load_csv
import comparison
import logging
import os
import pandas as pd

from mmcif_parsing import parse as mmcif_parse
from Bio.PDB.PDBExceptions import PDBConstructionException
from utlity import seq2pid_id_to_dict, pairs_to_nameidx
from comparison import seq2pid_id_to_pairs
from down_mmcif import download_mmcif_from_list
from build_pdb import cut_mmcif_from_list
from load_fasta import generate_seq2pid_id_csv

logger = logging.getLogger()

pdb_root = 'C:/Research_Foundation/data/protein_data_bank'
mmcif_root = 'C:/Research_Foundation/data/mmcifs'
name_idx_root = 'C:/Research_Foundation/data/name_idxs'
seq2pid_id_root = 'C:/Research_Foundation/data/seq2pid_id'
pids_root = 'C:/Research_Foundation/data/raw_pairs_data'


def prepare_data(pids):

    print('--- Downloading ---')
    download_mmcif_from_list(pids, mmcif_root)
    print('--- Downloading Over ---')
    print('--- Cutting ---')
    cut_mmcif_from_list(pids, mmcif_root, pdb_root)
    print('--- Cutting Over ---')


def extract_data(pids, save_path):
    generate_seq2pid_id_csv(pids, mmcif_root, save_path)


def seq2pid_id_to_name_idx(seq2pid_id_file_path, pdb_dir_path, name_idx_file_path, tm_thres=0.7, is_display_detail=False):

    seq2pid_id = seq2pid_id_to_dict(seq2pid_id_file_path)
    print('--- Loading is Over ! ---')
    pairs = seq2pid_id_to_pairs(seq2pid_id, pdb_dir_path, tm_thres=tm_thres, is_display_detail=is_display_detail)
    print('--- Comparison is Over ! ---')
    pairs_to_nameidx(pairs, name_idx_file_path)


def apo2pids():

    pids = set()
    data = pd.read_csv(os.path.join(pids_root, 'apo.csv'))
    my_dicts = data.to_dict('records')
    for dict_ in my_dicts:
        pids.add(dict_['name'][:4].upper())
        pids.add(dict_['holo'][:4].upper())

    return list(pids)


if __name__ == '__main__':
    pids = apo2pids()
    # prepare_data(pids)
    # extract_data(pids, os.path.join(seq2pid_id_root, 'apo_holo_au.csv'))
    seq2pid_id_to_name_idx(seq2pid_id_file_path=os.path.join(seq2pid_id_root, 'apo_holo_au.csv'),
                           pdb_dir_path=pdb_root,
                           name_idx_file_path=os.path.join(name_idx_root, 'apo_holo_TMscore_au.csv'), 
                           tm_thres=1,
                           is_display_detail=False)