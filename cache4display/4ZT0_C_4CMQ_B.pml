load C:/Research_Foundation/data/protein_data_bank\4ZT0\4ZT0_C.pdb
load C:/Research_Foundation/data/protein_data_bank\4CMQ\4CMQ_B.pdb
align 4ZT0_C, 4CMQ_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.54416')