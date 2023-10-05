load C:/Research_Foundation/data/protein_data_bank_kinase\7ENA\7ENA_s_.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7NVR\7NVR_m_.pdb
align 7ENA_s_, 7NVR_m_
cmd.set('seq_view', 1)
print(f'TMscore: 0.50768')