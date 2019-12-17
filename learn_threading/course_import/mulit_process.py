# -*- coding: utf-8 -*-

import multiprocessing as mp
from gevent import monkey;monkey.patch_all(thread=False)
import os
from time import sleep
from learn_threading.course_import.courses import test_request,_get_request

#import logging

# logger = mp.get_logger()
# logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler('logs/{}.log'.format(os.getppid()))
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)

def worker(msg):
   # print()

    print(msg,os.getpid())
    sleep(2)
    # return msg
    test_request()
    #logger.info('{} get www.baidu.com'.format(os.getppid()))

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

    #logger.info('{} main'.format(os.getppid()))

if __name__ ==  '__main__':
    main_func()


