load C:/Research_Foundation/data/protein_data_bank_kinase\7EGC\7EGC_F.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7ENA\7ENA_DF.pdb
align 7EGC_F, 7ENA_DF
cmd.set('seq_view', 1)
print(f'TMalign: 0.3141')