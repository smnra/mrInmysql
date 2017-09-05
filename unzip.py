#!/usr/bin/env python
# coding = utf-8


import os
import sys
import tarfile
import re


reStr = r'Baoji|Xian|Xianyang|Hanzhong|Tongchuan|Shangluo|Yulin|Yanan|Weinan|Ankang'

#定义正则表达式 来匹配文件名
def isMatch(reStr, fileName):
    pattern = re.compile(reStr)
    match = pattern.match(fileName)
    return match


def unzip(reStr,fileName,tagPath) :
    if not os.path.exists(fileName) :
        print('FileName Is Not Exist!')
        return -1
    if not os.path.exists(tagPath) :
        print('FileName Is Not Exist!')
        return -2

    tar = tarfile.open(fileName)
    names = tar.getnames()
    for name in names:
        if isMatch(reStr,fileName):
            #tar.extract(name, tagPath)
            print(name)
    return 0

if __name__ ==  '__main__' :
   unzip(reStr, '.\\test.tar.gzip', '.\\')



