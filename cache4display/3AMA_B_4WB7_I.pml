load C:/Research_Foundation/data/protein_data_bank_kinase\3AMA\3AMA_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB7\4WB7_I.pdb
align 3AMA_B, 4WB7_I
cmd.set('seq_view', 1)
print(f'TMscore: 0.599')