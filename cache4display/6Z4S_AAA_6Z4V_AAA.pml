load C:/Research_Foundation/data/protein_data_bank\6Z4S\6Z4S_AAA.pdb
load C:/Research_Foundation/data/protein_data_bank\6Z4V\6Z4V_AAA.pdb
align 6Z4S_AAA, 6Z4V_AAA
cmd.set('seq_view', 1)
print(f'TMalign: 0.564')