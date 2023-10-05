load C:/Research_Foundation/data/protein_data_bank_kinase\7EGB\7EGB_5.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7ENA\7ENA_5.pdb
align 7EGB_5, 7ENA_5
cmd.set('seq_view', 1)
print(f'TMscore: 0.66755')