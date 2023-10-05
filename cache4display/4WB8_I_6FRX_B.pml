load C:/Research_Foundation/data/protein_data_bank_kinase\4WB8\4WB8_I.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\6FRX\6FRX_B.pdb
align 4WB8_I, 6FRX_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.68516')