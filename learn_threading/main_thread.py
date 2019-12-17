# import multiprocessing as mp
#
# def job(a,b):
#     print('abc')
# if __name__=='__main__':
#     p1=mp.Process(target=job,args=(1,2))
#     p1.start()
#     p1.join()

import multiprocessing
import time


def hello(num):
    i = 0
    while i < num:
        i += 1
    print(i)


def test():
    ts = time.time()
    i = 3
    while i >= 1:
        p = multiprocessing.Process(target=hello, args=(20000000,))  # target=需调用函数名，args=函数参数
        p.start()  # 启动进程
        i -= 1
    p.join()
    te = time.time()
    print("using time: " + str(te - ts) + "s")


def test_a():
    time.sleep(10)


def test_pool():
    p = multiprocessing.Pool(processes=5)

    for i in range(10):
        p.apply_async(test_a)

    p.close()
    p.join()


if __name__ == '__main__':
    test_pool()
