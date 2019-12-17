import multiprocessing as mp
import os
from time import sleep

def worker(msg):
    print(os.getpid())
    sleep(2)
    print(msg)
    return msg

def main_func():
    #创建进程池对象
    p = mp.Pool(processes = 4) #创建4条进程

    pool_result = []
    for i in range(10):
        msg = 'hello-%d'%i
        r = p.apply_async(worker,(msg,)) #向进程池中添加事件
        pool_result.append(r)

    #获取事件函数的返回值
    for r in pool_result:
        print('return:',r)

    p.close()#关闭进程池,不再接受请求
    p.join()# 等待进程池中的事件执行完毕，回收进程池

if __name__ ==  '__main__':
    main_func()


