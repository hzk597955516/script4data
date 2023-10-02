load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\7V9M\7V9M_Y.pdb
align 6LML_C, 7V9M_Y
cmd.set('seq_view', 1)
print(f'TMscore: 0.67775')