load C:/Research_Foundation/data/protein_data_bank_kinase\7EGC\7EGC_F.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7ENC\7ENC_DF.pdb
align 7EGC_F, 7ENC_DF
cmd.set('seq_view', 1)
print(f'TMscore: 0.60247')