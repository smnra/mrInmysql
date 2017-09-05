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
        #如果路径不存在 则打印'Path Is Not Exist!' 函数返回 -1
        print('FileName Is Not Exist!')
        return -1
    if not os.path.exists(tagPath) :
        #如果路径不存在 则打印'Path Is Not Exist!' 函数返回 -2
        print('FileName Is Not Exist!')
        return -2
    #tarfile 打开压缩包文件
    tar = tarfile.open(fileName)
    #获取压缩包内的文件名保存到names
    names = tar.getnames()
    for name in names:
        #遍历文件名列表,如果 匹配正则表达式函数 isMatch() 则解压缩 文件到 tagPath 文件夹
        if isMatch(reStr,name):
            tar.extract(name, tagPath)
            print(name)
    tar.close()
    return 0

if __name__ ==  '__main__' :
   unzip(reStr, 'H:\\BaiduYunDownload\\test\\20170725.csv.tar.gzip',  'H:\\BaiduYunDownload\\test\\sx')



