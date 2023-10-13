load C:/Research_Foundation/data/protein_data_bank_kinase\3MVJ\3MVJ_I.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3OOG\3OOG_B.pdb
align 3MVJ_I, 3OOG_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.6907')