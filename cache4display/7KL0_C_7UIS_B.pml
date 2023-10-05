load C:/Research_Foundation/data/protein_data_bank_kinase\7KL0\7KL0_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7UIS\7UIS_B.pdb
align 7KL0_C, 7UIS_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.55515')