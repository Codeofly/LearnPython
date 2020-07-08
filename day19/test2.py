class G():
    def __init__(self):
        print("init g")

    def f1(self):
        print("g")

    def ff1(self):
        print("g")
class F(G):
    def __init__(self):
        print("init f")

    def ff1(self):
        print("f")
    def f1(self):
        print("f")
        super().f1()
class E(G):
    def __init__(self):
        print("init e")

    def ff1(self):
        print("e")
    def f1(self):
        print("e")
        super().f1()
class D():
    def __init__(self):
        print("init d")
    def f1(self):
        print("d")
        # super().f1()
class C():
    def __init__(self):
        print("init c")
    def f1(self):
        print("c")
        # super().f1()
class B(E,F):

    def f1(self):
        print("b")
        super().f1()
class A(B, C, D):

    def f1(self):
        print("f1 a")
        super().f1()
a = A()
# a.ff1()
# a.f1()
print(类名.__mro__)