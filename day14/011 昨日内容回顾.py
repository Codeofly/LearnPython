def func1():
    print(111)
    yield 666
    yield 777
    yield 888
# g = func1()
# print(func1().__next__())
# print(func1().__next__())
# print(func1().__next__())
print(func1(),func1(),func1())