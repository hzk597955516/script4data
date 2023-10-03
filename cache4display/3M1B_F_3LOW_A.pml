load C:/Research_Foundation/data/protein_data_bank\3M1B\3M1B_F.pdb
load C:/Research_Foundation/data/protein_data_bank\3LOW\3LOW_A.pdb
align 3M1B_F, 3LOW_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.54691')