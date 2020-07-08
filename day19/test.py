class A:
    def f1(self):
        print('in A')
class Foo(A):
    def f1(self):
        print('in Foo')
        super().f1()
class Bar(A):
    def f1(self):
        print('in Bar')
        # super().f1()
class Info(Foo,Bar):
    def f1(self):
        print('in Info f1')
        super().f1()
obj = Info()
obj.f1()


