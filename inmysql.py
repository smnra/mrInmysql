#!/usr/bin/env python
# coding = utf-8

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import re


filename = r'H:\BaiduYunDownload\testw文件\20170702-1_csv_tar_gzip\Ankang-cell-2017-07-02.csv'
mysql_uri = 'mysql+pymysql://root:10300@192.168.3.74:50014/temp?charset=utf8'
tablename = 'mr_cell'


#定义正则表达式 用来批量替换 列名中的 "\ ./ ( )"
reReplace = re.compile(r'[\.\\\(\)/]')
#print(reReplace.sub('_', '123abc'))

def inmysql(mysql_uri, tablename, *filenames ) :
    #共三个以上参数,
    # 第一个参数为mysql的连接字符串, 第二个为存储的表名,后面的参数都为需要读取的csv的文件名
    count= 0
    csvfile = ''
    #用sqlalchemy创建引擎
    engine = create_engine(mysql_uri)

    #如果第三个参数列表 则直接使用列表遍历
    if type(filenames[0]) != type('a'):
        filenames = filenames[0]
    #读取csv文件为 DataFream个数数据
    for csvfile in filenames :
        #遍历filenames 列表 ,读取filename的csv文件为dataFream格式数据,并添加到mrdatas列表中
        mrdata = pd.read_csv(csvfile)
        #替换列名中使用正则表达式替换 reReplace.sub('_', x)         r'[\.\\\(\)/]'
        mrdata.rename(columns=lambda x: reReplace.sub('_', x), inplace=True)
        #写入mysql数据库 表，
        if pd.io.sql.to_sql(mrdata,tablename,con=engine,if_exists='append') :
            count += 1
    return count
    # #存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么
    # mrdata.to_sql(tablename,engine,if_exists='append')

if __name__ == '__main__' :
    inmysql(mysql_uri, tablename, filename)