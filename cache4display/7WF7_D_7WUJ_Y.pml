load ./pdb_result_au\7WF7\7WF7_D.pdb
load ./pdb_result_au\7WUJ\7WUJ_Y.pdb
align 7WF7_D, 7WUJ_Y
cmd.set('seq_view', 1)
print(f'TMscore: 0.68821')