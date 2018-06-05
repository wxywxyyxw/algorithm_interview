# -*- coding: utf-8 -*-

# import tornado
# from tornado.httpclient import AsyncHTTPClient
# import time, sys
# from tornado import gen
#
#
# def http_callback_way(url1, url2):
#     http_client = AsyncHTTPClient()
#     begin = time.time()
#     count = [0]
#     def handle_result(response, url):
#         print('%s : handle_result with url %s' % (time.time(), url))
#         count[0] += 1
#         if count[0] == 2:
#             print ('http_callback_way cost', time.time() - begin)
#             sys.exit(0)
#
#     http_client.fetch(url1,lambda res, u = url1:handle_result(res, u))
#     print('%s here between to request' % time.time())
#     http_client.fetch(url2,lambda res, u = url2:handle_result(res, u))
#
#
#
# def test_call_back_learn():
#     url_list = [ 'http://xlambda.com/gevent-tutorial/','https://www.bing.com']
#     http_callback_way(*url_list)
#     tornado.ioloop.IOLoop.instance().start()
#
#
#
# def http_generator_way(url1, url2):
#     begin = time.time()
#     count = [0]
#     @gen.coroutine
#     def do_fetch(url):
#         http_client = AsyncHTTPClient()
#         response = yield http_client.fetch(url, raise_error = False)
#         print ( url, response.error)
#         count[0] += 1
#         if count[0] == 2:
#             print ('http_generator_way cost', time.time() - begin)
#             sys.exit(0)
#
#     do_fetch(url1)
#     do_fetch(url2)
#
#
# def test_generator_learn():
#     url_list = [ 'http://baidu.com/','https://www.bing.com']
#     http_generator_way(*url_list)
#     tornado.ioloop.IOLoop.instance().start()
from collections import namedtuple

def test_hello():
    import asyncio

    def hello_world(loop):
        print('Hello World')
        loop.stop()

    def hello_world2(loop):
        print('Hello World2')
        loop.stop()

    loop = asyncio.get_event_loop()

    # Schedule a call to hello_world()
    loop.call_soon(hello_world, loop)
    loop.call_soon(hello_world2, loop)

    # Blocking call interrupted by loop.stop()
    loop.run_forever()
    loop.close()


def test_yield():
    def consumer():  # 定义消费者，由于有yeild关键词，此消费者为一个生成器
        print("[Consumer] Init Consumer ......")
        r = "init ok"  # 初始化返回结果，并在启动消费者时，返回给生产者
        while True:
            n = yield r  # 消费者通过yield接收生产者的消息，同时返给其结果
            print("[Consumer] conusme n = %s, r = %s" % (n, r))
            r = "consume %s OK" % n  # 消费者消费结果，下个循环返回给生产者

    def produce(c):  # 定义生产者，此时的 c 为一个生成器
        print("[Producer] Init Producer ......")
        r = c.send(None)  # 启动消费者生成器，同时第一次接收返回结果
        print("[Producer] Start Consumer, return %s" % r)
        n = 0
        while n < 1:
            n += 1
            print("[Producer] While, Producing %s ......" % n)
            r = c.send(n)  # 向消费者发送消息并准备接收结果。此时会切换到消费者执行
            print("[Producer] Consumer return: %s" % r)
        c.close()  # 关闭消费者生成器
        print("[Producer] Close Producer ......")

    produce(consumer())

def test_basic_yield():
    def a():
        r = 5
        while True:
            b = yield r # 每次返回r，如果不使用send给b赋值，则 b = None
            print ("b is %s" % b)
            r = b

    gen = a()
    res = gen.send(None) #首次必须传入None
    print ("res is %s" % res)
    res = gen.send(1)
    print ("res is %s" % res)

    #res = gen.next() python2.7
    res = next(gen) # python 3  不向函数a中传值的话，默认传入None, 则 b = None
    print ("res is %s" % res)

    #res = gen.next()
    res = next(gen)
    print ("res is %s" % res)


