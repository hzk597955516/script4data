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
from movefile import mycopyfile

pdb_root = 'C:/Research_Foundation/data/protein_data_bank'
mmcif_root = 'C:/Research_Foundation/data/mmcifs'
name_idx_root = 'C:/Research_Foundation/data/name_idxs'
seq2pid_id_root = 'C:/Research_Foundation/data/seq2pid_id'
pids_root = 'C:/Research_Foundation/data/raw_pairs_data'


def iterate_dir(dir_path):

    result = []
    file_names = os.listdir(dir_path)
    num = len(file_names)

    for i in range(num):
        cur_path = os.path.join(dir_path, file_names[i])

        for j in range(i + 1, num):
            next_path = os.path.join(dir_path, file_names[j])

            if TMalign(cur_path, next_path) <= 0.7:
                result.append([file_names[i][:6], file_names[j][:6]])

    return result


def iterate_a_seq(seq2chains, pdb_dir_path, num, tm_thres=0.7, is_display_detail=False):

    seq, chains = seq2chains[0], seq2chains[1]
    pairs = []
    num_chain = len(chains)
    dont_use = set()
    for i in range(num_chain):

        cur_chain = chains[i]
        cur_id = cur_chain.split('_')[-1]
        cur_len = len(seq)
        if cur_id.islower(): cur_id += '_'
        if cur_chain[:4] in dont_use: continue
        
        cur_path = os.path.join(pdb_dir_path, cur_chain[:4], cur_chain[:4] + '_' + cur_id + '.pdb')

        print('--- Now is {}th : {}th chain !---'.format(num, i))

        for j in range(i + 1, num_chain):

            next_chain = chains[j]
            next_id = next_chain.split('_')[-1]
            if next_id.islower(): next_id += '_'
            
            if cur_chain[:4] == next_chain[:4]: 
                continue

            next_path = os.path.join(pdb_dir_path, next_chain[:4], next_chain[:4] + '_' + next_id + '.pdb')

            try:
                tm, l1, l2 = TMalign(cur_path, next_path, is_display_detail=is_display_detail)

            except Exception as e:
                print('--- Error occur when comparing ' + cur_chain + ' ' + next_chain + ' ! ---')

            # print(cur_chain + ' ' + next_chain + ' is {}'.format(tm))

            if tm < tm_thres:
                pairs.append([cur_chain, next_chain, cur_len, tm])
                dis_path = 'C:/Research_Foundation/data/gpcr_pair_pdb'
                mycopyfile(cur_path, os.path.join(dis_path, cur_chain + '_' + next_chain))
                mycopyfile(next_path, os.path.join(dis_path, cur_chain + '_' + next_chain))

        print('--- {}th : {}th chain is over !---'.format(num, i))

        dont_use.add(cur_chain[:4])

    return pairs


def seq2pid_id_to_pairs(seq2pid_id, pdb_dir_path, tm_thres=0.7, is_display_detail=False):

    all_pairs = []
    # candidates = list(seq2pid_id.values())
    candidates = seq2pid_id[:10]

    num = 0
    for chains in candidates:
        print('--- begining to select the {}th seq ! ---'.format(num))
        pairs = iterate_a_seq(chains, pdb_dir_path, num, tm_thres=tm_thres, is_display_detail=is_display_detail)

        if len(pairs) > 0:
            all_pairs += pairs

        print('--- the {}th seq is Ok ! ---'.format(num))
        num += 1

    return all_pairs
    

def TMalign(pid_id_1, pid_id_2, is_display_detail=False):
    
    output = subprocess.getoutput('TMalign ' + pid_id_1 + ' ' + pid_id_2)
    if is_display_detail:
        print(output)
    output = output.split('\n')
    output1 = float(output[13][10: 17])
    output2 = float(output[14][10: 17])
    l1 = int(output[9].split(' ')[-2])
    l2 = int(output[10].split(' ')[-2])
    return max(output1, output2), l1, l2 


def TMscore(pid_id_1, pid_id_2, is_display_detail=False):
    output = subprocess.getoutput('TMscore ' + pid_id_1 + ' ' + pid_id_2)
    if is_display_detail:
        print(output)
    output = output.split('\n')
    output = float(output[16][14: 20])
    return output


def display_pymol(pid_id_1, pid_id_2, pdb_dir_path, caches_path='./cache4display', TMalign=None):

    c1_path = os.path.join(pdb_dir_path, pid_id_1[:4], pid_id_1 + '.pdb')
    c2_path = os.path.join(pdb_dir_path, pid_id_2[:4], pid_id_2 + '.pdb')
    
    lines = [f'load {c1_path}\n', f'load {c2_path}\n', 
             f'align {pid_id_1}, {pid_id_2}\n', 
             'cmd.set(\'seq_view\', 1)\n']
    
    if TMalign: lines.append(f'print(f\'TMalign: {TMalign}\')')

    pair_cache = os.path.join(caches_path, f'{pid_id_1}_{pid_id_2}.pml')

    with open(pair_cache, 'w') as file:
        file.writelines(lines)
    file.close()

    subprocess.Popen('pymol ' + pair_cache)
    

