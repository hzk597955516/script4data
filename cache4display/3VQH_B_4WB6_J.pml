load C:/Research_Foundation/data/protein_data_bank_kinase\3VQH\3VQH_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB6\4WB6_J.pdb
align 3VQH_B, 4WB6_J
cmd.set('seq_view', 1)
print(f'TMscore: 0.39055')