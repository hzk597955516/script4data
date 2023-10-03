load C:/Research_Foundation/data/protein_data_bank\1X0G\1X0G_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1X0G\1X0G_D.pdb
align 1X0G_A, 1X0G_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.55323')