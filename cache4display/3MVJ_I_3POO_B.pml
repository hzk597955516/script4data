load C:/Research_Foundation/data/protein_data_bank_kinase\3MVJ\3MVJ_I.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3POO\3POO_B.pdb
align 3MVJ_I, 3POO_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.6243')