load C:/Research_Foundation/data/protein_data_bank\6LML\6LML_C.pdb
load C:/Research_Foundation/data/protein_data_bank\7E9G\7E9G_C.pdb
align 6LML_C, 7E9G_C
cmd.set('seq_view', 1)
print(f'TMalign: 0.657')