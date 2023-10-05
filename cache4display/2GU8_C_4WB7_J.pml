load C:/Research_Foundation/data/protein_data_bank_kinase\2GU8\2GU8_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB7\4WB7_J.pdb
align 2GU8_C, 4WB7_J
cmd.set('seq_view', 1)
print(f'TMscore: 0.42725')