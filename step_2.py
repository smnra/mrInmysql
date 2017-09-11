from inmysql import *
from  getfiles import *
import sys,traceback





filelist = getGzipList(r'H:\BaiduYunDownload\7月份数据' ,'.csv')

for file in filelist :
    if os.path.exists(file) :
        try:
            inmysql(mysql_uri, tablename, file)
        except:
            traceback.print_exception(*sys.exc_info())
    print(file + ' is in mysql complated!')
