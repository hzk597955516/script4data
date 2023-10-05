load C:/Research_Foundation/data/protein_data_bank_kinase\7LBM\7LBM_D.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\8BVW\8BVW_D.pdb
align 7LBM_D, 8BVW_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.4025')