load ./pdb_result_au\6WHA\6WHA_D.pdb
load ./pdb_result_au\7CKW\7CKW_G.pdb
align 6WHA_D, 7CKW_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.65122')