def check_pair(pid_id_1, pid_id_2, pdb_dir_path=pdb_root, caches_path='./cache4display', is_display_detail=True, is_align=True):
    
    if pid_id_1.split('_')[-1].islower(): pid_id_1 += '_'
    if pid_id_2.split('_')[-1].islower(): pid_id_2 += '_'
    
    c1_path = os.path.join(pdb_dir_path, pid_id_1[:4], pid_id_1 + '.pdb')
    c2_path = os.path.join(pdb_dir_path, pid_id_2[:4], pid_id_2 + '.pdb')
    if is_align:
        TM, _, _ = TMalign(c1_path, c2_path, is_display_detail=is_display_detail)
    else:
        TM = TMscore(c1_path, c2_path, is_display_detail=is_display_detail)
    # print(f'TMalign: {TM}')
    display_pymol(pid_id_1, pid_id_2, pdb_dir_path, caches_path, TMalign=TM)


def random_check(name_idx_path, n_sample=10):

    pairs_dicts = nameidx2dict(name_idx_path)
    pairs_num = len(pairs_dicts)

    for i in range(n_sample):

        idx = random.randint(0, 9) + i * 10
        
        if idx >= pairs_num: continue

        cur_pair = pairs_dicts[idx]
        print(cur_pair)
        check_pair(cur_pair['chain_A'], cur_pair['chain_B'])


def random_check_all(name_idx_path, n_sample=10, is_align=True):

    pairs_dicts = nameidx2dict(name_idx_path)
    pairs_num = len(pairs_dicts)

    for i in range(n_sample):

        idx = random.randint(0, pairs_num - 1)
        cur_pair = pairs_dicts[idx]
        print(cur_pair)
        check_pair(cur_pair['chain_A'], cur_pair['chain_B'], is_align=is_align)


def check_pid_data(pid, pid_id, pid_path, mmcif_dir_path, pdb_dir_path):

    mkdir(pid_path)
    download_mmcif(pid, mmcif_dir_path)
    if os.path.exists(os.path.join(pid_path, pid_id + '.pdb')):
        print(f'--- {pid_id}.pdb already exists ! ---')

    else:
        cut_mmcif(pid, mmcif_dir_path, pdb_dir_path)


def align_pairs(pid_id_1, pid_id_2, mmcif_dir_path=mmcif_root, pdb_dir_path=pdb_root, is_display_detail=True, is_align=True):

    pid1, pid2 = pid_id_1[:4], pid_id_2[:4]
    pid1_path, pid2_path = os.path.join(pdb_dir_path, pid1), os.path.join(pdb_dir_path, pid2)
    check_pid_data(pid1, pid_id_1, pid1_path, mmcif_dir_path, pdb_dir_path)
    check_pid_data(pid2, pid_id_2, pid2_path, mmcif_dir_path, pdb_dir_path)
    check_pair(pid_id_1, pid_id_2, pdb_dir_path, is_display_detail=is_display_detail, is_align=is_align)


if __name__ == '__main__':
    # print(TMalign(chain_id1='./pdb_result/7E9G/7E9G_E.pdb', chain_id2='./pdb_result/7E9H/7E9H_E.pdb'))
    # check_pair('7FIM_P', '7RGP_P')
    # random_check_all('./name_idx/test_gpcr_tmscore_all.csv', n_sample=1)

    align_pairs(pid_id_1='1CEE_B', pid_id_2='2K42_A', is_display_detail=True, is_align=True)
    # chains1 = ['1HSH_A', '1HSH_B', '1HSH_C', '1HSH_D', '1HSI_A', '1HSI_B']
    # chains2 = ['1Q95_A', '1Q95_B', '1Q95_C', '1Q95_D', '1Q95_E', '1Q95_F', '1ZA1_A', '1ZA1_C']
    # print(TMalign(pid_id_1='C:/Research_Foundation/data/protein_data_bank/1HSI/1HSI_B.pdb', pid_id_2='C:/Research_Foundation/data/protein_data_bank/1HSH/1HSH_D.pdb', 
    # is_display_detail=True))
    # pairs = iterate_a_seq(chains2, pdb_root, 0, tm_thres=1)
    # random_check_all(name_idx_path=os.path.join(name_idx_root, 'kinase_name_idx(Good integrity).csv'), is_align=True)
    