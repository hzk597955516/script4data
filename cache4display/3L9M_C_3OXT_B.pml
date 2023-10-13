load C:/Research_Foundation/data/protein_data_bank_kinase\3L9M\3L9M_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3OXT\3OXT_B.pdb
align 3L9M_C, 3OXT_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.66302')