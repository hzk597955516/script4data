import load_csv
import comparison
import logging
import os
import pandas as pd

from mmcif_parsing import parse as mmcif_parse
from Bio.PDB.PDBExceptions import PDBConstructionException
from utlity import seq2pid_id_to_dict, pairs_to_nameidx
from comparison import seq2pid_id_to_pairs, TMscore
from down_mmcif import download_mmcif_from_list, download_mmcif_quick
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
    # download_mmcif_from_list(pids, mmcif_root)
    print('--- Downloading Over ---')
    print('--- Cutting ---')
    cut_mmcif_from_list(pids, mmcif_root, pdb_root)
    print('--- Cutting Over ---')


def extract_data(pids, save_path):
    generate_seq2pid_id_csv(pids, mmcif_root, save_path)


def seq2pid_id_to_name_idx(seq2pid_id_file_path, pdb_dir_path, name_idx_file_path, tm_thres=0.7, is_display_detail=False):

    seq2pid_id = seq2pid_id_to_dict(seq2pid_id_file_path)
    seq2pid_id_list = [[key, value] for key, value in seq2pid_id.items()]
    print('--- Loading is Over ! ---')
    pairs = seq2pid_id_to_pairs(seq2pid_id_list, pdb_dir_path, tm_thres=tm_thres, is_display_detail=is_display_detail)
    print('--- Comparison is Over ! ---')
    pairs_to_nameidx(pairs, name_idx_file_path)


def apo2pids():

    pids = set()
    data = pd.read_csv(os.path.join(pids_root, 'codnas.csv'))
    my_dicts = data.to_dict('records')
    pairs = []
    
    for dict_ in my_dicts:
        pid_1, idx_1 = dict_['name'][:4].upper(), dict_['name'][5]
        pid_2, idx_2 = dict_['other'][:4].upper(), dict_['other'][5]
        tm = TMscore(os.path.join(pdb_root, pid_1, pid_1 + '_' + idx_1 + '.pdb'), 
                os.path.join(pdb_root, pid_2, pid_2 + '_' + idx_2 + '.pdb'))
        pairs.append([pid_1 + '_' + idx_1, pid_2 + '_' + idx_2, tm])
    
    pairs_to_nameidx(pairs, os.path.join(name_idx_root, '(eigenfold)fs_TMscore_au.csv'))
    


def fs2pids():
    
    pids = set()
    data = pd.read_csv(os.path.join(pids_root, 'codnas_orig.csv'))
    my_dicts = data.to_dict('records')
    pairs = []
    for dict_ in my_dicts:
        pid_1, idx_1 = dict_['Fold1'][:4].upper(), dict_['Fold1'][4]
        pid_2, idx_2 = dict_['Fold2'][:4].upper(), dict_['Fold2'][4]
        tm = TMscore(os.path.join(pdb_root, pid_1, pid_1 + '_' + idx_1 + '.pdb'), 
                os.path.join(pdb_root, pid_2, pid_2 + '_' + idx_2 + '.pdb'))
        pairs.append([pid_1 + '_' + idx_1, pid_2 + '_' + idx_2, tm])
    
    pairs_to_nameidx(pairs, os.path.join(name_idx_root, '(eigenfold)fs_TMscore_au.csv'))


def kinase2pids():
    pids = set()
    files = os.listdir('C:/Research_Foundation/data/human_kinase')
    for file in files:
        if file[-8] == '-': 
            continue
        pids.add(file[-9: -5])
    return list(pids)
    
    
def one_step():
    
    seq2pid_id_to_name_idx(seq2pid_id_file_path=os.path.join(seq2pid_id_root, 'kinase_au.csv'),
                           pdb_dir_path=pdb_root,
                           name_idx_file_path=os.path.join(name_idx_root, 'kinase_TMscore_au.csv'), 
                           tm_thres=0.7,
                           is_display_detail=False)
    

def kinase_pids():
    pids = []
    files = os.listdir(mmcif_root)
    for file in files:
        pids.append(file[:4])
    return pids
    
    
    
if __name__ == '__main__':
    pids = kinase_pids()
    # print(len(pids))
    # prepare_data(pids)
    # dont forget to cut them !
    # extract_data(pids, os.path.join(seq2pid_id_root, 'kinase_au.csv'))
    seq2pid_id_to_name_idx(seq2pid_id_file_path=os.path.join(seq2pid_id_root, 'gpcr_au.csv'),
                           pdb_dir_path=pdb_root,
                           name_idx_file_path=os.path.join(name_idx_root, 'test_10_13.csv'), 
                           tm_thres=1,
                           is_display_detail=False)
    
    
