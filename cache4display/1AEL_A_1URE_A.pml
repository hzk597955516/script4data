load C:/Research_Foundation/data/protein_data_bank\1AEL\1AEL_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1URE\1URE_A.pdb
align 1AEL_A, 1URE_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.80656')