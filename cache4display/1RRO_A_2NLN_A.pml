load C:/Research_Foundation/data/protein_data_bank\1RRO\1RRO_A.pdb
load C:/Research_Foundation/data/protein_data_bank\2NLN\2NLN_A.pdb
align 1RRO_A, 2NLN_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.65718')