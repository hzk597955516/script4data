load C:/Research_Foundation/data/protein_data_bank_kinase\7EGC\7EGC_V.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7NVR\7NVR_X.pdb
align 7EGC_V, 7NVR_X
cmd.set('seq_view', 1)
print(f'TMscore: 0.69654')