import load_csv
import comparison
import logging
import os
import pandas as pd
import tqdm

from mmcif_parsing import parse as mmcif_parse
from Bio.PDB.PDBExceptions import PDBConstructionException
from utlity import seq2pid_id_to_dict, pairs_to_nameidx
from comparison import seq2pid_id_to_pairs, TMscore
from down_mmcif import download_mmcif_from_list, download_mmcif_quick
from build_pdb import cut_mmcif_from_list
from load_fasta import generate_seq2pid_id_csv, load_mmcif
from load_csv import pairs2dict
from movefile import mycopyfile

logger = logging.getLogger()

pdb_root = '/home/hezaikai/data/gpcr_pdb'
mmcif_root = '/home/hezaikai/data/mmcif_data'
name_idx_root = './result/name_idxs'
seq2pid_id_root = './seq2pid_id'
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
    seq2pid_id_to_name_idx(seq2pid_id_file_path=os.path.join(seq2pid_id_root, 'gpcr_au.csv'),
                           pdb_dir_path=pdb_root,
                           name_idx_file_path=os.path.join(name_idx_root, 'gpcr_name_idx.csv'), 
                           tm_thres=1,
                           is_display_detail=False)

def kinase_pids():
    pids = []
    files = os.listdir(mmcif_root)
    for file in files:
        pids.append(file[:4])
    return pids
    

def get_by_mmcifs(root, seqs):

    mmcif_file_names = os.listdir(root)
    num = 0
    for file_name in mmcif_file_names:
        pid = file_name[: 4]
        print('--- begin ' + pid + '! ---')
        mmcif_info = load_mmcif(pid=pid,  file_path=os.path.join(root, file_name))
        for chain_id, res in mmcif_info.items():
            print('--- now is chain_' + chain_id + ' ! ---')
            if res in seqs.keys():
                seqs[res].append(pid + '_' + chain_id)
            else:
                seqs[res] = [pid + '_' + chain_id]
        num += 1
        print('--- end ' + pid + f'!(num: {num}) ---')
        

def len_pid_id(pid_id):
    pid, c_id = pid_id.split('_')
    chains = load_mmcif(pid=pid, file_path=os.path.join(mmcif_root, pid + '.cif'))
    return len(chains[c_id])


def postprocess():
    
    pair_dict = pairs2dict('./name_idxs/(eigenfold)fs_TMscore_au.csv')
    new_paris = []
    pdb_path = '/home/hezaikai/data/fs_pdb'
    
    for pair in tqdm.tqdm(pair_dict):
        
        chain_A = pair['chain_A']
        chain_B = pair['chain_B']
        
        cur_len = len_pid_id(chain_A)
        pidA, idA = chain_A.split('_')
        pidB, idB = chain_B.split('_')
        
        dis_path = './result/(eigenfold)fs_pair_pdb'
        cur_path = os.path.join(pdb_path, pidA, chain_A + '.pdb')
        next_path = os.path.join(pdb_path, pidB, chain_B + '.pdb')
        mycopyfile(cur_path, os.path.join(dis_path, chain_A + '_' + chain_B))
        mycopyfile(next_path, os.path.join(dis_path, chain_A + '_' + chain_B))
        new_paris.append([chain_A, chain_B, cur_len, pair['TMscore']])
        
    pairs_to_nameidx(new_paris, name_idx_file_path=os.path.join(name_idx_root, '(eigenfold)fs_name_idx.csv'))
    
if __name__ == '__main__':
    pids = kinase_pids()
    # print(len(pids))
    # prepare_data(pids)
    # dont forget to cut them !
    # extract_data(pids, os.path.join(seq2pid_id_root, 'kinase_au.csv'))
    postprocess()
    print('OK')
    
    
