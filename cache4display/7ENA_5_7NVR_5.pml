load C:/Research_Foundation/data/protein_data_bank_kinase\7ENA\7ENA_5.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7NVR\7NVR_5.pdb
align 7ENA_5, 7NVR_5
cmd.set('seq_view', 1)
print(f'TMscore: 0.68016')