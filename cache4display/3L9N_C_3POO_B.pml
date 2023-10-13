load C:/Research_Foundation/data/protein_data_bank_kinase\3L9N\3L9N_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3POO\3POO_B.pdb
align 3L9N_C, 3POO_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.43245')