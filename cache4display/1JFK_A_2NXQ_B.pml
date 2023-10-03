load C:/Research_Foundation/data/protein_data_bank\1JFK\1JFK_A.pdb
load C:/Research_Foundation/data/protein_data_bank\2NXQ\2NXQ_B.pdb
align 1JFK_A, 2NXQ_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.43261')