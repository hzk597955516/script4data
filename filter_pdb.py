from movefile import mycopyfile_cmp
import os


root_path = 'C:/Research_Foundation'
pdb_path = 'C:/Research_Foundation/data/transfer_station/casp15_pre_data/sigma_1'
target_path = 'C:/Research_Foundation/practice'
times = os.listdir(pdb_path)

for time in times:
    
    t = time[-1]
    cur_pdb_path = os.path.join(pdb_path, time)
    pdbs = os.listdir(cur_pdb_path)
    
    for pdb in pdbs:
        if pdb.split('.')[-1] != 'pdb': continue
        pid = pdb.split('.')[0]
        dst_path = os.path.join(target_path, pid)
        
        mycopyfile_cmp(t, os.path.join(cur_pdb_path, pdb), dst_path)
        
    
