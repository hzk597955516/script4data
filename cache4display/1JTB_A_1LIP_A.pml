load C:/Research_Foundation/data/protein_data_bank\1JTB\1JTB_A.pdb
load C:/Research_Foundation/data/protein_data_bank\1LIP\1LIP_A.pdb
align 1JTB_A, 1LIP_A
cmd.set('seq_view', 1)
print(f'TMscore: 0.67509')