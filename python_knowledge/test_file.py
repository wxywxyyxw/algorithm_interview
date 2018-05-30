# -*- coding: utf-8 -*-
"""
理解__file__
__file__ 就是一个路径
"""
import os

if __name__ == "__main__":
    print __file__, type(__file__)
    #  输出当前文件全路径 /Users/wangxiaoyang/PycharmProjects/algorithm_interview/python_knowledge/test_file.py  <type 'str'>
    print os.path.dirname(__file__)
    #  输出文件所在目录  /Users/wangxiaoyang/PycharmProjects/algorithm_interview/python_knowledge
    file_path = os.path.dirname(__file__)
    print type(file_path)  # 输出是字符串类型 <type 'str'>
    print os.path.join(file_path, 'template')
    # 输出 /Users/wangxiaoyang/PycharmProjects/algorithm_interview/python_knowledge/template
    # 是将两个目录用'/'组合在一起
