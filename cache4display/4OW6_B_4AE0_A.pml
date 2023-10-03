load C:/Research_Foundation/data/protein_data_bank\4OW6\4OW6_B.pdb
load C:/Research_Foundation/data/protein_data_bank\4AE0\4AE0_A.pdb
align 4OW6_B, 4AE0_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.64985')