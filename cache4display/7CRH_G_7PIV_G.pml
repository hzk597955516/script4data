load ./pdb_result_au\7CRH\7CRH_G.pdb
load ./pdb_result_au\7PIV\7PIV_G.pdb
align 7CRH_G, 7PIV_G
cmd.set('seq_view', 1)
print(f'TMscore: 0.90459')