def test_yield_return():
    """
    python3.3之后生成器中才可以使用return
    """


    Result = namedtuple('Result', 'count average')

    def averager():
        total = 0.0
        count = 0
        average = None
        while True:
            term = yield
            if term is None:
                break  # 为了返回值，协程必须正常终止；这里是退出条件
            total += term
            count += 1
            average = total/count
        # 返回一个namedtuple，包含count和average两个字段。在python3.3前，如果生成器返回值，会报错
        return Result(count, average)

    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(20)
    coro_avg.send(30)
    coro_avg.send(40)

    #coro_avg.send(None) # 发送None终止循环，导致协程结束。生成器对象会抛出StopIteration异常。异常对象的value属性保存着返回值。
    try:
         coro_avg.send(None)
    except StopIteration as exc:
        result = exc.value # 利用try except 来接收return的值
    print (result)

def  yield_from_simple_use():
    # def gen():
    #     for c in 'AB':
    #         yield c
    #     for i in range(1, 3):
    #         yield i

    #利用yield from 可以简化yield的写法
    def gen():
        yield from 'AB'
        yield from range(1, 3)
    print (list(gen()))

def yield_from_flatten():
    from collections import Iterable

    def flatten(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                yield from flatten(x) # 这里递归调用，如果x是可迭代对象，继续分解
            else:
                yield x

    items = [1, 2, [3, 4, [5, 6], 7], 8]

    # Produces 1 2 3 4 5 6 7 8
    for x in flatten(items):
        print(x)

    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)


def use_yield_complex():
    Result = namedtuple('Result', 'count average')

    # 子生成器
    # 这个例子和上边示例中的 averager 协程一样，只不过这里是作为字生成器使用
    def averager():
        total = 0.0
        count = 0
        average = None
        while True:
            # main 函数发送数据到这里
            term = yield
            if term is None: # 终止条件
                break
            total += term
            count += 1
            average = total/count
        return Result(count, average) # 返回的Result 会成为grouper函数中yield from表达式的值


    # 委派生成器
    def grouper(results, key):
         # 这个循环每次都会新建一个averager 实例，每个实例都是作为协程使用的生成器对象
        while True:
            # grouper 发送的每个值都会经由yield from 处理，通过管道传给averager 实例。grouper会在yield from表达式处暂停，等待averager实例处理客户端发来的值。averager实例运行完毕后，返回的值绑定到results[key] 上。while 循环会不断创建averager实例，处理更多的值。
            results[key] = yield from averager()


    # 调用方
    def main(data):
        results = {}
        for key, values in data.items():
            # group 是调用grouper函数得到的生成器对象，传给grouper 函数的第一个参数是results，用于收集结果；第二个是某个键
            group = grouper(results, key)
            group.send(None) #等价于next(group)
            for value in values:
                # 把各个value传给grouper 传入的值最终到达averager函数中；
                # grouper并不知道传入的是什么，同时grouper实例在yield from处暂停
                group.send(value)
            # 把None传入groupper，传入的值最终到达averager函数中，导致当前实例终止。然后继续创建下一个实例。
            # 如果没有group.send(None)，那么averager子生成器永远不会终止，委派生成器也永远不会在此激活，也就不会为result[key]赋值
            group.send(None)
        report(results)


    # 输出报告
    def report(results):
        for key, result in sorted(results.items()):
            group, unit = key.split(';')
            print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


    data = {
        'girls;kg':[40, 41, 42, 43, 44, 54],
        'girls;m': [1.5, 1.6, 1.8, 1.5, 1.45, 1.6],
        'boys;kg':[50, 51, 62, 53, 54, 54],
        'boys;m': [1.6, 1.8, 1.8, 1.7, 1.55, 1.6],
    }

    main(data)
if __name__ == '__main__':
    # test_call_back_learn()
    print ('--------------')
    # test_generator_learn()
    # test_hello()
    #test_yield_return()
    #yield_from_simple_use()
    #yield_from_flatten()
    use_yield_complex()
