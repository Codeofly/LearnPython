# 8-9 深圳
# 8:30 - 10:30
# class B:pass
# class A(B):pass
# a = A()
# print(isinstance(a,A))
# print(isinstance(a,B))  # 能够检测到继承关系
# print(type(a) is A)
# print(type(a) is B)     # type只单纯的判断类
# 判断一个对象和一个类有没有血缘关系
# isinstance(a,A)

class B:pass
class C(B):pass
class D(C):pass
print(issubclass(C,D))
print(issubclass(D,C))
print(issubclass(B,C))
print(issubclass(C,B))
print(issubclass(D,B))
# issubclass(子类名,父类名) 如果返回True,说明有继承关系
#