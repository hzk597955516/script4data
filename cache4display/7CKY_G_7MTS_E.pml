load C:/Research_Foundation/data/protein_data_bank\7CKY\7CKY_G.pdb
load C:/Research_Foundation/data/protein_data_bank\7MTS\7MTS_E.pdb
align 7CKY_G, 7MTS_E
cmd.set('seq_view', 1)
print(f'TMalign: 0.3295')