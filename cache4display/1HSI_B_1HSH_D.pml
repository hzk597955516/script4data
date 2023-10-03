load C:/Research_Foundation/data/protein_data_bank\1HSI\1HSI_B.pdb
load C:/Research_Foundation/data/protein_data_bank\1HSH\1HSH_D.pdb
align 1HSI_B, 1HSH_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.94221')