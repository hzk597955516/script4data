load C:/Research_Foundation/data/protein_data_bank_kinase\3MVJ\3MVJ_I.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3P0M\3P0M_B.pdb
align 3MVJ_I, 3P0M_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.64461')