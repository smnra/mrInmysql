#!/usr/bin/env python
# coding = utf-8

import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine
import re, os


filename = r'H:\BaiduYunDownload\testw文件\20170702-1_csv_tar_gzip\Baoji-cell-2017-07-02.csv'
mysql_uri = 'mysql+pymysql://root:10300@192.168.3.74:50014/temp?charset=utf8'
tablename = 'mr_cell'
#写入数据库时的数据类型
datatype = {
    'city': sqlalchemy.String(32),
    'IMEI': sqlalchemy.String(32),
    'IMSI': sqlalchemy.String(32),
    'time': sqlalchemy.String(32),
    'gps_Lon': sqlalchemy.String(32),
    'gps_Lat': sqlalchemy.String(32),
    'cell_Connected': sqlalchemy.String(32),
    'cell_m': sqlalchemy.String(32),
    'cell_networktype': sqlalchemy.String(32),
    'cell_cell_type': sqlalchemy.String(32),
    'cell_mnc': sqlalchemy.String(32),
    'cell_tac_cid_sid_': sqlalchemy.String(32),
    'cell_pci_lac_nid_': sqlalchemy.String(32),
    'cell_sinr_dbm_':sqlalchemy.String(32),
    'cell_rsrp_bid_': sqlalchemy.String(32)
}


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
        if not os.path.exists(csvfile) :
            #如果路径不存在 则打印'Path Is Not Exist!' 函数返回 -1
            print('File Does Not Exist!')
            return -1
        else :
            #从csv文件名中提取城市名
            city = os.path.split(csvfile)[1].split('-')[0]
        #遍历filenames 列表 ,读取filename的csv文件为dataFream格式数据,并添加到mrdatas列表中
        #index_col = False 参数为不使用(读取)索引
        mrdata = pd.read_csv(csvfile,low_memory = False, index_col = False )

        #替换列名中使用正则表达式替换 reReplace.sub('_', x)         r'[\.\\\(\)/]'
        mrdata.rename(columns=lambda x: reReplace.sub('_', x), inplace=True)

        del mrdata['battery']
        del mrdata['speed_in']
        del mrdata['speed_out']
        del mrdata['ping_163']
        del mrdata['ping_baidu']
        del mrdata['ping_sina']
        del mrdata['ping_taobao']
        del mrdata['ping_qq']
        del mrdata['ping_youku']
        del mrdata['ping_iqiyi']
        del mrdata['ping_sohutv']
        del mrdata['ping_qqtv']
        del mrdata['ping_baiduv']
        del mrdata['ping_letv']
        del mrdata['ping_tudou']
        mrdata.insert(0,'city',city)



        #写入mysql数据库 表， 第一个参数 为原始数据,第二个参数为写入表的名称,
        # 第4个if_exists为如果表存在则追加,第6个dtype为各个字段的数据类型 第5个index 参数为是否添加索引列
        pd.io.sql.to_sql(mrdata,tablename,con=engine,if_exists='append', index = True, dtype = datatype )
        count += 1
    return count
    # #存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么
    # mrdata.to_sql(tablename,engine,if_exists='append')

if __name__ == '__main__' :
    inmysql(mysql_uri, tablename, filename)