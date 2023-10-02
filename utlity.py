import os
import pandas as pd
import csv


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:                   
        os.makedirs(path)            
        print (f"---  new folder: {path} is Ok ! ---")

    else:
        print (f"--- {path} already exists ! ---")


def dict2list(d):
    if isinstance(d, list): return d
    else: 
        o = []
        for k, v in d.items():
            o += dict2list(v)
        return o


def seq2pid_id_to_dict(seq2pid_id_file_path):

    data = pd.read_csv(seq2pid_id_file_path)
    my_dict = data.to_dict('records')
    seqs = {}

    for item in my_dict:

        cans = []
        valuse = list(item.values())
        l_c = len(valuse)

        for i in range(2, l_c):
            if pd.isna(valuse[i]): break
            cans.append(valuse[i])

        seqs[valuse[0]] = cans
    
    return seqs


def seq2pid_id_to_pid_list(seq2pid_id_file_path):

    data = seq2pid_id_to_dict(seq2pid_id_file_path)
    pids = []

    for v in list(data.values()):
        pids += v

    pid_only = set()

    for pid in pids:
        pid_only.add(pid[: 4])

    return list(pid_only)


def pairs_to_nameidx(pairs, name_idx_file_path):
    
    df = pd.DataFrame(pairs)
    df.to_csv(name_idx_file_path, index=False, encoding='gbk')


def nameidx2dict(nameidx_file_path):

    data = pd.read_csv(nameidx_file_path)
    my_dict = data.to_dict('records')
    
    return my_dict