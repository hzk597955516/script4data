load C:/Research_Foundation/data/protein_data_bank_kinase\4WB7\4WB7_I.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB8\4WB8_I.pdb
align 4WB7_I, 4WB8_I
cmd.set('seq_view', 1)
print(f'TMscore: 0.64805')