load C:/Research_Foundation/data/protein_data_bank\1PFL\1PFL_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1FIL\1FIL_A.pdb
align 1PFL_A, 1FIL_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.89035')