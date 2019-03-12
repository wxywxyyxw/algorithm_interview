import _thread
import time
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)



# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


def test_redis(threadName, flag):
    # if r.get(flag) and int(r.get(flag)) > 0:
    #    print ('wait')
    # else:
    #    r.incr(flag,amount=1)
    #    print ('begin mission %s',  r.get(flag) )
    #    time.sleep(3)
    #    print ('end mission')
    #    r.set(flag,0)
    lock = None
    while lock != 1:
        lock = r.setnx(flag, 10)
        if lock == 1:
            print("get lock %s", threadName)
            print('begin mission')
            time.sleep(3)
            print('end mission')
            r.delete(flag)
            print("release lock %s", threadName)
        else:
            print('wait')
            time.sleep(0.5)


def test():
    # 创建两个线程
    try:
        _thread.start_new_thread(test_redis, ("Thread-1", "Thread-1",))
        # time.sleep(0.5)
        _thread.start_new_thread(test_redis, ("Thread-2", "Thread-1",))
    except:
        print("Error: 无法启动线程")
    time.sleep(30)


if __name__ == "__main__":
    test()
