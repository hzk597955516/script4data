load C:/Research_Foundation/data/protein_data_bank_kinase\3L9L\3L9L_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3MVJ\3MVJ_K.pdb
align 3L9L_C, 3MVJ_K
cmd.set('seq_view', 1)
print(f'TMalign: 0.52559')