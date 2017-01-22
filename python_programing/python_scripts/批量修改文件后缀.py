# -*- coding:utf8 -*-

import os

# 列出当前目录下所有文件
files = os.listdir(".")

for filename in files:
    # 分离文件名与扩展名，默认返回(fname,fextension)元组，可做分片操作
    portion = os.path.splitext(filename)
    if portion[1].lower() == ".mp4":
        newname = portion[0] + ".rmvb"
        os.rename(filename, newname)
