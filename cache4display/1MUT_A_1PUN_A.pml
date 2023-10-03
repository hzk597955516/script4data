load C:/Research_Foundation/data/protein_data_bank\1MUT\1MUT_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1PUN\1PUN_A.pdb
align 1MUT_A, 1PUN_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.65543')