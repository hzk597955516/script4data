load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\7F2O\7F2O_Y.pdb
align 6LML_C, 7F2O_Y
cmd.set('seq_view', 1)
print(f'TMscore: 0.68887')