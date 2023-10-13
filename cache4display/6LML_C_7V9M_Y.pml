load C:/Research_Foundation/data/protein_data_bank\6LML\6LML_C.pdb
load C:/Research_Foundation/data/protein_data_bank\7V9M\7V9M_Y.pdb
align 6LML_C, 7V9M_Y
cmd.set('seq_view', 1)
print(f'TMalign: 0.2872')