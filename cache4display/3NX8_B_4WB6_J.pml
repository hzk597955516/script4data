load C:/Research_Foundation/data/protein_data_bank_kinase\3NX8\3NX8_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB6\4WB6_J.pdb
align 3NX8_B, 4WB6_J
cmd.set('seq_view', 1)
print(f'TMalign: 0.43833')