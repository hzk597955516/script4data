load C:/Research_Foundation/data/protein_data_bank_kinase\3MVJ\3MVJ_I.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4UJB\4UJB_B.pdb
align 3MVJ_I, 4UJB_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.61771')