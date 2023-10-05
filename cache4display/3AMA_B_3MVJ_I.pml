load C:/Research_Foundation/data/protein_data_bank_kinase\3AMA\3AMA_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3MVJ\3MVJ_I.pdb
align 3AMA_B, 3MVJ_I
cmd.set('seq_view', 1)
print(f'TMscore: 0.61402')