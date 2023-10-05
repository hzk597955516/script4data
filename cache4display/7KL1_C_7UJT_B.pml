load C:/Research_Foundation/data/protein_data_bank_kinase\7KL1\7KL1_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7UJT\7UJT_B.pdb
align 7KL1_C, 7UJT_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.66126')