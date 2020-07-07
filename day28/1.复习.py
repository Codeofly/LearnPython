# 复习
#     collections
        # 增加了一些扩展数据类型 ：namedtuple orderdict defaltdict
#     队列和栈
#     time 时间
#         三种格式 ： 时间戳  结构化 字符串
#     random
#         随机数 打乱顺序
#     sys
#          和python解释器交互的：
            # path 导入模块的时候 从这个路径中获取
            # argv 以脚本的形式执行一个文件的时候，可以加一些参数

            # import sys
            # print(sys.argv)  #['xx.py','alex','sb']
# 作业
# 求时间差
# 作业1
# y-m-d h:M:S
# 从当前时间开始
import time
比起y-m-d h:M:S过去了多少年 多少月 多少天 多少h，多少m，多少s
当前的时间 时间戳
过去的时间 转成时间戳
时间戳相减
相减之后的结果转成结构化时间
结构化时间 - 1970.1.1 0:0:0
def cal_time(fmt_time,fmt):
    now = time.time()
    time_before = time.mktime(time.strptime(fmt_time,fmt))
    sub_time = now - time_before
    struct_time = time.gmtime(sub_time)
    return '过去了%d年%d月%d天%d小时%d分钟%d秒' % \
    (struct_time.tm_year - 1970, struct_time.tm_mon - 1,
                                       struct_time.tm_mday - 1, struct_time.tm_hour,
                                       struct_time.tm_min, struct_time.tm_sec)

ret = cal_time('2018-4-23 10:30:20','%Y-%m-%d %H:%M:%S')  #过去了0年0月2天0小时38分钟35秒
print(ret)

# 要求 生成随机验证码
# 基础需求： 6位数字验证码 数字可以重复
# 进阶需求： 字母+数字 4位验证码 数字字母都可以重复
import random
# def id_code(num):
#     ret = ''
#     for i in range(num):
#         n = random.randint(0,9)
#         ret += str(n)
#     return ret
# print(id_code(6))

# def id_code(num):   # num 大写字母 小写字母在每一位被取到的概率相同
#     ret = ''
#     for i in range(num):
#         number = str(random.randint(0,9))
#         alph_num = random.randint(97,122)   # A65 a97 +25
#         alph_num2 = random.randint(65,90)   # A65 a97 +25
#         alph = chr(alph_num)
#         alph2 = chr(alph_num2)
#         choice = random.choice([number,alph,alph2])
#         ret += choice
#     return ret
# print(id_code(6))

# def id_code(num):  # num 字母在每一位被取到的概率相同
#     ret = ''
#     for i in range(num):
#         number = str(random.randint(0,9))
#         alph_num = random.randint(97,122)   # A65 a97 +25
#         alph_num2 = random.randint(65,90)   # A65 a97 +25
#         alph = chr(alph_num)
#         alph2 = chr(alph_num2)
#         choice = random.choice([alph,alph2])
#         choice = random.choice([number,choice])
#         ret += choice
#     return ret
# print(id_code(6))

# os模块

# 面向对象的进阶

# 3.模块

# 包
