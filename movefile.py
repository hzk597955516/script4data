import os
import shutil


def movefiles2other(root, target):

    children = os.listdir(root)
    num = 0

    if len(children) == 0: return 0

    if len(children[0]) >= 6 and children[0][-6] == '.':
        for child in children:
            shutil.copy(os.path.join(root, child), target)
            num += 1
            print('---' + child + ' is Ok !---')
    else:
        for child in children:
            num += movefiles2other(os.path.join(root, child), target)
            
    return num

def mycopyfile(srcfile, dstpath):                      
    fpath,fname = os.path.split(srcfile)           
    if not os.path.exists(dstpath):
        os.makedirs(dstpath)           
    shutil.copy(srcfile, os.path.join(dstpath, fname))          
        