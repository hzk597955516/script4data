load C:/Research_Foundation/data/protein_data_bank\2KKW\2KKW_A.pdb
load C:/Research_Foundation/data/protein_data_bank\2N0A\2N0A_D.pdb
align 2KKW_A, 2N0A_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.18927')