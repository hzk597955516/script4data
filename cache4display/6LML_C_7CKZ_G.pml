load ./pdb_result_au\6LML\6LML_C.pdb
load ./pdb_result_au\7CKZ\7CKZ_G.pdb
align 6LML_C, 7CKZ_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.65927')