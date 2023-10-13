load C:/Research_Foundation/data/protein_data_bank\7CKZ\7CKZ_G.pdb
load C:/Research_Foundation/data/protein_data_bank\7FII\7FII_G.pdb
align 7CKZ_G, 7FII_G
cmd.set('seq_view', 1)
print(f'TMalign: 0.362')