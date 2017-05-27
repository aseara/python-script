#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : aseara@163.com
# date: 2017-05-26
# version: 0.1
# desc hdf框架中的sqlmap调整，唯一约束相关
import re
from os import listdir, path


def modify_sqlmap(new_path, old_path, sqlmap):
    f = open(new_path + sqlmap, 'r')
    new_xml = f.read()
    f.close()
    pattern = re.compile(r'.*(<select id="checkUniqueCount".*?>.*?</select>)', re.S)
    new_check_sql = pattern.match(new_xml).group(1)

    f = open(old_path + sqlmap, 'r')
    old_xml = f.read()
    f.close()
    old_xml = re.sub('(?s)<select id="checkUniqueCount".*?>.*?</select>', new_check_sql, old_xml)

    pattern = re.compile(r'.*<sql id="SQL_\w*_NID_WHERE">\s*(.*?)\s*</sql>', re.S)
    nid_where_sql_content = pattern.match(old_xml).group(1)

    old_xml = re.sub('(?s)\s*(<!--\s*\w*\s*-->)?\s*<sql id="SQL_\w*_NID_WHERE">.*?</sql>', '', old_xml)
    old_xml = re.sub('(?s)<include\s+refid="SQL_\w*_NID_WHERE"\s*/>', nid_where_sql_content, old_xml)

    f = open(old_path + sqlmap, 'w')
    f.write(old_xml)
    f.close()

if __name__ == "__main__":
    new_p = 'D:/temp/mybatis/'
    old_p = 'E:/prjs/hdf/hbm/be/src/main/resources/mybatis/sys/'
    for sm in listdir(new_p):
        if path.exists(old_p + sm) and path.isfile(old_p + sm):
            modify_sqlmap(new_p, old_p, sm)
