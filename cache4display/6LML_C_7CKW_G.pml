load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\7CKW\7CKW_G.pdb
align 6LML_C, 7CKW_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.67041')