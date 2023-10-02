load ./pdb_result_au\6ORV\6ORV_BP.pdb
load ./pdb_result_au\7TZF\7TZF_B.pdb
align 6ORV_BP, 7TZF_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.99633')