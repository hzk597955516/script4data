load C:/Research_Foundation/data/protein_data_bank_kinase\7EGC\7EGC_5.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\8BVW\8BVW_6.pdb
align 7EGC_5, 8BVW_6
cmd.set('seq_view', 1)
print(f'TMscore: 0.68677')