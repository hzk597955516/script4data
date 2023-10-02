load ./pdb_result_au\7FII\7FII_G.pdb
load ./pdb_result_au\7WUJ\7WUJ_Y.pdb
align 7FII_G, 7WUJ_Y
cmd.set('seq_view', 1)
print(f'TMscore: 0.68541')