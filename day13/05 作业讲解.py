# 1.
# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2), (‘草花’，2), …(‘黑桃’，‘A’)]


# def func(li):
#     l = []
#     for i in li:
#         for j in range(1,14):
#             l.append((i,j))
#     return l
# print(func(['草花', '黑桃', '红桃', '方片']))

# 2.
# 写函数，传入n个数，返回字典
# {‘max’:最大值,’min’:最小值}
# 例如: min_max(2, 5, 7, 8, 4)
# 返回: {‘max’:8,’min’:2}
# max([1, 2, 3])  3
# min（[1, 2, 3]）

# def func2(*args):return {'max':max(args), 'min':min(args)}
# func2(1,2,3,4,5)

# 3.
# 写函数，专门计算图形的面积
# 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
# 调用函数area(‘圆形’, 圆半径)  返回圆的面积
# 调用函数area(‘正方形’, 边长)  返回正方形的面积
# 调用函数area(‘长方形’, 长，宽)  返回长方形的面积
#
#
# def area(*args):
#     if args[0] == '长方形':
#         def 计算长方形面积():
#             s = args[1]*args[2]
#             return s
#         return 计算长方形面积()
#     elif args[0] == '正方形':
    # def 计算正方形面积():
    #     pass
    #
    # def 计算圆形面积():
    #     pass
# print(area('长方形',2,3))
# area('正方形',5)
# area('圆形',6)





#


# 4.
# 写函数，传入一个参数n，返回n的阶乘
# 例如: cal(7)
# 计算7 * 6 * 5 * 4 * 3 * 2 * 1


# def func3(n):
#     count = 1
#     for i in range(n,0,-1):
#         count = count * i
#     return count
# print(func3(3))




# 5、编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果（升级题）
# 5.1.为题目3编写装饰器，实现缓存网页内容的功能：（升级题）
# 具体：实现下载的页面存放于文件中，如果网页有对应的缓存文件，就优先从文件中读取网页内容，否则，就去下载，然后存到文件中


# 6
# 给每个函数写一个记录日志的功能，
# 功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
# 所需模块：
# import time
# def wrapper(func):
#     def inner(*args, **kwargs):
#         struct_time = time.localtime()
#         time_now = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
#         with open('log', encoding='utf-8', mode='a') as f1:
#             f1.write('在%s是时间，执行了%s函数\n' % (time_now, func.__name__))
#         ret = func(*args, **kwargs)
#         '''函数执行之后操作'''
#         return ret
#     return inner
#
# @wrapper
# def func1():
#     time.sleep(1)
#     print(555)
# @wrapper
# def func2():
#     time.sleep(2)
#     print(666)
# c = input('选择函数')
# print(eval(c))








# 7、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次(三次机会)，后续的函数都无需再输入用户名和密码

# dic = {
#     'username':None,
#     'status':False,
# }
#
# def wrapper(func):
#     def inner(*args, **kwargs):
#         if dic['status']:
#             ret = func(*args, **kwargs)
#             return ret
#         else:
#             i = 0
#             while i < 3:
#                 username = input('请输入用户名:').strip()
#                 password = input('请输入密码:').strip()
#                 with open('register_msg',encoding='utf-8') as f1:
#                     for j in f1:
#                         j_li = j.strip().split()  # ['张三','123']
#                         if username == j_li[0] and password == j_li[1]:
#                             dic['username'] = username
#                             dic['status'] = True
#                             ret = func(*args, **kwargs)
#                             return ret
#                     else:
#                         print('账号或者密码错误，请重新输入%s机会' % (2-i))
#                         i += 1
#
#
#     return inner
#
#
# @wrapper
# def article():
#     print('文章')
#
# @wrapper
# def diary():
#     print('日记')
#
# @wrapper
# def comment():
#     print('评论')
#
# @wrapper
# def file():
#     print('文件')
# c = input('输入函数')
# y = eval(c)
# y()
#
# # article()
# # diary()
# # comment()
# # file()
#

# 8，在编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码。
# 这个作业之上进行升级操作：
# 设置两套密码，一套为微信账号密码，一套为qq账号密码保存在文件中。
# 设置四个函数，分别代表
# 京东首页，京东超市，淘宝首页，淘宝超市。
# 循环打印四个选项：东首页，京东超市，淘宝首页，淘宝超市。
# 供用户选择，用户输入选项后，执行该函数，四个函数都加上认证功能，只要登陆成功一次，在选择其他函数，后续都无需输入用户名和密码。
# 相关提示：用带参数的装饰器。装饰器内部加入判断，验证不同的账户密码。

dic = {
    'username':None,
    'status':False,
}


def login(flag):
    def wrapper(func):
        def inner(*args, **kwargs):
            if dic['status']:
                ret = func(*args, **kwargs)
                return ret
            else:
                i = 0
                while i < 3:
                    username = input('请输入用户名(用%s账号):' % flag).strip()
                    password = input('请输入密码:').strip()
                    with open('user_pwd',encoding='utf-8') as f1:
                        msg_dic = eval(f1.readline())
                        # {'微信': {'password': '123', 'username': '老男孩'}, 'qq': {'password': '123', 'username': '老男孩1'}}
                        if username == msg_dic[flag]['username'] and password == msg_dic[flag]['password']:
                            dic['username'] = username
                            dic['status'] = True
                            ret = func(*args, **kwargs)
                            return ret
                        else:
                            print('您输入的用户或者密码错误，请重新输入，还有%s次机会' % (2-i))
                            i += 1
        return inner
    return wrapper




@login('微信')
def taobao_home():
    print('淘宝首页')

@login('微信')
def taobao_shop():
    print('淘宝超市')

@login('qq')
def jingdong_home():
    print('京东首页')

@login('qq')
def jingdong_shop():
    print('京东超市')

choice_dict = {
    1: taobao_home,
    2: taobao_shop,
    3: jingdong_home,
    4: jingdong_shop,
}

while True:
    print('1 淘宝首页\n2 淘宝超市\n3 京东首页\n4 京东超市')
    choice_num = input('请选择输入的序号:').strip()
    if choice_num.isdigit():
        choice_num = int(choice_num)
        if 0 < choice_num <= len(choice_dict):
            choice_dict[choice_num]()
        else:
            print('请输入范围内的序号')
    else:
        print('您输入的有非法字符，请重新输入')