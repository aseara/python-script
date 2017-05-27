#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : aseara@163.com
# date: 2017-05-26
# version: 0.1
# desc hdf框架中的sqlmap调整，唯一约束相关

# D:/temp/mybatis/SysAccount-sqlmap.xml
# E:/prjs/hdf/hbm/be/src/main/resources/mybatis/sys/SysAccount-sqlmap.xml

import re

f = open('D:/temp/mybatis/SysAccount-sqlmap.xml', 'r')
newXml = f.read()
f.close()
pattern = re.compile(r'.*(<select id="checkUniqueCount".*?>.*?</select>)', re.S)
newCheckSql = pattern.match(newXml).group(1)

f = open('E:/prjs/hdf/hbm/be/src/main/resources/mybatis/sys/SysAccount-sqlmap.xml', 'r')
oldXml = f.read()
f.close()
oldXml = re.sub('(?s)<select id="checkUniqueCount".*?>.*?</select>', newCheckSql, oldXml)

f = open('out.xml', 'w')
f.write(oldXml)
f.close