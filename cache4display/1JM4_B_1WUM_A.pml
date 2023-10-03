load C:/Research_Foundation/data/protein_data_bank\1JM4\1JM4_B.pdb
load C:/Research_Foundation/data/protein_data_bank\1WUM\1WUM_A.pdb
align 1JM4_B, 1WUM_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.81256')