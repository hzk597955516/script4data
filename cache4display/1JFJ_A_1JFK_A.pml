load C:/Research_Foundation/data/protein_data_bank\1JFJ\1JFJ_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1JFK\1JFK_A.pdb
align 1JFJ_A, 1JFK_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.53259')