load C:/Research_Foundation/data/protein_data_bank\1DMO\1DMO_A.pdb
load C:/Research_Foundation/data/protein_data_bank\3CLN\3CLN_A.pdb
align 1DMO_A, 3CLN_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.32546')