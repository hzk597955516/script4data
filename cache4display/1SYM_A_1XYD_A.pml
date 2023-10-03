load C:/Research_Foundation/data/protein_data_bank\1SYM\1SYM_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1XYD\1XYD_A.pdb
align 1SYM_A, 1XYD_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.58115')