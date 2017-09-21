#!/usr/bin/env python
# -*- coding:utf8 -*-

def lines(file):
	for line in file: yield line
	yield '\n' # 确保文件的最后一行是空行

def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():  # 如果不是空行
			block.append(line)
		elif block:   # 如果不是空block
			yield ''.join(block).strip()
			block = []
        # 不会返回空块
