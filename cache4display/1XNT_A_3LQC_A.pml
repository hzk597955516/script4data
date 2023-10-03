load C:/Research_Foundation/data/protein_data_bank\1XNT\1XNT_A.pdb
load C:/Research_Foundation/data/protein_data_bank\3LQC\3LQC_A.pdb
align 1XNT_A, 3LQC_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.72217')