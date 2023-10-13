load C:/Research_Foundation/data/protein_data_bank\6YVR\6YVR_AAA.pdb
load C:/Research_Foundation/data/protein_data_bank\6ZA8\6ZA8_AAA.pdb
align 6YVR_AAA, 6ZA8_AAA
cmd.set('seq_view', 1)
print(f'TMalign: 0.2218')