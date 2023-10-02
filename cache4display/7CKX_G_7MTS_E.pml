load ./pdb_result_au\7CKX\7CKX_G.pdb
load ./pdb_result_au\7MTS\7MTS_E.pdb
align 7CKX_G, 7MTS_E
cmd.set('seq_view', 1)
print(f'TMscore: 0.69971')