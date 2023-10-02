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

if __name__ == '__main__':
    data = csv2dict('./csv_result/result_7.csv')