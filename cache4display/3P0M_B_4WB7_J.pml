load C:/Research_Foundation/data/protein_data_bank_kinase\3P0M\3P0M_B.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB7\4WB7_J.pdb
align 3P0M_B, 4WB7_J
cmd.set('seq_view', 1)
print(f'TMalign: 0.4454')