load C:/Research_Foundation/data/protein_data_bank\5HK5\5HK5_H.pdb
load C:/Research_Foundation/data/protein_data_bank\4JPH\4JPH_B.pdb
align 5HK5_H, 4JPH_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.72657')