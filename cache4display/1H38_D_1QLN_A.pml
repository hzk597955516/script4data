load C:/Research_Foundation/data/protein_data_bank\1H38\1H38_D.pdb
load C:/Research_Foundation/data/protein_data_bank\1QLN\1QLN_A.pdb
align 1H38_D, 1QLN_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.73037')