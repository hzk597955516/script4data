load C:/Research_Foundation/data/protein_data_bank_kinase\3OVV\3OVV_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB7\4WB7_I.pdb
align 3OVV_B, 4WB7_I
cmd.set('seq_view', 1)
print(f'TMscore: 0.56569')