load C:/Research_Foundation/data/protein_data_bank\1XJT\1XJT_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1XJU\1XJU_B.pdb
align 1XJT_A, 1XJU_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.76203')