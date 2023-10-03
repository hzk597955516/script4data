import subprocess
import os
import argparse
import pymol
import random

from pymol import cmd
import pandas as pd

from build_pdb import cut_mmcif
from down_mmcif import download_mmcif
from utlity import mkdir, nameidx2dict


pdb_root = 'C:/Research_Foundation/data/protein_data_bank'
mmcif_root = 'C:/Research_Foundation/data/mmcifs'

def iterate_dir(dir_path):

    result = []
    file_names = os.listdir(dir_path)
    num = len(file_names)

    for i in range(num):
        cur_path = os.path.join(dir_path, file_names[i])

        for j in range(i + 1, num):
            next_path = os.path.join(dir_path, file_names[j])

            if TMscore(cur_path, next_path) <= 0.7:
                result.append([file_names[i][:6], file_names[j][:6]])

    return result


def iterate_a_seq(chains, pdb_dir_path, num, tm_thres=0.7, is_display_detail=False):

    pairs = []
    num_chain = len(chains)
    dont_use = set()

    for i in range(num_chain):

        cur_chain = chains[i]

        if cur_chain[: 4] in dont_use: continue

        cur_path = os.path.join(pdb_dir_path, cur_chain[:4], cur_chain + '.pdb')
        print('--- Now is {}th : {}th chain !---'.format(num, i))

        for j in range(i + 1, num_chain):

            next_chain = chains[j]
            
            if cur_chain[:4] == next_chain[:4]: 
                dont_use.add(cur_chain[:4])
                break

            next_path = os.path.join(pdb_dir_path, next_chain[:4], next_chain + '.pdb')

            try:
                tm = TMscore(cur_path, next_path, is_display_detail=is_display_detail)

            except Exception as e:
                print('--- Error occur when comparing ' + cur_chain + ' ' + next_chain + ' ! ---')

            # print(cur_chain + ' ' + next_chain + ' is {}'.format(tm))

            if tm <= tm_thres:
                pairs.append([cur_chain, next_chain, tm])

        print('--- {}th : {}th chain is over !---'.format(num, i))

    return pairs


def seq2pid_id_to_pairs(seq2pid_id, pdb_dir_path, tm_thres=0.7, is_display_detail=False):

    all_pairs = []
    candidates = list(seq2pid_id.values())

    num = 0
    for chains in candidates:
        print('--- begining to select the {}th seq ! ---'.format(num))
        pairs = iterate_a_seq(chains, pdb_dir_path, num, tm_thres=tm_thres, is_display_detail=is_display_detail)

        if len(pairs) > 0:
            all_pairs += pairs

        print('--- the {}th seq is Ok ! ---'.format(num))
        num += 1

    return all_pairs
    

def TMscore(pid_id_1, pid_id_2, is_display_detail=False):
    
    output = subprocess.getoutput('TMalign ' + pid_id_1 + ' ' + pid_id_2)
    if is_display_detail:
        print(output)
    output = output.split('\n')
    output1 = float(output[13][10: 17])
    output2 = float(output[14][10: 17])

    return max(output1, output2) 


def display_pymol(pid_id_1, pid_id_2, pdb_dir_path, caches_path='./cache4display', TMscore=None):

    c1_path = os.path.join(pdb_dir_path, pid_id_1[:4], pid_id_1 + '.pdb')
    c2_path = os.path.join(pdb_dir_path, pid_id_2[:4], pid_id_2 + '.pdb')
    
    lines = [f'load {c1_path}\n', f'load {c2_path}\n', 
             f'align {pid_id_1}, {pid_id_2}\n', 
             'cmd.set(\'seq_view\', 1)\n']
    
    if TMscore: lines.append(f'print(f\'TMscore: {TMscore}\')')

    pair_cache = os.path.join(caches_path, f'{pid_id_1}_{pid_id_2}.pml')

    with open(pair_cache, 'w') as file:
        file.writelines(lines)
    file.close()

    subprocess.Popen('pymol ' + pair_cache)
    

def check_pair(pid_id_1, pid_id_2, pdb_dir_path='./gpcr_pdbs', caches_path='./cache4display', is_display_detail=False):

    c1_path = os.path.join(pdb_dir_path, pid_id_1[:4], pid_id_1 + '.pdb')
    c2_path = os.path.join(pdb_dir_path, pid_id_2[:4], pid_id_2 + '.pdb')
    TM = TMscore(c1_path, c2_path, is_display_detail=is_display_detail)
    # print(f'TMscore: {TM}')
    display_pymol(pid_id_1, pid_id_2, pdb_dir_path, caches_path, TMscore=TM)


def random_check(name_idx_path, n_sample=10):

    pairs_dicts = nameidx2dict(name_idx_path)
    pairs_num = len(pairs_dicts)

    for i in range(n_sample):

        idx = random.randint(0, 9) + i * 10
        
        if idx >= pairs_num: continue

        cur_pair = pairs_dicts[idx]
        print(cur_pair)
        check_pair(cur_pair['chain_A'], cur_pair['chain_B'])


def random_check_all(name_idx_path, n_sample=10):

    pairs_dicts = nameidx2dict(name_idx_path)
    pairs_num = len(pairs_dicts)

    for i in range(n_sample):

        idx = random.randint(0, pairs_num - 1)
        cur_pair = pairs_dicts[idx]
        print(cur_pair)
        check_pair(cur_pair['chain_A'], cur_pair['chain_B'])


def check_pid_data(pid, pid_id, pid_path, mmcif_dir_path, pdb_dir_path):

    mkdir(pid_path)
    download_mmcif(pid, mmcif_dir_path)
    if os.path.exists(os.path.join(pid_path, pid_id + '.pdb')):
        print(f'--- {pid_id}.pdb already exists ! ---')

    else:
        cut_mmcif(pid, mmcif_dir_path, pdb_dir_path)


def align_pairs(pid_id_1, pid_id_2, mmcif_dir_path=mmcif_root, pdb_dir_path=pdb_root, is_display_detail=True):

    pid1, pid2 = pid_id_1[:4], pid_id_2[:4]
    pid1_path, pid2_path = os.path.join(pdb_dir_path, pid1), os.path.join(pdb_dir_path, pid2)
    check_pid_data(pid1, pid_id_1, pid1_path, mmcif_dir_path, pdb_dir_path)
    check_pid_data(pid2, pid_id_2, pid2_path, mmcif_dir_path, pdb_dir_path)
    check_pair(pid_id_1, pid_id_2, pdb_dir_path, is_display_detail=is_display_detail)


if __name__ == '__main__':
    # print(TMscore(chain_id1='./pdb_result/7E9G/7E9G_E.pdb', chain_id2='./pdb_result/7E9H/7E9H_E.pdb'))
    # check_pair('7FIM_P', '7RGP_P')
    # random_check_all('./name_idx/test_gpcr_tmscore_all.csv', n_sample=1)

    align_pairs(pid_id_1='7TYF_P', pid_id_2='7TYI_P', is_display_detail=True)
    