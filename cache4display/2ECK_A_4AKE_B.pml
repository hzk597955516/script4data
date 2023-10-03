load C:/Research_Foundation/data/protein_data_bank\2ECK\2ECK_A.pdb
load C:/Research_Foundation/data/protein_data_bank\4AKE\4AKE_B.pdb
align 2ECK_A, 4AKE_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.68868')