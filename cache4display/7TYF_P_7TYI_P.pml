load C:/Research_Foundation/data/protein_data_bank\7TYF\7TYF_P.pdb
load C:/Research_Foundation/data/protein_data_bank\7TYI\7TYI_P.pdb
align 7TYF_P, 7TYI_P
cmd.set('seq_view', 1)
print(f'TMalign: 0.5504')