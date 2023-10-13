load C:/Research_Foundation/data/protein_data_bank\7AUE\7AUE_G.pdb
load C:/Research_Foundation/data/protein_data_bank\7CKY\7CKY_G.pdb
align 7AUE_G, 7CKY_G
cmd.set('seq_view', 1)
print(f'TMalign: 0.2914')