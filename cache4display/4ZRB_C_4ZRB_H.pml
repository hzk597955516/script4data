load C:/Research_Foundation/data/protein_data_bank\4ZRB\4ZRB_C.pdb
load C:/Research_Foundation/data/protein_data_bank\4ZRB\4ZRB_H.pdb
align 4ZRB_C, 4ZRB_H
cmd.set('seq_view', 1)
print(f'TMscore: 0.92908')