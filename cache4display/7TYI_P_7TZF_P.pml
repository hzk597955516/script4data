load C:/Research_Foundation/data/protein_data_bank\7TYI\7TYI_P.pdb
load C:/Research_Foundation/data/protein_data_bank\7TZF\7TZF_P.pdb
align 7TYI_P, 7TZF_P
cmd.set('seq_view', 1)
print(f'TMalign: 0.553')