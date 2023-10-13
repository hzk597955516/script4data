load C:/Research_Foundation/data/protein_data_bank\7CKX\7CKX_G.pdb
load C:/Research_Foundation/data/protein_data_bank\7MTS\7MTS_E.pdb
align 7CKX_G, 7MTS_E
cmd.set('seq_view', 1)
print(f'TMalign: 0.3288')