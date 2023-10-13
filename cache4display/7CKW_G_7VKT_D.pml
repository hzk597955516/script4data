load C:/Research_Foundation/data/protein_data_bank\7CKW\7CKW_G.pdb
load C:/Research_Foundation/data/protein_data_bank\7VKT\7VKT_D.pdb
align 7CKW_G, 7VKT_D
cmd.set('seq_view', 1)
print(f'TMalign: 0.658')