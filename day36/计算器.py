import re
def cal(exp):
    if '*' in exp:
        a,b = exp.split('*')
        return str(float(a) * float(b))
    elif '/' in exp:
        a, b = exp.split('/')
        return str(float(a) / float(b))

def format(exp):
    exp = exp.replace('++',"+")
    exp = exp.replace('-+',"-")
    exp = exp.replace('+-',"-")
    exp = exp.replace('--',"+")
    return exp

def dealwith(no_bracket_exp):
    # 匹配乘除法
    while True:
        mul_div = re.search('\d+(\.?\d+)?[*/]-?\d+(\.?\d+)?', no_bracket_exp)
        if mul_div:
            exp = mul_div.group()
            result = cal(exp)
            no_bracket_exp = no_bracket_exp.replace(exp, result, 1)  # (-8)
        else:break
    no_bracket_exp = format(no_bracket_exp)
    # 计算加减法
    lst = re.findall(r'[-+]?\d+(?:\.\d+)?', no_bracket_exp)
    res = str(sum([float(i) for i in lst]))
    return res   # 返回一个计算完毕的字符串数据类型的 数字

def remove_bracket(s):
    s = s.replace(' ', '')     # 去掉空格
    while True:
        ret = re.search(r'\([^()]+\)', s)   # 匹配最内层的括号
        if ret:      # 能匹配到括号 就先处理括号内的加减乘除
            no_bracket_exp = ret.group()    # 拿到括号中的表达式
            ret = dealwith(no_bracket_exp)  # 把括号中的表达式交给的dealwith
            s = s.replace(no_bracket_exp, ret, 1)
        else:       # 不能匹配到括号 就字节处理加减乘除
            ret = dealwith(s)  # 把表达式交给的dealwith
            return ret

s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
print(remove_bracket(s))
