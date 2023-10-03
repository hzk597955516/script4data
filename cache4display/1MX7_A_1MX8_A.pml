load C:/Research_Foundation/data/protein_data_bank\1MX7\1MX7_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1MX8\1MX8_A.pdb
align 1MX7_A, 1MX8_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.91326')