load C:/Research_Foundation/data/protein_data_bank\1TFU\1TFU_A.pdb
load C:/Research_Foundation/data/protein_data_bank\3UC5\3UC5_A.pdb
align 1TFU_A, 3UC5_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.96727')