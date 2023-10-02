load ./pdb_result_au\7S8M\7S8M_B.pdb
load ./pdb_result_au\7WQ3\7WQ3_A.pdb
align 7S8M_B, 7WQ3_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.96996')