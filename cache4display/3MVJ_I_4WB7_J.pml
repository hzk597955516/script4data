load C:/Research_Foundation/data/protein_data_bank_kinase\3MVJ\3MVJ_I.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4WB7\4WB7_J.pdb
align 3MVJ_I, 4WB7_J
cmd.set('seq_view', 1)
print(f'TMalign: 0.5681')