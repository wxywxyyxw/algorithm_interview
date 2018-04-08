# -*- coding: utf-8 -*-
from threading import Thread, current_thread

import time
import gevent

"""
理解join，简单的说就是
"""
def compare_threads():
    #多线程比单线程慢的例子
    def counter():
        i = 0
        for _ in xrange(5):
            i += 1
        print('finish {name}'.format(name=current_thread().name))
        return True

    def main():
        start_time = time.time()

        # 2个线程顺序执行counter函数，一个开始后就阻塞主程序，直到这个线程结束，才运行下一次for循环
        for tid in range(2):
            t = Thread(target=counter)
            t.start() # 线程开始
            print('i am block')
            t.join()  # 阻塞自己，等待线程完成

        end_time = time.time()
        print "total time of single is: {}".format(end_time - start_time)

    def multi_main():
        thread_all = []
        start_time = time.time()
        for tid in range(2):
            t = Thread(target=counter)
            t.start() # 线程开始
            thread_all.append(t)

        # 2个线程并行执行counter函数
        for i in range(2):
            end_time = time.time()
            print ('i: {i} {times}'.format(i=i,times=end_time -start_time))
            thread_all[i].join()
            end_time = time.time()
            print ('after i: {i} {times}'.format(i=i,times=end_time -start_time))

        end_time = time.time()
        print "total time of multi is: {}".format(end_time -start_time)

    def single():
        start_time = time.time()
        counter()
        counter()
        end_time = time.time()
        print "one time of single is: {}".format(end_time - start_time)
        #current_thread().join() 这条语句会报错


   # main()
    print('------------------------')
    #multi_main()
    print('------------------------')
    single()

    """
    total time of single is: 3.72316193581
    total time of multi is: 5.38856887817
    one time of single is: 1.78377985954
    """



if __name__ == '__main__':
    compare_threads()
