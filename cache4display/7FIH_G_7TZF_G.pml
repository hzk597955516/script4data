load ./pdb_result_au\7FIH\7FIH_G.pdb
load ./pdb_result_au\7TZF\7TZF_G.pdb
align 7FIH_G, 7TZF_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.92622')