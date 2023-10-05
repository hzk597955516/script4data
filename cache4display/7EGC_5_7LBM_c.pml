load C:/Research_Foundation/data/protein_data_bank_kinase\7EGC\7EGC_5.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7LBM\7LBM_c.pdb
align 7EGC_5, 7LBM_c
cmd.set('seq_view', 1)
print(f'TMscore: 0.53847')