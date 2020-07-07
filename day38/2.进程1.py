import os
import time
print(os.getpid())  # 进程id
time.sleep(1000)
print(os.getpid())
# 4核 —— 4个进程
# 一个进程 —— cpu
# 多进程 —— 4个进程