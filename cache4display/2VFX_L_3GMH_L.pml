load C:/Research_Foundation/data/protein_data_bank\2VFX\2VFX_L.pdb
load C:/Research_Foundation/data/protein_data_bank\3GMH\3GMH_L.pdb
align 2VFX_L, 3GMH_L
cmd.set('seq_view', 1)
print(f'TMscore: 0.70005')