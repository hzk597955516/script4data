load C:/Research_Foundation/data/protein_data_bank_kinase\7ENA\7ENA_d_.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7LBM\7LBM_s_.pdb
align 7ENA_d_, 7LBM_s_
cmd.set('seq_view', 1)
print(f'TMalign: 0.5058')