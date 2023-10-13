load C:/Research_Foundation/data/protein_data_bank\7MTQ\7MTQ_A.pdb
load C:/Research_Foundation/data/protein_data_bank\7MTS\7MTS_A.pdb
align 7MTQ_A, 7MTS_A
cmd.set('seq_view', 1)
print(f'TMalign: 0.4787')