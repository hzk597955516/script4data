load C:/Research_Foundation/data/protein_data_bank\7BB7\7BB7_F.pdb
load C:/Research_Foundation/data/protein_data_bank\7MTS\7MTS_E.pdb
align 7BB7_F, 7MTS_E
cmd.set('seq_view', 1)
print(f'TMalign: 0.2796')