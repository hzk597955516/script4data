load ./pdb_result_au\5GLH\5GLH_A.pdb
load ./pdb_result_au\6IGL\6IGL_A.pdb
align 5GLH_A, 6IGL_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.94423')