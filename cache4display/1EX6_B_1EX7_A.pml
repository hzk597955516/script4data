load C:/Research_Foundation/data/protein_data_bank\1EX6\1EX6_B.pdb
load C:/Research_Foundation/data/protein_data_bank\1EX7\1EX7_A.pdb
align 1EX6_B, 1EX7_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.78325')