import json
import time
import random
from multiprocessing import Process,Lock

def check_ticket(i):
    with open('ticket') as f:
        ticket_count  = json.load(f)
    print('person%s查询当前余票 ：'%i,ticket_count['count'])

def buy_ticket(i,lock):
    check_ticket(i)
    lock.acquire()
    with open('ticket') as f:
        ticket_count = json.load(f)
    time.sleep(random.random())
    if ticket_count['count'] > 0:
        print('person%s购票成功'%i)
        ticket_count['count'] -= 1
    else:
        print('余票不足，person%s购票失败'%i)
    time.sleep(random.random())
    with open('ticket','w') as f:
        json.dump(ticket_count,f)

    
if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        Process(target=buy_ticket,args=[i,lock]).start()







