load C:/Research_Foundation/data/protein_data_bank\5L35\5L35_D.pdb
load C:/Research_Foundation/data/protein_data_bank\5L35\5L35_G.pdb
align 5L35_D, 5L35_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.89498')