# 爬取页面的例子
from gevent import monkey;monkey.patch_all()
from urllib.request import urlopen
import gevent
import time

def get_page(url):
    res = urlopen(url)
    print(len(res.read()))

url_lst = [
    'http://www.baidu.com',
    'http://www.sogou.com',
    'http://www.sohu.com',
    'http://www.qq.com',
    'http://www.cnblogs.com',
]
start = time.time()
gevent.joinall([gevent.spawn(get_page,url) for url in url_lst])
print(time.time() - start)
start = time.time()
gevent.joinall([gevent.spawn(get_page,url) for url in url_lst])
print(time.time() - start)
start = time.time()
for url in url_lst:get_page(url)
print(time.time() - start)














