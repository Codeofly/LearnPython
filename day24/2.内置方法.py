# str
# repr
# print(repr('1'))
# print(repr(1))
# print(str(1))
# print(str('1'))

# l = [1,2,3,4]
# print(l)   # 向文件中写   print替你将数据类型转化成字符串打印出来

# class List:
#     def __init__(self,*args):
#         self.l = list(args)
#     def __str__(self):
#         return '[%s]'%(','.join([str(i) for i in self.l]))
# l = List(1,2,3,4,5)
# print(l)   #--> l.__str__()   # object类中的__str__就是返回一个数据的内存地址
# print(l)
# print(str(l))
# print('%s'%l)
# print(obj)   的结果 是 obj.__str__()的结果
# str(obj)   的结果 也是 obj.__str__()的结果
# '%s'%obj   的结果 也是 obj.__str__()的结果


# class Teacher:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return "Teacher's object %s"%self.name
#     def __repr__(self):
#         return 'repr function %s'%self.name
# a = Teacher('alex',80)
# b = Teacher('egon',80)
# print(a)
# print(b)
# def repr(obj):
#     return obj.__repr__()

# print(repr(a))   # 函数  打印repr的返回值
# print(a.__repr__())
# print('%r'%a)
# print(str(a))   # 函数 打印str函数的返回值

# repr(obj)的结果和obj.__repr__()是一样的
# '%r'%(obj)的结果和obj.__repr__()是一样的

# repr(a)
# print(a)

# repr(1)
# repr('1')
# 因为 class int
# 和class str
#  中的__repr__方法不一样
# class int:
#     def __repr__(self):
#         return str(1)

# class str2:
#     def __repr__(self):
#         return "'%s'"%str(1)

# a = int()
# b = str2()
# print(repr(a))
# print(repr(b))


# class Teacher:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return "Teacher's object %s"%self.name
    # def __repr__(self):
    #     return 'repr function %s'%self.name
# a = Teacher('alex',80)
# b = Teacher('egon',80)
# print(a)
# print(repr(a))
# 当需要使用__str__的场景时找不到 __str__就找__repr__
# 当需要使用__repr__的场景时找不到__repr__的时候就找父类的repr
# 双下repr是双下str的备胎

# len   __len__
# print(l)   l.__str__
# 010100101   ---> 代码
# class A:
#     pass
# A()   #->


# def func(cal):
#     return 1
#
# ret = func('1+2*3-5/5')

# class A:
#     def __init__(self):pass
#     def __len__(self):pass
# def len(obj):
#     obj.__len__()
# a = A()
# a.__len__()
# len()   # 为什么要归一化设计呢？
# 更接近面向函数编程

# str()
# print()
# %s

# len()  obj.__len__()  返回值是一致的
# len() 的结果是依赖 obj.__len__()
# hash() 的结果是依赖 obj.__hash__()

# str() 的结果是依赖 obj.__str__()
# print(obj) 的结果是依赖 obj.__str__()
# %s 的结果是依赖 obj.__str__()    # 语法糖
#
# repr() 的结果是依赖 obj.__repr__()
# %r 的结果是依赖 obj.__repr__()

# repr是str的备胎

# __str__
# __repr__   一定是选择repr

# 核心编程 第2版
# 核心编程 第3版
# 流畅的python
# 数据结构与算法  python 机械工业出版社

# object.__repr__()
# '%r' # __repr__()
# int.__repr__()
# str.__repr__()

# class Teacher:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# @wrapper    func = wrapper(func)
# 语法糖   -->

# a==b
# 1>2
# 1+2

# format()
# __format__
# class A:
#     def __init__(self,name,school,addr):
#         self.name = name
#         self.school = school
#         self.addr = addr
#     def __format__(self,format_spec):
#         return format_spec.format(obj=self)


# a = A('大表哥','oldboy','沙河')
# format_spec = '{obj.name}-{obj.addr}-{obj.school}'
# print(format(a,format_spec))


# print('{0}-{1}'.format('a','b'))

# format_dict={
#     'nat':'{obj.name}-{obj.addr}-{obj.type}',#学校名-学校地址-学校类型
#     'tna':'{obj.type}:{obj.name}:{obj.addr}',#学校类型:学校名:学校地址
#     'tan':'{obj.type}/{obj.addr}/{obj.name}',#学校类型/学校地址/学校名
# }
# class School:
#     def __init__(self,name,addr,type):
#         self.name=name
#         self.addr=addr
#         self.type=type
#
#     def __format__(self, format_spec):   #format_spec = 'nat'
#         if not format_spec or format_spec not in format_dict:
#             format_spec='nat'
#         fmt=format_dict[format_spec]     #'{obj.name}-{obj.addr}-{obj.type}'
#         return fmt.format(obj=self)     #'{obj.name}-{obj.addr}-{obj.type}'.format(obj=self)
#
# s1=School('oldboy1','北京','私立')
# print(format(s1,'nat'))  #s1.__format__('nat')
# print(format(s1,'tna'))
# print(format(s1,'tan'))
# print(format(s1,'asfdasdffd'))


# if True:print('执行if中的代码')
# if False:print('不执行if中的代码')
#
# if True or False:print('or两端的条件有一个为True就执行这个if中的代码')
# if not True or False:pass
# if not False or False:pass
# if not format_spec or format_spec not in format_dict
# 0  [] '' {} () None