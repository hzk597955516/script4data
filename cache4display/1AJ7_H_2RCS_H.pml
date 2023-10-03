load C:/Research_Foundation/data/protein_data_bank\1AJ7\1AJ7_H.pdb
load C:/Research_Foundation/data/protein_data_bank\2RCS\2RCS_H.pdb
align 1AJ7_H, 2RCS_H
cmd.set('seq_view', 1)
print(f'TMscore: 0.57446')