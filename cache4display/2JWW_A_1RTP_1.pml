load C:/Research_Foundation/data/protein_data_bank\2JWW\2JWW_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1RTP\1RTP_1.pdb
align 2JWW_A, 1RTP_1
cmd.set('seq_view', 1)
print(f'TMscore: 0.7584')