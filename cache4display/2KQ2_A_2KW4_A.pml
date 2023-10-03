load C:/Research_Foundation/data/protein_data_bank\2KQ2\2KQ2_A.pdb
load C:/Research_Foundation/data/protein_data_bank\2KW4\2KW4_A.pdb
align 2KQ2_A, 2KW4_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.33954')