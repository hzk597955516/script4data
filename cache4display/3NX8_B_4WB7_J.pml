load C:/Research_Foundation/data/protein_data_bank_kinase\3NX8\3NX8_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB7\4WB7_J.pdb
align 3NX8_B, 4WB7_J
cmd.set('seq_view', 1)
print(f'TMalign: 0.52644')