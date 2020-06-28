dic = {"name_list":['张三','lisi','隔壁王叔叔'],
       'dic2':{'name':'太白','age':12},
       }
#1 ,给列表追加一个元素：'旺旺'
# l1 = dic['name_list']
# l1.append('旺旺')
dic['name_list'].append('旺旺')
print(dic)
#,2,给列表lisi全部大写
# print(dic['name_list'][1].upper())
dic['name_list'][1] = dic['name_list'][1].upper()
print(dic)
#3，给dic2 对应的字典添加一个键值对：hobby：girl.
dic['dic2']['hobby'] = 'girl'
print(dic)