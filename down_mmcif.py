import os
import sys
import  urllib.request
import pandas as pd
import requests

from utlity import seq2pid_id_to_pid_list, mkdir

pdb_root = 'C:/Research_Foundation/data/protein_data_bank'
mmcif_root = 'C:/Research_Foundation/data/mmcifs'


def download_mmcif(pid, path=mmcif_root):

    fname = os.path.join(path, pid + '.cif')
    flag = False

    try:
        if pid + '.cif' in os.listdir(path):
            print(f"--- {pid}.cif already exists ! ---")
            return
        
        print(f"--- Begining to download {pid} ! ---")
        f = urllib.request.urlopen("https://files.rcsb.org/download/" + pid + ".cif")
        flag = True

    except Exception as e:
        print(f"--- Error occurs when downloading {fname} ---")

    if flag:
        with open(fname, "wb") as g:
            g.write(f.read())
        print(f"--- {pid} download completed ! ---")


def download_mmcif_from_list(pids, path=mmcif_root):

    for pid in pids:
        if len(pid) == 4:
            download_mmcif(pid=pid, path=path)
    

def down_mmcif_GPCR():
    data = pd.read_csv('./all_gpcr_pdb_info.csv')
    other_pids = list(data['pdb_code'])
    download_mmcif_from_list(other_pids, '.\\mmCif')


if __name__ == "__main__":
    pids = seq2pid_id_to_pid_list('./seq2pid_id/gpcr.csv')

    

