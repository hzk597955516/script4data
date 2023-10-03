load C:/Research_Foundation/data/protein_data_bank\1IJA\1IJA_A.pdb
load C:/Research_Foundation/data/protein_data_bank\2KID\2KID_A.pdb
align 1IJA_A, 2KID_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.80326')