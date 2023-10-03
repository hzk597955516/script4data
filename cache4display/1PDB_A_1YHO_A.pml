load C:/Research_Foundation/data/protein_data_bank\1PDB\1PDB_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1YHO\1YHO_A.pdb
align 1PDB_A, 1YHO_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.93511')