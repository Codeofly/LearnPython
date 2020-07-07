# 管道
# from multiprocessing import Pipe
# left,right = Pipe()
# left.send('1234')
# print(right.recv())
# left.send('1234')
# print(right.recv())

from multiprocessing import Process, Pipe

def f(parent_conn,child_conn):
    parent_conn.close() #不写close将不会引发EOFError
    while True:
        try:
            print(child_conn.recv())
        except EOFError:
            child_conn.close()
            break

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(parent_conn,child_conn,))
    p.start()
    child_conn.close()
    parent_conn.send('hello')
    parent_conn.send('hello')
    parent_conn.send('hello')
    parent_conn.close()
    p.join()