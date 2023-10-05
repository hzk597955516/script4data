load C:/Research_Foundation/data/protein_data_bank_kinase\7LBM\7LBM_w_.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7NVR\7NVR_m_.pdb
align 7LBM_w_, 7NVR_m_
cmd.set('seq_view', 1)
print(f'TMalign: 0.1187')