load C:/Research_Foundation/data/protein_data_bank\1K2H\1K2H_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1ZFS\1ZFS_A.pdb
align 1K2H_A, 1ZFS_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.51926')