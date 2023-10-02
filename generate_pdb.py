from load_fasta import load_all
from build_pdb import build_all

def generate_all(fastas_dir, mmcif_dir, output_dir):
    seqs2chains = load_all(fastas_dir)
    build_all(seqs2chains, mmcif_dir, output_dir)

if __name__ == "__main__":
    # generate_all(fastas_dir='./GPCR', mmcif_dir='./mmCif', output_dir='./pdb_result')
    s2c = {'ABCD': ['7JHJ_C', '7JV5_D', '7JVP_D', '7JVQ_D', '7KH0_E', '7LJC_D', '7LJD_D', '7RKF_C', '7RKM_C', '7RKN_C', '7T6S_C', '7T6T_C',	'7T6U_C', '7T6V_D', '7VGY_D', '7VGZ_D']}
    build_all(seq2chains=s2c, mmcif_dir='./mmCif', output_dir='./same_chains_pdb')