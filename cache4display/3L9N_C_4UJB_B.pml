load C:/Research_Foundation/data/protein_data_bank_kinase\3L9N\3L9N_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\4UJB\4UJB_B.pdb
align 3L9N_C, 4UJB_B
cmd.set('seq_view', 1)
print(f'TMalign: 0.43635')