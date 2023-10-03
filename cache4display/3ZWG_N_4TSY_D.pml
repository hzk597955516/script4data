load C:/Research_Foundation/data/protein_data_bank\3ZWG\3ZWG_N.pdb
load C:/Research_Foundation/data/protein_data_bank\4TSY\4TSY_D.pdb
align 3ZWG_N, 4TSY_D
cmd.set('seq_view', 1)
print(f'TMscore: 0.85065')