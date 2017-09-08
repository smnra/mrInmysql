#!/usr/bin/env python
# coding = utf-8


import sys
from unzip import *
from getfiles import *
from inmysql import *


#获取当前脚本运行时的参数 如果只有1个参数(脚本自身),则打印提示信息
if len(sys.argv) == 1 :
    print('Not Find Path, arg1 is path of the ".tgz" file path.')
    exit()
elif len(sys.argv) > 1 :
    #如果路径不存在 则打印'Path Is Not Exist!' 退出脚本
    if not os.path.exists(sys.argv[1]) :
        print('Path Is Not Exist!')
        exit()


#从参数获取保存压缩包的路径
#压缩包所在的文件路径 为脚本运行时的第一个参数
basePath = sys.argv[1]
#压缩包解压路径

#压缩包的扩展名列表
typelist = '.gz', '.gzip', '.tgz'
#压缩文件列表
ziplist = []
#csv文件列表
csvlist = []

#匹配csv文件名的正则表达式
reStr = r'Baoji-cell|Xian-cell|Xianyang-cell|Hanzhong-cell|Tongchuan-cell|Shangluo-cell|Yulin-cell|Yanan-cell|Weinan-cell|Ankang-cell'
#mysql连接字符串
mysql_uri = 'mysql+pymysql://root:10300@192.168.3.74:50014/temp?charset=utf8'



#获取指定文件夹basePath 下的所有 '.gz', '.gzip', '.tgz' 文件 保存到ziplist
ziplist = getGzipList(basePath, '.gz', '.gzip', '.tgz')

#遍历压缩包文件名列表 ziplist
for zip in ziplist :
    #根据正则表达式reStr 匹配  解压缩相应的文件 并把已解压缩的文件路径保存到unzipfiles
    unzipfiles = unzip(reStr, zip)
    #遍历unzipfiles  判断csvfile中包含 cell 还是包含 wifi 来判断录入相应的表
    for csvfile in  unzipfiles :
        if 'cell' in csvfile :
            tablename = 'mr_cell'
            #读取scv文件csvfile，把表格写进mysql中tablename表中
            inmysql(mysql_uri, tablename, csvfile)

