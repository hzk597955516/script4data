load ./pdb_result_au\7T6B\7T6B_D.pdb
load ./pdb_result_au\7TYN\7TYN_G.pdb
align 7T6B_D, 7TYN_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.93624')