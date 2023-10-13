import itertools
import argparse
import numpy as np
import os
import pandas as pd
import tqdm

from save_pdb import save_general_pdb
from utlity import seq2pid_id_to_dict, mkdir
from make_data_from_mmcif import process4single, process4protein, process4protein_au


def build_A_seq(pid_same_chains, mmcif_dir, output_dir):

    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    args.pdb_dir = mmcif_dir
    args.output_dir = output_dir

    for pid_chainid in pid_same_chains:
        process4single(pid_chainid[:4], pid_chainid, args)


def build_all(seq2chains, mmcif_dir, output_dir):

    for seq, chains in seq2chains.items():
        length = len(seq)
        outpath = os.path.join(output_dir, seq[:6] + '_' + str(length))
        mkdir(outpath)
        build_A_seq(pid_same_chains=chains, mmcif_dir=mmcif_dir, output_dir=outpath)


def cut_mmcif_from_list(pids, mmcif_dir, output_dir):

    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    args.pdb_dir = mmcif_dir
    args.output_dir = output_dir

    for pid in tqdm.tqdm(pids):
        if os.path.exists(os.path.join(output_dir, pid)): continue
        if len(pid) == 4:
            process4protein_au(pid, args)
    

def cut_mmcif(pid, data_dir_path, target_dir_path):

    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    args.pdb_dir = data_dir_path
    args.output_dir = target_dir_path
    process4protein_au(pid, args)
    

def test1():
    seq2chains = {'ABCD': ['6B3J_A', '6B3J_B', '6B3J_C', '6B3J_D'],
                  'EFGH': ['6B3J_E', '6B3J_F', '6ORV_E', '6X18_F', '6X19_E'], 
                  'IJKL': ['6X1A_E', '7C2E_E', '7KI0_F', '7KI1_E', '7LCI_A', '7LCJ_A'],
                  'MNOP': ['7LLL_F', '7LLY_F', '7S1M_F', '7S3I_E']}
    
    data = seq2pid_id_to_dict('./csv_result/result_7.csv')
    pids = []
    for v in list(data.values()):
        pids += v

    pid_only = set()

    for pid in pids:
        pid_only.add(pid[: 4])

    pids = list(pid_only)
    
    cut_mmcif_from_list(pids=pids, mmcif_dir='.\\mmCif', output_dir='.\\pdb_result')


if __name__ == '__main__':
    # cut_mmcif_from_list(['7ENC'], mmcif_dir='C:/Research_Foundation/data/mmcifs_kinase',
                        #output_dir='./test4chains')
    print('ok')