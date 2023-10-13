load C:/Research_Foundation/data/protein_data_bank\6YVR\6YVR_AAA.pdb
load C:/Research_Foundation/data/protein_data_bank\6Z4Q\6Z4Q_AAA.pdb
align 6YVR_AAA, 6Z4Q_AAA
cmd.set('seq_view', 1)
print(f'TMalign: 0.3099')