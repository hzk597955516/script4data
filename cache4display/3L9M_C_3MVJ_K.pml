load C:/Research_Foundation/data/protein_data_bank_kinase\3L9M\3L9M_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3MVJ\3MVJ_K.pdb
align 3L9M_C, 3MVJ_K
cmd.set('seq_view', 1)
print(f'TMscore: 0.50169')