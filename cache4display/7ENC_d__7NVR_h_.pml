load C:/Research_Foundation/data/protein_data_bank_kinase\7ENC\7ENC_d_.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7NVR\7NVR_h_.pdb
align 7ENC_d_, 7NVR_h_
cmd.set('seq_view', 1)
print(f'TMalign: 0.3745')