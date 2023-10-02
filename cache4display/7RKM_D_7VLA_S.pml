load ./pdb_result_au\7RKM\7RKM_D.pdb
load ./pdb_result_au\7VLA\7VLA_S.pdb
align 7RKM_D, 7VLA_S
cmd.set('seq_view', 1)
print(f'TMscore: 0.98958')