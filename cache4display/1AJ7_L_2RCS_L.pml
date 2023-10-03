load C:/Research_Foundation/data/protein_data_bank\1AJ7\1AJ7_L.pdb
load C:/Research_Foundation/data/protein_data_bank\2RCS\2RCS_L.pdb
align 1AJ7_L, 2RCS_L
cmd.set('seq_view', 1)
print(f'TMscore: 0.57955')