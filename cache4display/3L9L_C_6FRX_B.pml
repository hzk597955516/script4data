load C:/Research_Foundation/data/protein_data_bank_kinase\3L9L\3L9L_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\6FRX\6FRX_B.pdb
align 3L9L_C, 6FRX_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.63872')