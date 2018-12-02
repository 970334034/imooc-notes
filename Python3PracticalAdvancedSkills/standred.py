#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 13:30:53
# @Author  : Lewis Tian (chtian@hust.edu.cn)
# @Link    : https://lewistian.github.io
# @Version : Python3.7
# @Desc	   : 用来格式化 pynb 的 cell 显示的数字顺序

import json
from glob import glob


def regular(file):
	with open(file, encoding='utf-8') as f:
		data = json.load(f)
	cells = data['cells']
	index = 1
	for i in cells:
		if 'code' == i['cell_type']:
			if i['execution_count'] != index:
				i['execution_count'] = index
				if 'execution_count' in i['outputs'][0].keys():
					i['outputs'][0]['execution_count'] = index
			index += 1
	with open(file, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
	for x in glob('*.ipynb'):
		regular(x)
