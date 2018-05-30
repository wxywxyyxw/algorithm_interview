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

if __name__ == '__main__':
    # test_call_back_learn()
    print ('--------------')
    # test_generator_learn()
    # test_hello()
    test_basic_yield()
