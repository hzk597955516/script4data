load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\7EZK\7EZK_G.pdb
align 6LML_C, 7EZK_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.69417')