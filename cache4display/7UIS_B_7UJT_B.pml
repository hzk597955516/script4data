load C:/Research_Foundation/data/protein_data_bank_kinase\7UIS\7UIS_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7UJT\7UJT_B.pdb
align 7UIS_B, 7UJT_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.64039')