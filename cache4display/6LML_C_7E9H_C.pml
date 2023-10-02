load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\7E9H\7E9H_C.pdb
align 6LML_C, 7E9H_C
cmd.set('seq_view', 1)
print(f'TMscore: 0.35299')