load ./pdb_result_au\6WHA\6WHA_D.pdb
load ./pdb_result_au\7E9H\7E9H_C.pdb
align 6WHA_D, 7E9H_C
cmd.set('seq_view', 1)
print(f'TMscore: 0.28319')