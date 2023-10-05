load C:/Research_Foundation/data/protein_data_bank_kinase\3AMB\3AMB_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3L9N\3L9N_C.pdb
align 3AMB_B, 3L9N_C
cmd.set('seq_view', 1)
print(f'TMscore: 0.48423')