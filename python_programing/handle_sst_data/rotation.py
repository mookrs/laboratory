# coding: utf-8
'''
    放到需要变换的 .txt 同级目录下执行，将在当前目录生成 rotation 文件夹，存放变换好的同名 .txt 数据。该 .txt 文件还加入了文件头。

    变换的规则如下：
    1,2,3      1,4,7      3,6,9
    4,5,6  =>  2,5,8  =>  2,5,8
    7,8,9      3,6,9      1,4,7

    已知问题：最后会多出一个空行。
'''

import os


def transpose_matrix(readpath, writepath):
    with open(readpath, 'r') as fileread, open(writepath, 'w') as filewrite:
        matrix = []
        for oldline in fileread.readlines():
            alist = oldline.rstrip().split('\t')
            matrix.append(alist)
        matrix_transposed = map(list, zip(*matrix))
        filewrite.writelines('ncols 1440\n')
        filewrite.writelines('nrows 720\n')
        filewrite.writelines('xllcorner 0.00\n')
        filewrite.writelines('yllcorner 0.00\n')
        filewrite.writelines('cellsize 0.25\n')
        filewrite.writelines('NODATA_value -9999.00\n')
        for alist_reverse in reversed(matrix_transposed):
            newline = '\t'.join(alist_reverse) + '\n'
            filewrite.writelines(newline)


if not os.path.exists('rotation'):
    os.mkdir('rotation')
file_paths = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".txt")]
for file_path_read in file_paths:
    file_path_split = os.path.split(file_path_read)
    file_path_write = os.path.join(file_path_split[0], 'rotation', file_path_split[1])
    transpose_matrix(file_path_read, file_path_write)
