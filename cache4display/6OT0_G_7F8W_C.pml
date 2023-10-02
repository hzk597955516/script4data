load ./pdb_result_au\6OT0\6OT0_G.pdb
load ./pdb_result_au\7F8W\7F8W_C.pdb
align 6OT0_G, 7F8W_C
cmd.set('seq_view', 1)
print(f'TMscore: 0.63672')