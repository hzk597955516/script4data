load C:/Research_Foundation/data/protein_data_bank_kinase\7KL0\7KL0_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7KL2\7KL2_B.pdb
align 7KL0_C, 7KL2_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.4206')