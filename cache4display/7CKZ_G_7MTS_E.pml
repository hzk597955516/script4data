load C:/Research_Foundation/data/protein_data_bank\7CKZ\7CKZ_G.pdb
load C:/Research_Foundation/data/protein_data_bank\7MTS\7MTS_E.pdb
align 7CKZ_G, 7MTS_E
cmd.set('seq_view', 1)
print(f'TMalign: 0.3252')