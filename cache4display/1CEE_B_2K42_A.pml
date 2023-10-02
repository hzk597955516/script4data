load C:/Research_Foundation/data/protein_data_bank\1CEE\1CEE_B.pdb
load C:/Research_Foundation/data/protein_data_bank\2K42\2K42_A.pdb
align 1CEE_B, 2K42_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.28474')