load C:/Research_Foundation/data/protein_data_bank\1MNM\1MNM_C.pdb
load C:/Research_Foundation/data/protein_data_bank\1MNM\1MNM_D.pdb
align 1MNM_C, 1MNM_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.75257')