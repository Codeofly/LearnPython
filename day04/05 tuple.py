tu = (1,2,'al')
print(tu[:2])
print(tu[2])
for i in tu:
    print(i)
#儿子不能改，孙子可能改
tu1 = (1,2,'al',[1,'tai'],(1,2,3))
tu1[3].append('日天')
print(tu1)
#count len index
li = [1,(1,2,3)]
