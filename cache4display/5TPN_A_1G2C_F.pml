load C:/Research_Foundation/data/protein_data_bank\5TPN\5TPN_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1G2C\1G2C_F.pdb
align 5TPN_A, 1G2C_F
cmd.set('seq_view', 1)
print(f'TMscore: 0.71837')