from Bio.PDB import PDBParser
parser = PDBParser()


longToShort = {'GLY': 'G', 'ALA': 'A', 'VAL': 'V', 'LEU': 'L', 'ILE': 'I', 'PHE': 'F', 'TRP': 'W', 'TYR': 'Y','ASP': 'D' ,'HIS': 'H', 'ASN': 'N', 'GLU': 'E', 'LYS': 'K', 'GLN': 'Q', 'MET': 'M', 'ARG': 'R', 'SER': 'S', 'THR': 'T', 'CYS': 'C', 'PRO': 'P', 'SEC': 'U', 'PYL': 'O'}

structure = parser.get_structure("test", './pdb_result_au/1F88/1F88_A.pdb')
seqren = ''
for model in structure:
    for chain in model:
        for residue in chain:
            seqren += longToShort[residue.get_resname()]
print(seqren)