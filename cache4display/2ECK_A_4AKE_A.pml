load C:/Research_Foundation/data/protein_data_bank\2ECK\2ECK_A.pdb
load C:/Research_Foundation/data/protein_data_bank\4AKE\4AKE_A.pdb
align 2ECK_A, 4AKE_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.68483')