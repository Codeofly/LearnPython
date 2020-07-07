# 圆
# 计算圆的周长 2 pi r
# 计算圆的面积 pi r**2
# 5个圆
# 1,3,5,7,9
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
    def cal_area(self):
        '''
        计算圆面积的方法
        :return:返回值是float数据类型的面积
        '''
        return pi*self.r**2
    def cal_perimeter(self):
        '''
        计算圆周长的方法
        :return:返回值是float数据类型的周长
        '''
        return pi * self.r * 2
for i in range(1,10,2):
    c1 = Circle(i)
    print(c1.cal_area())
    print(c1.cal_perimeter())
# 类 属性 和 方法
    # 半径
    # 计算面积 计算周长
# 程序的解耦
    # 当计算的规模足够大的时候 我们应该在编码的过程当中让操作尽量原子化
    # 尽量用返回值来代替print

# 面向对象的基础

# 用面向对象的思想
# 1.博客上的练一练
# 2.计算圆环的面积和周长
# 3.默写 交互
# 4.校园管理系统第一步
