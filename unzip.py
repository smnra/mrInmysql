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


def unzip(reStr,fileName) :
    #定义已解压的文件名
    unzipfiles = []
    if not os.path.exists(fileName) :
        #如果路径不存在 则打印'Path Is Not Exist!' 函数返回 -1
        print('File Does Not Exist!!!')
        return -1

    #替换文件路径中的'.' 为 '_",创建文件夹
    tagPath = fileName.replace('.', '_')
    if not os.path.exists(tagPath) :
        #如果路径tagPath不存在 则创建
        os.makedirs(tagPath)

    #tarfile 打开压缩包文件
    tar = tarfile.open(fileName)
    #获取压缩包内的文件名保存到names
    names = tar.getnames()
    for name in names:
        #遍历文件名列表,如果 匹配正则表达式函数 isMatch() 则解压缩 文件到 tagPath 文件夹
        if isMatch(reStr,name):
            tar.extract(name, tagPath)
            unzipfiles.append(os.path.join(tagPath, name))
            print(os.path.abspath(name))
    tar.close()
    return unzipfiles

if __name__ ==  '__main__' :
   unzip(reStr, r'H:\BaiduYunDownload\testw文件\20170702-1.csv.tar.gzip')



