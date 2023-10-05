load C:/Research_Foundation/data/protein_data_bank_kinase\7EGC\7EGC_5.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7LBM\7LBM_c_.pdb
align 7EGC_5, 7LBM_c_
cmd.set('seq_view', 1)
print(f'TMalign: 0.1709')