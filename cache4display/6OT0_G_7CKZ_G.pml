load C:/Research_Foundation/data/protein_data_bank\6OT0\6OT0_G.pdb
load C:/Research_Foundation/data/protein_data_bank\7CKZ\7CKZ_G.pdb
align 6OT0_G, 7CKZ_G
cmd.set('seq_view', 1)
print(f'TMalign: 0.6827')