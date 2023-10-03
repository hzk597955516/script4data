load C:/Research_Foundation/data/protein_data_bank\4O0P\4O0P_A.pdb
load C:/Research_Foundation/data/protein_data_bank\4O01\4O01_D.pdb
align 4O0P_A, 4O01_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.84779')