class Animal:
    role = 'Animal'

    def __init__(self, name, hp, ad):
        self.name = name  # 对象属性 属性
        self.hp = hp  # 血量
        self.ad = ad  # 攻击力
        self.r = self.role


class Person(Animal):
    role = 'Person'


# 继承中的init
alex = Person('alex',10,5)
print(Person.__dict__)   # role
print(Person.role)
print(alex.__dict__)
print(alex.role)



# --------------------------------------------
# class A:
#     def f1(self):
#         print('in A')
# class Foo(A):
#     def f1(self):
#         print('in Foo')
#         super().f1()
# class Bar(A):
#     def f1(self):
#         print('in Bar')
#         # super().f1()
# class Info(Foo,Bar):
#     def f1(self):
#         print('in Info f1')
#         super().f1()
# obj = Info()
# obj.f1()
