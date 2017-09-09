from  getfiles import *
from unzip import *

filelist = getGzipList(r'H:\BaiduYunDownload\7月份数据' ,'.gz', '.gzip', '.tgz')

for filename in filelist :
    unzip(reStr, filename)