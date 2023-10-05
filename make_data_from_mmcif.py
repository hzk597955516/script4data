import os
import argparse
import functools
import multiprocessing as mp
import logging
import itertools
import json

import numpy as np

from Bio.PDB.PDBExceptions import PDBConstructionException

import residue_constants
from mmcif_parsing import parse as mmcif_parse
from save_pdb import save_general_pdb
from utlity import mkdir


logger = logging.getLogger()

amino_acids = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']
nucleotides = ['DA', 'DT', 'DG', 'DC', 'A', 'U', 'G', 'C']


def parse_list(path):
    with open(path) as f:
        names = [n.strip() for n in f]
        print(names)
    for pid, full_pid in itertools.groupby(names, key=lambda x:x[:4]):
        yield (pid, list(full_pid))


def make_npz(code, chain_id, str_seq, seq2struc, structure, args):
    n = len(str_seq)
    assert n > 0
    coords = np.zeros((n, 14, 3), dtype=np.float32)
    coord_mask = np.zeros((n, 14), dtype=bool)

    for seq_idx, residue_at_position in seq2struc.items():
        if not residue_at_position.is_missing and residue_at_position.hetflag == ' ':
            residue_id = (residue_at_position.hetflag,
                    residue_at_position.position.residue_number,
                    residue_at_position.position.insertion_code)

            residue = structure[residue_id]

            if residue.resname not in residue_constants.restype_name_to_atom14_names:
                continue
            res_atom14_list = residue_constants.restype_name_to_atom14_names[residue.resname]
            for atom in residue.get_atoms():
                if atom.id not in res_atom14_list:
                    continue
                atom14idx = res_atom14_list.index(atom.id)
                coords[seq_idx, atom14idx] = atom.get_coord()
                coord_mask[seq_idx, atom14idx]= True
                
    feature = dict(seq=str_seq,
            coords=coords,
            coord_mask=coord_mask)

    # np.savez(os.path.join(args.output_dir, f'{code}_{chain_id}.npz'), **feature)

    return feature


def save_header(header, file_path):
    with open(file_path, 'w') as fw:
        json.dump(header, fw)


def process4single(pid, full_pid, args):
    logging.info(f'{pid}, {",".join(full_pid)}')
    mmcif_file = os.path.join(args.pdb_dir, f'{pid}.cif')

    try:
        parsing_result = mmcif_parse(file_id=pid, mmcif_file=mmcif_file)

    except PDBConstructionException as e:
        logging.warning('mmcif_parse: %s {%s}', mmcif_file, str(e))

    except Exception as e:
        logging.warning('mmcif_parse: %s {%s}', mmcif_file, str(e))
        raise Exception('...') from e
    
    if not parsing_result.mmcif_object:
        return

    struc = parsing_result.mmcif_object.structure
    c2a = parsing_result.mmcif_object.mmcif_to_author_chain_id
    chain_id = full_pid[-1]

    if c2a[chain_id] not in parsing_result.mmcif_object.chain_to_seqres:
        print(pid + ' dont have chain ' + chain_id)
        return

    str_seq = parsing_result.mmcif_object.chain_to_seqres[c2a[chain_id]]
    seqres_to_structure = parsing_result.mmcif_object.seqres_to_structure[c2a[chain_id]]

    try:
        feature = make_npz(pid, chain_id, str_seq, seqres_to_structure, struc[c2a[chain_id]], args)
        save_general_pdb(str_seq=feature['seq'], coord=feature['coords'], pdb_path=os.path.join(args.output_dir, pid + '_' + chain_id + '.pdb'))

    except Exception as e:
        logging.error(f'make structure: {mmcif_file} {c2a[chain_id]} {str(e)}')

def process4protein(pid, args):
    # logging.info(f'{pid}, {",".join(full_pid)}')
    mmcif_file = os.path.join(args.pdb_dir, f'{pid}.cif')

    try:
        parsing_result = mmcif_parse(file_id=pid, mmcif_file=mmcif_file)

    except PDBConstructionException as e:
        logging.warning('mmcif_parse: %s {%s}', mmcif_file, str(e))

    except Exception as e:
        logging.warning('mmcif_parse: %s {%s}', mmcif_file, str(e))
        raise Exception('...') from e
    
    if not parsing_result.mmcif_object:
        return

    struc = parsing_result.mmcif_object.structure
    c2a = parsing_result.mmcif_object.mmcif_to_author_chain_id
    next_output_dir = os.path.join(args.output_dir, pid)
    chain_ids = parsing_result.mmcif_object.chain_ids
    mkdir(next_output_dir)

    for chain_id in chain_ids:

        if c2a[chain_id] not in parsing_result.mmcif_object.chain_to_seqres:
            print(pid + ' dont have chain ' + chain_id)
            return

        str_seq = parsing_result.mmcif_object.chain_to_seqres[c2a[chain_id]]
        seqres_to_structure = parsing_result.mmcif_object.seqres_to_structure[c2a[chain_id]]

        try:
            feature = make_npz(pid, chain_id, str_seq, seqres_to_structure, struc[c2a[chain_id]], args)
            save_general_pdb(str_seq=feature['seq'], coord=feature['coords'], pdb_path=os.path.join(next_output_dir, pid + '_' + chain_id + '.pdb'))

        except Exception as e:
            logging.error(f'make structure: {mmcif_file} {c2a[chain_id]} {str(e)}')


def process4protein_au(pid, args):
    # logging.info(f'{pid}, {",".join(full_pid)}')
    mmcif_file = os.path.join(args.pdb_dir, f'{pid}.cif')
    
    if not os.path.exists(mmcif_file):
        print(f'--- {pid}.cif doesnt exists ! ---')

    try:
        parsing_result = mmcif_parse(file_id=pid, mmcif_file=mmcif_file)

    except PDBConstructionException as e:
        logging.warning('mmcif_parse: %s {%s}', mmcif_file, str(e))

    except Exception as e:
        logging.warning('mmcif_parse: %s {%s}', mmcif_file, str(e))
        raise Exception('...') from e
    
    if not parsing_result.mmcif_object:
        return

    struc = parsing_result.mmcif_object.structure
    c2a = parsing_result.mmcif_object.mmcif_to_author_chain_id
    next_output_dir = os.path.join(args.output_dir, pid)
    chain_ids = parsing_result.mmcif_object.chain_ids
    mkdir(next_output_dir)

    for chain_id in chain_ids:

        if c2a[chain_id] not in parsing_result.mmcif_object.chain_to_seqres:
            print(pid + ' dont have chain ' + c2a[chain_id])
            return

        str_seq = parsing_result.mmcif_object.chain_to_seqres[c2a[chain_id]]
        seqres_to_structure = parsing_result.mmcif_object.seqres_to_structure[c2a[chain_id]]
        file_id = c2a[chain_id]
        if file_id.islower(): file_id += '_'
        try:
            feature = make_npz(pid, chain_id, str_seq, seqres_to_structure, struc[c2a[chain_id]], args)
            save_general_pdb(str_seq=feature['seq'], coord=feature['coords'], pdb_path=os.path.join(next_output_dir, pid + '_' + file_id + '.pdb'))

        except Exception as e:
            logging.error(f'make structure: {mmcif_file} {c2a[chain_id]} {str(e)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--cpus', type=int, default=1)
    parser.add_argument('--name_idx', type=str, required=True)
    parser.add_argument('--pdb_dir', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--header_dir', type=str)
    parser.add_argument('--verbose', action='store_true', help='verbose')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

    