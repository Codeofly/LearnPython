
# 配置文件
# 开发 测试
# 给实施(运维)部分
    # 程序的稳定
# import configparser
# config = configparser.ConfigParser()
# config["DEFAULT"] = {'a': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes'
#                      }
#
# config['bitbucket.org'] = {'User':'hg'}
# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
# with open('example.ini', 'w') as f:
#    config.write(f)

# import configparser
# config = configparser.ConfigParser()
# config.read('example.ini')
# print(config.sections())        #  查看所有的节 但是默认不显示DEFAULT []
# print('bitbucket.org' in config) # True  验证某个节是否在文件中
# print('bytebong.com' in config) # False
# print(config['bitbucket.org']["user"])  # hg 查看某节下面的某个配置项的值
# print(config['DEFAULT']['Compression']) #yes
# print(config['topsecret.server.com']['ForwardX11'])  #no
# print(config['bitbucket.org'])          #<Section: bitbucket.org>
# for key in config['bitbucket.org']:     # 注意,有default会默认default的键
#     print(key)
# print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
# print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
# print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value

import configparser

config = configparser.ConfigParser()
config.read('example.ini')
config.add_section('yuan')
config.remove_section('bitbucket.org')
config.remove_option('topsecret.server.com',"forwardx11")
config.set('topsecret.server.com','k1','11111')
config.set('yuan','k2','22222')
config.write(open('new2.ini', "w"))


# section  可以直接操作它的对象来获取所有的节信息
# option  可以通过找到的节来查看多有的项

