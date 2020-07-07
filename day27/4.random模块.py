import random
# 随机 打乱顺序有关的

# print(random.random())   # 0-1随机小数
# print(random.uniform(1,4))

# print(random.randint(1,1000))    # 包含1,2
# print(random.randrange(1,2))     # 不包含2
# print(random.randrange(1,20,2))  # 包含所有奇数

# print(random.choice([1,'23',[4,5]]))

# print(random.sample([1,'23',[4,5]],2))

# item=[1,3,5,7,9]
# import random
# random.shuffle(item)
# print(item)
'''
# 要求 生成随机验证码
# 基础需求： 6位数字验证码 数字可以重复
# 进阶需求： 字母+数字 4位验证码 数字字母都可以重复
'''

# st = random.sample('QWERTYUIOPASDFGHJKLZXCVBNM123456789',6)
# s = ''
# for i in st:
#     s += str(i)
# print(s)
# ret = input('请输入验证码 :').upper()
# print('验证成功' if s == ret else '验证失败')
