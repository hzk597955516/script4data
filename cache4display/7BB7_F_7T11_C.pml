load C:/Research_Foundation/data/protein_data_bank\7BB7\7BB7_F.pdb
load C:/Research_Foundation/data/protein_data_bank\7T11\7T11_C.pdb
align 7BB7_F, 7T11_C
cmd.set('seq_view', 1)
print(f'TMalign: 0.285')