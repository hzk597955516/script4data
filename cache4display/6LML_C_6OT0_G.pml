load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\6OT0\6OT0_G.pdb
align 6LML_C, 6OT0_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.64682')