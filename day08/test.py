f = open('/Users/liyan/PycharmProjects/LearnPython/day08/01 昨日内容回顾',encoding='utf-8')
for i in f:
    print(i.split("\n")[0])
    # print(i)
f.close()