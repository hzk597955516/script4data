load C:/Research_Foundation/data/protein_data_bank\4PHU\4PHU_A.pdb
load C:/Research_Foundation/data/protein_data_bank\5KW2\5KW2_A.pdb
align 4PHU_A, 5KW2_A
cmd.set('seq_view', 1)
print(f'TMalign: 0.247')