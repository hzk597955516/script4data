load ./pdb_result_au\7MTS\7MTS_E.pdb
load ./pdb_result_au\7WUJ\7WUJ_Y.pdb
align 7MTS_E, 7WUJ_Y
cmd.set('seq_view', 1)
print(f'TMscore: 0.68033')