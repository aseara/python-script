#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : aseara@163.com
# date: 2017-09-08
# version: 0.1
# desc 删除项目中的Idea配置文件

import sys
import os


def iml_remove(root_dir):
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        if os.path.isdir(path):
            if os.path.basename(path) == '.idea':
                print 'remove ' + path
                os.rmdir(path)
            else:
                iml_remove(path)
        elif path.endswith('.iml'):
            print 'remove ' + path
            os.remove(path)


# use: python removeiml.py E:\prjs\ete\ete
if __name__ == "__main__":
    rootDir = sys.argv[1]
    print 'project root dir: ' + rootDir
    iml_remove(rootDir)
