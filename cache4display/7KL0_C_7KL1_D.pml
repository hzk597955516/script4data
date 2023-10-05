load C:/Research_Foundation/data/protein_data_bank_kinase\7KL0\7KL0_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7KL1\7KL1_D.pdb
align 7KL0_C, 7KL1_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.57496')