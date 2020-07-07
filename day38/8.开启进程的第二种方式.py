import os
from multiprocessing import Process
class Myprocess(Process):
    def __init__(self,*args):
        super().__init__()
        self.args = args
    def run(self):
        print(os.getpid(),self.name,self.pid)
        for name in self.args:
            print('%s和女主播聊天'%name)

if __name__ == '__main__':
    print(os.getpid())
    p = Myprocess('yuan','wusir')
    p.start()   # 在执行start的时候，会帮我们主动执行run方法中的内容