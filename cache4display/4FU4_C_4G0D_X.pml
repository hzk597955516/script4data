load C:/Research_Foundation/data/protein_data_bank\4FU4\4FU4_C.pdb
load C:/Research_Foundation/data/protein_data_bank\4G0D\4G0D_X.pdb
align 4FU4_C, 4G0D_X
cmd.set('seq_view', 1)
print(f'TMscore: 0.32117')