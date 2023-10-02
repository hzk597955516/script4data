from Bio import SeqIO
import os
import csv
import pandas as pd
import logging
from tqdm import tqdm

from mmcif_parsing import parse as mmcif_parse
from Bio.PDB.PDBExceptions import PDBConstructionException

pdb_root = 'C:/Research_Foundation/data/protein_data_bank'
mmcif_root = 'C:/Research_Foundation/data/mmcifs'


def padding_fun(seqs_from_proteins):
    max_len = max([len(i) for i in seqs_from_proteins.values()])

    for key in seqs_from_proteins.keys():
        addition = max_len - len(seqs_from_proteins[key])
        seqs_from_proteins[key] += addition * ['_']


def filter_fun(seqs_from_proteins):
    keys = list(seqs_from_proteins.keys())

    for key in keys:
        seqs_from_proteins[key].sort()

        if len(seqs_from_proteins[key]) < 2: del seqs_from_proteins[key]


def read_fasta_file(file_path):
    sequences = []

    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(record.seq)

    return sequences
 

def load_fasta(path):
    input_file = open(path,'r')
    seq = ""
    header = input_file.readline().strip()[1:]
    seqs = {}

    for line in input_file:
        line = line.strip()

        if line[0] != ">":
            seq = seq + line
        else:
            seqs[seq] = int(header[5])
            header = line[1:]
            seq = ""

    input_file.close()
    seqs[seq] = int(header[5])
    output = list(seqs.keys())

    return sorted(output, key=lambda x: seqs[x])


def get_PID_by_FileName(File_name):
    return File_name[:-6].split('_')[-1]


def fastas2dict(curr_dir, filter=True, padding=True, seqs=None):
    file_names = os.listdir(curr_dir)
    proteins = {}

    if isinstance(seqs, dict):
        seqs_from_proteins = seqs
    else:
        seqs_from_proteins = {}

    for file_name in file_names:
        proteins[get_PID_by_FileName(file_name)] = load_fasta(curr_dir + '\\' + file_name)

    PIDs = list(proteins.keys())
    n = len(PIDs)

    for i in range(n):
        curr_pid = PIDs[i]
        cur_seqs = proteins[curr_pid]
        num_chain = len(cur_seqs)

        for j in range(num_chain):
            seq = cur_seqs[j]
            info = curr_pid + '_' + chr(ord('A') + j)

            if seq in seqs_from_proteins.keys():
                seqs_from_proteins[seq].append(info)
            else:
                seqs_from_proteins[seq] = [info]

    if filter:
        filter_fun(seqs_from_proteins)

    if padding:
        padding_fun(seqs_from_proteins)
    print('---' + curr_dir + ' is Ok ! (#:=' + str(n) + ')---')

    if not seqs:
        return seqs_from_proteins


def pre4cvs(seqs):
    output = []
    keys = sorted(seqs.keys(), key=lambda x: len(x))

    for key in keys:
        if len(key) < 20: continue
        tmp = {}
        value = seqs[key]
        tmp['Seqren']= key
        tmp['Length'] = len(key)

        for i, chain in enumerate(value):
            tmp['Candidate ' + str(i + 1)] = chain

        output.append(tmp)

    sorted(output, key=lambda x: x['Length'])

    return output


def data2cvs(seqs, save_path):
    seqs = pre4cvs(seqs)
    df = pd.DataFrame(seqs)
    df.to_csv(save_path, index=False, encoding='gbk')


def get_by_fastas(root, seqs, inplace=True):
    children = os.listdir(root)
    num_pro = 0

    if len(children) == 0: return 0
    if len(children[0]) >= 6 and children[0][-6] == '.':
        if inplace:
            fastas2dict(root, filter=False, padding=False, seqs=seqs)
        else:
            seqs.update(fastas2dict(root, filter=False, padding=False))
        return len(children)
    else:
        for child in children:
            num_pro += get_by_fastas(root + '\\' + child, seqs, inplace=inplace)

    print('---' + root + ' is Ok ! (#:=' + str(num_pro) + ')---')

    return num_pro


def load_all(root, selection_program, result_path=None, filter=True):
    seqs = {}
    selection_program(root, seqs)
    if filter:
        filter_fun(seqs)
    # padding_fun(seqs)
    if result_path:
        data2cvs(seqs, result_path)
    return seqs


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


def load_mmcif(pid, file_path):
    
    try:
        parsing_result = mmcif_parse(file_id=pid, mmcif_file=file_path)

    except PDBConstructionException as e:
        logging.warning('mmcif_parse: %s {%s}', file_path, str(e))

    except Exception as e:
        logging.warning('mmcif_parse: %s {%s}', file_path, str(e))
        raise Exception('...') from e

    return parsing_result.mmcif_object.chain_to_seqres


def get_seq2pid_id_by_pids(pids, mmcif_dir_path):

    seq2pid_id = {}
    
    for pid in tqdm(pids):

        # print('--- begin ' + pid + '! ---')
        pid_path = os.path.join(mmcif_dir_path, pid + '.cif')
        chain2seq = load_mmcif(pid, pid_path)

        for id, res in chain2seq.items():
            # print('--- now is chain_' + id + ' ! ---')
            if res in seq2pid_id.keys():
                seq2pid_id[res].append(pid + '_' + id)
            else:
                seq2pid_id[res] = [pid + '_' + id]
        # print(f'--- {pid} over ! ---')

    return seq2pid_id


def generate_seq2pid_id_csv(pids, mmcif_dir_path, save_path):

    seq2pid_id = get_seq2pid_id_by_pids(pids, mmcif_dir_path)
    filter_fun(seq2pid_id)
    data2cvs(seq2pid_id, save_path)


if __name__ == "__main__":
    print('begin')
    data = pd.read_csv('./all_gpcr_pdb_info.csv')
    pids = list(data['pdb_code'])
    generate_seq2pid_id_csv(pids=pids,
                            mmcif_dir_path=mmcif_root, 
                            save_path='./seq2pid_id/test_au.csv')