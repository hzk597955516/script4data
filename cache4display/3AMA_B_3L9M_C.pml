load C:/Research_Foundation/data/protein_data_bank_kinase\3AMA\3AMA_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3L9M\3L9M_C.pdb
align 3AMA_B, 3L9M_C
cmd.set('seq_view', 1)
print(f'TMalign: 0.6531')