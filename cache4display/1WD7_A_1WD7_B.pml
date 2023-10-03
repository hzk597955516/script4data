load C:/Research_Foundation/data/protein_data_bank\1WD7\1WD7_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1WD7\1WD7_B.pdb
align 1WD7_A, 1WD7_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.98267')