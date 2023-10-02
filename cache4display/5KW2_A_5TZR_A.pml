load ./pdb_result_au\5KW2\5KW2_A.pdb
load ./pdb_result_au\5TZR\5TZR_A.pdb
align 5KW2_A, 5TZR_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.62521')