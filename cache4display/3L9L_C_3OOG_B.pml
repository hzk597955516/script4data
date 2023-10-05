load C:/Research_Foundation/data/protein_data_bank_kinase\3L9L\3L9L_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3OOG\3OOG_B.pdb
align 3L9L_C, 3OOG_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.69571')