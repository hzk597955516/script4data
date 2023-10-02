load C:/Research_Foundation/data/protein_data_bank\2GRM\2GRM_B.pdb
load C:/Research_Foundation/data/protein_data_bank\2AXZ\2AXZ_A.pdb
align 2GRM_B, 2AXZ_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.95047')