from greenlet import greenlet
# 不是创造协程的模块
# 在协程这个模块中用来做多个协程任务的切换问题的
# 它到底是怎样实现切换的呢？
# import time
# def func1():
#     print(123)
#     g2.switch()
#     time.sleep(1)
#     print('abc')
#
# def func2():
#     time.sleep(1)
#     print(456)
#     g1.switch()
# g1 = greenlet(func1)   # 实例化
# g2 = greenlet(func2)   # 实例化
# g1.switch() # 开始运行

