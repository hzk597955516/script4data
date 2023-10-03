load C:/Research_Foundation/data/protein_data_bank\2HDM\2HDM_A.pdb
load C:/Research_Foundation/data/protein_data_bank\2N54\2N54_B.pdb
align 2HDM_A, 2N54_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.33784')