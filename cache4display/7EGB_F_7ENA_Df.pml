load C:/Research_Foundation/data/protein_data_bank_kinase\7EGB\7EGB_F.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7ENA\7ENA_Df.pdb
align 7EGB_F, 7ENA_Df
cmd.set('seq_view', 1)
print(f'TMalign: 0.61329')