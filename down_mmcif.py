import os
import sys
import  urllib.request
import pandas as pd
import requests
import tqdm
import threading

from utlity import seq2pid_id_to_pid_list, mkdir
from load_csv import pairs2dict


pdb_root = 'C:/Research_Foundation/data/protein_data_bank'
mmcif_root = 'C:/Research_Foundation/data/mmcifs'
fasta_path = 'C:/Research_Foundation/data/fastas/fs_fastas'
d_f = 'https://www.rcsb.org/fasta/entry/2K42'


def download_mmcif(pid, path=mmcif_root):

    fname = os.path.join(path, pid + '.fasta')
    flag = False

    try:
        if pid + '.fasta' in os.listdir(path):
            print(f"--- {pid}.fasta already exists ! ---")
            return
        
        print(f"--- Begining to download {pid} ! ---")
        f = urllib.request.urlopen("https://www.rcsb.org/fasta/entry/" + pid)
        flag = True
        with open(fname, "wb") as g:
            g.write(f.read())
            
    except Exception as e:
        print(f"--- Error occurs when downloading {fname} ---")

    if flag:
        print(f"--- {pid} download completed ! ---")


def download_mmcif_from_list(pids, path=mmcif_root):

    for pid in pids:
        if len(pid) == 4:
            download_mmcif(pid=pid, path=path)
    

def down_mmcif_GPCR():
    data = pd.read_csv('./all_gpcr_pdb_info.csv')
    other_pids = list(data['pdb_code'])
    download_mmcif_from_list(other_pids, '.\\mmCif')


def download_mmcif_b2e(pids, begin, end, path=mmcif_root):

    for i in range(begin, end):
        if i >= len(pids): return 
        pid = pids[i]
        if len(pid) == 4:
            download_mmcif(pid=pid, path=path)


def download_mmcif_quick(pids, path=mmcif_root):
    thread_num = 8
    threads = []
    every = len(pids) // thread_num + 1
    for i in range(thread_num):
        begin, end = i * every, (i + 1) * every
        t = threading.Thread(target=download_mmcif_b2e, 
                             args=(pids, begin, end, path))
        
        threads.append(t)
        t.start()
    
    for th in threads:
        th.join()
    print('ok')

def load_gpcr_pids():
    data = pd.read_csv('./all_gpcr_pdb_info.csv')
    my_dict = data.to_dict('records')
    pid = []
    for i in my_dict:
        pid.append(i['pdb_code'])
    return pid


def load_apo_holo_pids():
    pids = set()
    my_dict = pairs2dict('./name_idxs/(eigenfold)apo_holo_TMscore_au.csv')
    for i in my_dict:
        pids.add(i['chain_A'][:4])
        pids.add(i['chain_B'][:4])
    return list(pids)


def load_fs_pids():
    pids = set()
    my_dict = pairs2dict('./name_idxs/(eigenfold)fs_TMscore_au.csv')
    for i in my_dict:
        pids.add(i['chain_A'][:4])
        pids.add(i['chain_B'][:4])
    return list(pids)
             
if __name__ == "__main__":
    pids = load_fs_pids()
    print(len(pids))
    download_mmcif_quick(pids=pids, path=fasta_path)

    

