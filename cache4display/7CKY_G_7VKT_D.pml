load C:/Research_Foundation/data/protein_data_bank\7CKY\7CKY_G.pdb
load C:/Research_Foundation/data/protein_data_bank\7VKT\7VKT_D.pdb
align 7CKY_G, 7VKT_D
cmd.set('seq_view', 1)
print(f'TMalign: 0.6443')