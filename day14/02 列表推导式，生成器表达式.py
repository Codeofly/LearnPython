# li = []
# for i in range(1,101):
#     li.append(i)
# print(li)
#l1 = [python1期，python2期，python3期.....]
# l1 = []
# for i in range(1,12):
#     l1.append('python%s期' % i)
# print(l1)
#一行搞定，列表推导式：用列表推导式能够构建的任何列表，用别的都可以构建。
#一行，简单，感觉高端。但是，不易排错。
# li = [i for i in range(1,101)]
# print(li)
# l2 = ['python%s期' % i for i in range(1,12)]
# print(l2)
#循环模式
#[经过加工的i for i in 可迭代对象]

l_obj = ('python%s期' % i for i in range(1,12))
print(l_obj)
print(l_obj.__next__())
print(l_obj.__next__())
print(l_obj.__next__())

#列表推导式：一目了然，占内存。
#生成器表达式：不易看出，节省内容。

#循环模式
#[经过加工的i for i in 可迭代对象]
# l2 = [i*i for i in range(1,11)]
# print(l2)
#筛选模式
#[经过加工的i for i in 可迭代对象 if 条件 筛选]
# l3 = [i for i in range(1,101) if i % 3 == 0]
# print(l3)

# l3 = [i for i in range(31) if i % 3 == 0]
# print(l3)
#
# l3 = [i**2 for i in range(31) if i % 3 == 0]
# print(l3)

# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#
# l4 = [name for i in names for name in i if name.count('e') == 2]
# print(l4)

# mcase = {'a': 10, 'b': 34}
# mcase_frequency = {mcase[k]: k for k in mcase}
# print(mcase_frequency)

squared = list({x**2 for x in [1, -1, 2]})
print(squared)