# # 多继承
# class A:
#     def func(self):
#         print('A')
# class B(A):
#     pass
#     def func(self):
#         print('B')
# class C(A):
#     pass
#     def func(self):
#         print('C')
# class D(B):
#     pass
#     # def func(self):
#     #     print('D')
# class E(B,C):
#     pass
#     def func(self):
#         print('E')
# class F(D,E):
#     pass
#     # def func(self):
#     #     print('F')
# f = F()
# f.func()
# print(F.mro())  # 广度优先的遍历顺序

# 新式类 多继承 寻找名字的顺序 遵循广度优先
# class A:
#     def func(self):
#         print('A')
# class B(A):
#     def func(self):
#         super().func()
#         print('B')
# class C(A):
#     def func(self):
#         super().func()
#         print('C')
# class D(B,C):
#     def func(self):
#         super().func()   # B
#         print('D')
#
# d = D()
# d.func()

# super():
    # 在单继承中就是单纯的寻找父类
    # 在多继承中就是根据子节点 所在图 的 mro顺序找寻下一个类
# 遇到多继承和super
    # 对象.方法
        # 找到这个对象对应的类
        # 将这个类的所有父类都找到画成一个图
        # 根据图写出广度优先的顺序
        # 再看代码，看代码的时候要根据广度优先顺序图来找对应的super
