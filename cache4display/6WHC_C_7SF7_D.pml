load ./pdb_result_au\6WHC\6WHC_C.pdb
load ./pdb_result_au\7SF7\7SF7_D.pdb
align 6WHC_C, 7SF7_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.6787')