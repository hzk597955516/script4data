load C:/Research_Foundation/data/protein_data_bank_kinase\3L9M\3L9M_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3OWP\3OWP_B.pdb
align 3L9M_C, 3OWP_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.68479')