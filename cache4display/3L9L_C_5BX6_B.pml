load C:/Research_Foundation/data/protein_data_bank_kinase\3L9L\3L9L_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\5BX6\5BX6_B.pdb
align 3L9L_C, 5BX6_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.65451')