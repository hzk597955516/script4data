from Bio.PDB import PDBParser


longToShort = {'GLY': 'G', 'ALA': 'A', 'VAL': 'V', 'LEU': 'L', 'ILE': 'I', 'PHE': 'F', 'TRP': 'W', 'TYR': 'Y','ASP': 'D' ,'HIS': 'H', 'ASN': 'N', 'GLU': 'E', 'LYS': 'K', 'GLN': 'Q', 'MET': 'M', 'ARG': 'R', 'SER': 'S', 'THR': 'T', 'CYS': 'C', 'PRO': 'P', 'SEC': 'U', 'PYL': 'O'}

def get_seq_from_pdb(pdb_file_path):

    parser = PDBParser()
    structure = parser.get_structure("test", pdb_file_path)
    seqren = ''
    for model in structure:
        for chain in model:
            for residue in chain:
                seqren += longToShort[residue.get_resname()]
    return seqren