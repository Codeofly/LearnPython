# 包就是py模块的集合
# 自带__init__.py文件
    # py2 包中必须有一个__init__.py文件
    # py3
# 能不能导入一个包：要看sys.path中的路径下有没有这个包
# 从包中导入模块： 把包与包之间的关系写清楚，精确到模块，就一定能导入
# 直接导入一个包，并不会导入包下的模块，而是执行这个包下的__init__.py文件
# 如果对导入还有更高的要求
    # 可以对包中的__init__.py文件做定义
    # 绝对路径导入的方式
    # 相对路径导入的方式 使用相对路径导入的模块不能作为脚本执行


from new_pec2 import glance