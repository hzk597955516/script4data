load C:/Research_Foundation/data/protein_data_bank\2K0Q\2K0Q_A.pdb
load C:/Research_Foundation/data/protein_data_bank\2LEL\2LEL_A.pdb
align 2K0Q_A, 2LEL_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.54195')