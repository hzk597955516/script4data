load C:/Research_Foundation/data/protein_data_bank_kinase\1Y57\1Y57_A.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\2SRC\2SRC_A.pdb
align 1Y57_A, 2SRC_A
cmd.set('seq_view', 1)
print(f'TMalign: 0.54093')