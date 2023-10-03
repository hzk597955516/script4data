load C:/Research_Foundation/data/protein_data_bank\2LV1\2LV1_A.pdb
load C:/Research_Foundation/data/protein_data_bank\6LNI\6LNI_A.pdb
align 2LV1_A, 6LNI_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.25079')