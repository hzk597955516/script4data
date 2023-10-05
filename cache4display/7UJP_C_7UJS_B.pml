load C:/Research_Foundation/data/protein_data_bank_kinase\7UJP\7UJP_C.pdb
load C:/Research_Foundation/data/protein_data_bank_kinase\7UJS\7UJS_B.pdb
align 7UJP_C, 7UJS_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.55788')