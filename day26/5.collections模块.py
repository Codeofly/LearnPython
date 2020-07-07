from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p)        #Point(x=1, y=2)
print(p.x)      #1
print(p.y)      #2

# from collections import deque
# 双端队列
# dq = deque()
# dq.append(1)
# dq.append(2)
# dq.append(3)
# print(dq)
# print(dq.pop())
# print(dq.popleft())
# dq.appendleft(4)
# dq.appendleft(5)
# print(dq)

import queue
# 队列   先进先出 fifo
# 计算机数据结构模型
# 先进先出

# 栈    先进后出
# 计算机数据结构模型
# 先进先出

# dic = {'k1':'v1','k2':'v1','k3':'v1','k4':'v1'}
# keys = list(dic.keys())
# print(keys)
# for k in keys:
#     print(k,dic[k])

from collections import OrderedDict
# dic = dict([('k1','v1'),('k2','v2')])
# print(dic)

dic = OrderedDict([('k1','v1'),('k2','v2')])
print(dic)