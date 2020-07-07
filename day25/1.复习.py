# 反射 必须会 必须能看懂 必须知道在哪儿用
    # hasattr getattr setattr delattr
# 内置方法 必须能看懂 能用尽量用
# __len__ len(obj)的结果依赖于obj.__len__()的结果，计算对象的长度
# __hash__ hash(obj)的结果依赖于obj.__hash__()的结果，计算对象的hash值
# __eq__  obj1 == obj2 的结果依赖于obj.__eq__()的结果,用来判断值相等
# __str__ str(obj) print(obj) '%s'%obj 的结果依赖于__str__,用来做输出、显示
# __repr__ repr(obj) '%r'%obj的结果依赖于__repr__,还可以做str的备胎
# __format__ format() 的结果依赖于__format__的结果，是对象格式化的
# __call__ obj()相当于调用__call__，实现了__call__的对象是callable的
# __new__  构造方法，在执行__init__之前执行，负责创建一个对象，在单例模式中有具体的应用
# __del__  析构方法，在对象删除的时候，删除这个对象之前执行，主要用来关闭在对象中打开的系统的资源

# class A:
#     def __getitem__(self, item):
#         print(item)
# a = A()
# a['bbb']    # 对象['值'] 触发了__getitem__
# __getitem__ 对象[]的形式对对象进行增删改查
# __setitem__
# __delitem__
# __delattr__   del obj.attr 用来自定义删除一个属性的方法

# 只有一个对象   只开了一个内存空间
# 创建一个类 单例模式中的对象属性编程类中的静态属性，所有的方法变成类方法
# 设计模式 —— java
# python中的单例模式 是使用__new__


# python
# 显示一个对象中的所有以a开头的属性 wahaha(obj)   obj.__wahaha__()
# obj.age