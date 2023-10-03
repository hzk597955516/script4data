load C:/Research_Foundation/data/protein_data_bank\3HDF\3HDF_A.pdb
load C:/Research_Foundation/data/protein_data_bank\3HDE\3HDE_A.pdb
align 3HDF_A, 3HDE_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.77421')