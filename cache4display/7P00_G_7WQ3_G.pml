load ./pdb_result_au\7P00\7P00_G.pdb
load ./pdb_result_au\7WQ3\7WQ3_G.pdb
align 7P00_G, 7WQ3_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.91493')