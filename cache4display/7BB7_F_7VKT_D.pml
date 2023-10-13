load C:/Research_Foundation/data/protein_data_bank\7BB7\7BB7_F.pdb
load C:/Research_Foundation/data/protein_data_bank\7VKT\7VKT_D.pdb
align 7BB7_F, 7VKT_D
cmd.set('seq_view', 1)
print(f'TMalign: 0.6571')