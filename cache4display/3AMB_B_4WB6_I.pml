load C:/Research_Foundation/data/protein_data_bank_kinase\3AMB\3AMB_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB6\4WB6_I.pdb
align 3AMB_B, 4WB6_I
cmd.set('seq_view', 1)
print(f'TMscore: 0.51174')