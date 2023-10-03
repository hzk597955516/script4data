load C:/Research_Foundation/data/protein_data_bank\5INE\5INE_A.pdb
load C:/Research_Foundation/data/protein_data_bank\3MKO\3MKO_A.pdb
align 5INE_A, 3MKO_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.32099')