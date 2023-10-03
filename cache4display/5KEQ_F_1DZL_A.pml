load C:/Research_Foundation/data/protein_data_bank\5KEQ\5KEQ_F.pdb
load C:/Research_Foundation/data/protein_data_bank\1DZL\1DZL_A.pdb
align 5KEQ_F, 1DZL_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.93')