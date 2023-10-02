load ./pdb_result_au\6WHA\6WHA_D.pdb
load ./pdb_result_au\7WUJ\7WUJ_Y.pdb
align 6WHA_D, 7WUJ_Y
cmd.set('seq_view', 1)
print(f'TMscore: 0.67269')