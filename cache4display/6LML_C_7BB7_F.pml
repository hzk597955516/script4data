load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\7BB7\7BB7_F.pdb
align 6LML_C, 7BB7_F
cmd.set('seq_view', 1)
print(f'TMscore: 0.66615')