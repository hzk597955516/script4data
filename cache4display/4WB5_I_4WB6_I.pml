load C:/Research_Foundation/data/protein_data_bank_kinase\4WB5\4WB5_I.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB6\4WB6_I.pdb
align 4WB5_I, 4WB6_I
cmd.set('seq_view', 1)
print(f'TMscore: 0.5176')