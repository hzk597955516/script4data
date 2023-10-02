load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\7WF7\7WF7_D.pdb
align 6LML_C, 7WF7_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.65388')