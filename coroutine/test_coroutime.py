import time
import asyncio

def test_time():


    now = lambda : time.time()

    async def do_some_work(x):
        print('Waiting: ', x)

    async def sleeps():
        print('I am sleep')
        await asyncio.sleep(5)
        print('I am awake')

    async def funny():
        print('I am funny')



    start = now()

    coroutine = do_some_work(2)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)
    loop.run_until_complete(sleeps())
    loop.run_until_complete(funny())

    print('TIME: ', now() - start)


def test_sleep():
    now = lambda: time.time()

    async def do_some_work(x):
        print('Waiting: ', x)
        await asyncio.sleep(x)
        return 'Done after {}s'.format(x)

    start = now()

    coroutine = do_some_work(5)

    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)

    loop.run_until_complete(task)

    print('Task ret: ', task.result())
    print('TIME: ', now() - start)


def test_tasks():
    now = lambda: time.time()

    async def do_some_work(x):
        print('Waiting: ', x)

        await asyncio.sleep(x)
        return 'Done after {}s'.format(x)

    start = now()

    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print('Task ret: ', task.result())

    print('TIME: ', now() - start)

def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    while index < up_to:
        yield index
        index += 1


def lazy_range2(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    def gratuitous_refactor():
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()

def jumping_range(up_to):
    """Generator for the sequence of integers from 0 to up_to, exclusive.

    Sending a value into the generator will shift the sequence by that amount.
    """
    index = 0
    while index < up_to:
        jump = yield index
        print ('jump: {}'.format(jump))
        if jump is None:
            jump = 1
        index += jump


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

def test_wget():
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    # for i in  lazy_range(10):
    #     print (i)

    # a = lazy_range(10)
    # print (a)
    # iterator = jumping_range(500)
    # print(next(iterator))  # 0
    # print(next(iterator))  # 0
    # print(iterator.send(100))  # 2
    #print(next(iterator))  # 3
    #print(iterator.send(-1))  # 2
    #for x in iterator:
    #    print(x)  # 3, 4

    a = lazy_range2(4)
    for i in a:
        print (i)