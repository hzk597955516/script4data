load ./pdb_result_au\6P9X\6P9X_B.pdb
load ./pdb_result_au\6P9Y\6P9Y_B.pdb
align 6P9X_B, 6P9Y_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.99573')