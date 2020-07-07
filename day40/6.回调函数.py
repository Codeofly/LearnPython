import os
from urllib.request import urlopen
from multiprocessing import Pool
def get_url(url):
    print('-->',url,os.getpid())
    ret = urlopen(url)
    content = ret.read().decode('utf-8')
    print(content)
    return url

def call(url):
    # 分析
    print(url,os.getpid())

if __name__ == '__main__':
    print(os.getpid())
    l = [
        'http://www.baidu.com',  # 5
        'http://www.sina.com',
        'http://www.sohu.com',
        'http://www.sogou.com',
        'http://www.qq.com',
        'http://www.bilibili.com',  #0.1
    ]
    p = Pool(5)   # count(cpu)+1
    ret_l = []
    for url in l:
        ret = p.apply_async(func = get_url,args=[url,],callback=call)
        ret_l.append(ret)
    for ret in ret_l : ret.get()


# 回调函数
# 在进程池中，起了一个任务，这个任务对应的函数在执行完毕之后
# 的返回值会自动作为参数返回给回调函数
# 回调函数就根据返回值再进行相应的处理

# 回调函数 是在主进程执行的








