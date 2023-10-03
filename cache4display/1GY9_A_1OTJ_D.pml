load C:/Research_Foundation/data/protein_data_bank\1GY9\1GY9_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1OTJ\1OTJ_D.pdb
align 1GY9_A, 1OTJ_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.94961')