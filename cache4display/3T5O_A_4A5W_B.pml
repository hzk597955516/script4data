load C:/Research_Foundation/data/protein_data_bank\3T5O\3T5O_A.pdb
load C:/Research_Foundation/data/protein_data_bank\4A5W\4A5W_B.pdb
align 3T5O_A, 4A5W_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.58687')