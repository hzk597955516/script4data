load C:/Research_Foundation/data/protein_data_bank_kinase\3L9M\3L9M_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\3VQH\3VQH_B.pdb
align 3L9M_C, 3VQH_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.63996')