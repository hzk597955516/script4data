load C:/Research_Foundation/data/protein_data_bank_kinase\3L9M\3L9M_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3MVJ\3MVJ_J.pdb
align 3L9M_C, 3MVJ_J
cmd.set('seq_view', 1)
print(f'TMalign: 0.59827')