# 内置函数
# isinstance()    对象 类
# issubclass()    子类 父类

# 反射 ：使用字符串数据类型的变量名来使用变量
    # 文件中存储的都是字符串
    # 网络上能传递的也最接近字符串
    # 用户输入的
# wwwh
# what where why how
# a.b
# hasattr(a,'b')
# getattr()
# setattr()
# delattr()
# 类调用静态属性
# 对象调用属性 和 方法
# 模块调用模块中的名字
# 调用自己模块中的名字
# import sys
# a = 1
# a
# getattr(sys.modules['__main__'],'a')
# def func():pass
# func
# getattr(sys.modules['__main__'],'func')
# getattr(sys.modules['__main__'],'func')()
# class Teacher():
#     role = 'Person'
#     def wahaha(self):pass
#
#     @classmethod
#     def ADCa(cls):
#         cls.role
#
#     @staticmethod
#     def qqxing():
#         pass

# alex = Teacher()
# alex.wahaha()

# Teacher类 wahaha方法的连续反射
# alex = getattr(sys.modules['__main__'],'Teacher')()
# getattr(alex,'wahaha')()
# Teacher.wahaha()

# staticmethod 类反射类中的静态方法
# Teacher = getattr(sys.modules['__main__'],'Teacher')
# getattr(Teacher,'qqxing')()

# 找对象
# 'alex'
# alex = getattr(sys.modules['__main__'],'alex')

# 内置方法
# __len__   len(obj)
# obj对应的类中含有__len__方法，len(obj)才能正常执行

# __hash__  hash(obj)   是object类自带的
# 只有实现了 __hash__方法，hash(obj)才能正常执行

# print(hash('str'))
# print(hash('str'))
# print(hash('str'))
# print(hash('str'))

#1499850323766830849

# 可hash
# 不可hash就可变