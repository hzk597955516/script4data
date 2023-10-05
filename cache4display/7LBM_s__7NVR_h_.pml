load C:/Research_Foundation/data/protein_data_bank_kinase\7LBM\7LBM_s_.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7NVR\7NVR_h_.pdb
align 7LBM_s_, 7NVR_h_
cmd.set('seq_view', 1)
print(f'TMalign: 0.50116')