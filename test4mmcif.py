from mmcif_parsing import parse as mmcif_parse
import os


root = 'C:/Research_Foundation/data/mmcifs_kinase'

def test(pid):
    print(os.path.join(root, pid + '.cif'))
    return mmcif_parse(file_id=pid, mmcif_file=os.path.join(root, pid + '.cif'))


def test4kinase(file_name):
    print(os.path.join(root, file_name))
    return mmcif_parse(file_id='3MV5', mmcif_file=os.path.join(root, file_name))

if __name__ == "__main__":
    parser = test('7ENA')