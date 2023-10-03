from mmcif_parsing import parse as mmcif_parse
import os


root = 'C:/Research_Foundation/data/mmcifs'

def test(pid):
    print(os.path.join(root, pid + '.cif'))
    return mmcif_parse(file_id=pid, mmcif_file=os.path.join(root, pid + '.cif'))


if __name__ == "__main__":
    parser = test('4PJ1')