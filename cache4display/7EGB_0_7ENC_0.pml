load C:/Research_Foundation/data/protein_data_bank_kinase\7EGB\7EGB_0.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7ENC\7ENC_0.pdb
align 7EGB_0, 7ENC_0
cmd.set('seq_view', 1)
print(f'TMalign: 0.59045')