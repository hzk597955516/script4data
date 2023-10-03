load C:/Research_Foundation/data/protein_data_bank\1Q95\1Q95_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1ZA1\1ZA1_A.pdb
align 1Q95_A, 1ZA1_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.94372')