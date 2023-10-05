load C:/Research_Foundation/data/protein_data_bank_kinase\7EGC\7EGC_D.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7ENC\7ENC_Dd.pdb
align 7EGC_D, 7ENC_Dd
cmd.set('seq_view', 1)
print(f'TMscore: 0.67018')