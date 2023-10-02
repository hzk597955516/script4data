load ./pdb_result_au\7T10\7T10_C.pdb
load ./pdb_result_au\7WUJ\7WUJ_Y.pdb
align 7T10_C, 7WUJ_Y
cmd.set('seq_view', 1)
print(f'TMscore: 0.68048')