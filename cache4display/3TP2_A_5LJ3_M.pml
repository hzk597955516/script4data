load C:/Research_Foundation/data/protein_data_bank\3TP2\3TP2_A.pdb
load C:/Research_Foundation/data/protein_data_bank\5LJ3\5LJ3_M.pdb
align 3TP2_A, 5LJ3_M
cmd.set('seq_view', 1)
print(f'TMscore: 0.31168')