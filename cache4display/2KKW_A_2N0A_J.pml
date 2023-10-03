load C:/Research_Foundation/data/protein_data_bank\2KKW\2KKW_A.pdb
load C:/Research_Foundation/data/protein_data_bank\2N0A\2N0A_J.pdb
align 2KKW_A, 2N0A_J
cmd.set('seq_view', 1)
print(f'TMscore: 0.23137')