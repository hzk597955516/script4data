load C:/Research_Foundation/data/protein_data_bank_kinase\3AMB\3AMB_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3L9L\3L9L_C.pdb
align 3AMB_B, 3L9L_C
cmd.set('seq_view', 1)
print(f'TMscore: 0.64925')