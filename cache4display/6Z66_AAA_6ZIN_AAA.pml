load C:/Research_Foundation/data/protein_data_bank\6Z66\6Z66_AAA.pdb
load C:/Research_Foundation/data/protein_data_bank\6ZIN\6ZIN_AAA.pdb
align 6Z66_AAA, 6ZIN_AAA
cmd.set('seq_view', 1)
print(f'TMalign: 0.3964')