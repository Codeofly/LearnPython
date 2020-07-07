import logging
# log 日志
# 管理员
# 服务器上做操作
# 消费记录
# 淘宝

# 日志
# 给我们在内部操作的时候提供很多遍历
# 给用户提供更多的信息
# 在程序使用的过程中自己调试需要看的信息
# 帮助程序员排查程序的问题

# logging模块 不会自动帮你添加日志的内容
# 你自己想打印什么 你就写什么

# logging
    # 简单配置
    # 配置logger对象

# 简单配置
import logging
# 默认情况下 只显示 警告 及警告级别以上信息
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %y %H:%M:%S',
#                     filename = 'userinfo.log'
#                     )
# logging.debug('debug message')       # debug 调试模式 级别最低
# logging.info('info message')         # info  显示正常信息
# logging.warning('warning message')   # warning 显示警告信息
# logging.error('error message')       # error 显示错误信息
# logging.critical('critical message') # critical 显示严重错误信息

# 编码格式不能设置
# 不能同时输出到文件 和 屏幕

# 配置logger对象
import logging
logger = logging.getLogger()  # 实例化了一个logger对象

fh = logging.FileHandler('test.log',encoding='utf-8')    # 实例化了一个文件句柄
sh = logging.StreamHandler()

fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fmt)   # 格式和文件句柄或者屏幕句柄关联
sh.setFormatter(fmt)
sh.setLevel(logging.WARNING)

# 吸星大法
logger.addHandler(fh)  # 和logger关联的只有句柄
logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

logger.debug('debug message')       # debug 调试模式 级别最低
logger.info('info message')         # info  显示正常信息
logger.warning('warning message')   # warning 显示警告信息
logger.error('error message')       # error 显示错误信息
logger.critical('critical message')


# logging
# logging 是记录日志的模块
# 它不能自己打印内容 只能根据程序员写的代码来完成功能
# logging模块提供5中日志级别，从低到高一次：debug info warning error critical
# 默认从warning模式开始显示
# 只显示一些基础信息，我们还可以对显示的格式做一些配置

# 简单配置 配置格式 basicCondfig
# 问题：编码问题，不能同时输出到文件和屏幕

# logger对象配置
# 高可定制化
# 首先创造logger对象
# 创造文件句柄 屏幕句柄
# 创造格式
# 使用文件句柄和屏幕句柄 绑定格式
# logger对象和句柄关联
# logger.setLevel
# 使用的时候 logger.debug










