load C:/Research_Foundation/data/protein_data_bank\1FSF\1FSF_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1FQO\1FQO_B.pdb
align 1FSF_A, 1FQO_B
cmd.set('seq_view', 1)
print(f'TMscore: 0.96975')