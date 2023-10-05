load C:/Research_Foundation/data/protein_data_bank_kinase\7EGC\7EGC_D.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7ENA\7ENA_Dd.pdb
align 7EGC_D, 7ENA_Dd
cmd.set('seq_view', 1)
print(f'TMscore: 0.67802')