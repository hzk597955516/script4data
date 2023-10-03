load C:/Research_Foundation/data/protein_data_bank\1IYT\1IYT_A.pdb
load C:/Research_Foundation/data/protein_data_bank\2NAO\2NAO_D.pdb
align 1IYT_A, 2NAO_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.21984')