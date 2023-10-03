load C:/Research_Foundation/data/protein_data_bank\5I2M\5I2M_A.pdb
load C:/Research_Foundation/data/protein_data_bank\5I2S\5I2S_A.pdb
align 5I2M_A, 5I2S_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.37327')