import pandas as pd
import csv


def csv2dict(csv_path):

    data = pd.read_csv(csv_path)
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


def to_name_idx(seqs, name_idx_path):
    df = pd.DataFrame(seqs)
    df.to_csv(name_idx_path, index=False, encoding='gbk')


def pairs2dict(pairs_path):

    data = pd.read_csv(pairs_path)
    my_dict = data.to_dict('records')
    
    return my_dict


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


if __name__ == '__main__':
    pids = load_fs_pids()
    print(pids)
    print('ok')
    