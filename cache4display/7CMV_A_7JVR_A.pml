load ./pdb_result_au\7CMV\7CMV_A.pdb
load ./pdb_result_au\7JVR\7JVR_A.pdb
align 7CMV_A, 7JVR_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.96467')