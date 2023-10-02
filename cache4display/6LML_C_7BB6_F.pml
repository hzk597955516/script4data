load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\7BB6\7BB6_F.pdb
align 6LML_C, 7BB6_F
cmd.set('seq_view', 1)
print(f'TMscore: 0.59068')