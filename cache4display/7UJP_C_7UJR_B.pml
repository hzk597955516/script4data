load C:/Research_Foundation/data/protein_data_bank_kinase\7UJP\7UJP_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7UJR\7UJR_B.pdb
align 7UJP_C, 7UJR_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.2975')