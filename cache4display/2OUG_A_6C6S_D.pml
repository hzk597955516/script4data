load C:/Research_Foundation/data/protein_data_bank\2OUG\2OUG_A.pdb
load C:/Research_Foundation/data/protein_data_bank\6C6S\6C6S_D.pdb
align 2OUG_A, 6C6S_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.59261')