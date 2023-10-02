load ./pdb_result_au\7AUE\7AUE_G.pdb
load ./pdb_result_au\7CKY\7CKY_G.pdb
align 7AUE_G, 7CKY_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.69139')