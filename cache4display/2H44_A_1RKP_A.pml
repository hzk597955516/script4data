load C:/Research_Foundation/data/protein_data_bank\2H44\2H44_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1RKP\1RKP_A.pdb
align 2H44_A, 1RKP_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.92729')