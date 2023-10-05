load C:/Research_Foundation/data/protein_data_bank_kinase\3L9M\3L9M_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4UJ1\4UJ1_B.pdb
align 3L9M_C, 4UJ1_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.66358')