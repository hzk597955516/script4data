load C:/Research_Foundation/data/protein_data_bank\7CKY\7CKY_G.pdb
load C:/Research_Foundation/data/protein_data_bank\7EW3\7EW3_C.pdb
align 7CKY_G, 7EW3_C
cmd.set('seq_view', 1)
print(f'TMalign: 0.3453')