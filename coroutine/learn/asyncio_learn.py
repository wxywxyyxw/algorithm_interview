import time
import asyncio

def sample1():

    now = lambda : time.time()

    async def do_some_work(x):
        time.sleep(5)
        print('Waiting: ', x)

    async def do_some_work2(x):
        print('Waiting: ', x)

    start = now()

    coroutine = do_some_work(2)
    coroutine2 = do_some_work2(100)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)
    loop.run_until_complete(coroutine2)

    print('TIME: ', now() - start)

def sample2():
    now = lambda : time.time()

    async def do_some_work(x):
        print('Waiting: ', x)

    start = now()

    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    # task = asyncio.ensure_future(coroutine)
    task = loop.create_task(coroutine)
    print(task)
    loop.run_until_complete(task)
    print(task)
    print('TIME: ', now() - start)

def sample3():
    now = lambda : time.time()

    async def do_some_work(x):
        print('Waiting: ', x)
        return 'Done after {}s'.format(x)

    def callback(future):
        print ('aaa: ',future.aaa)
        print('Callback: ', future.result())

    start = now()

    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    task.add_done_callback(callback)
    task.aaa=100
    loop.run_until_complete(task)

    print('TIME: ', now() - start)

def sample4():
    now = lambda : time.time()
    async def do_some_work(x):
        print('Waiting {}'.format(x))
        return 'Done after {}s'.format(x)

    start = now()

    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    loop.run_until_complete(task)

    print('Task ret: {}'.format(task.result()))
    print('TIME: {}'.format(now() - start))

def sample5():
    now = lambda: time.time()

    async def do_some_work(x):
        print('Waiting: ', x)
        await asyncio.sleep(x)
        return 'Done after {}s'.format(x)

    start = now()

    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    loop.run_until_complete(task)

    print('Task ret: ', task.result())
    print('TIME: ', now() - start)

def sample6():
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

def sample7():
    now = lambda: time.time()

    async def do_some_work(x):
        print('Waiting: ', x)

        await asyncio.sleep(x)
        return 'Done after {}s'.format(x)

    async def main():
        coroutine1 = do_some_work(1)
        coroutine2 = do_some_work(2)
        coroutine3 = do_some_work(4)

        tasks = [
            asyncio.ensure_future(coroutine1),
            asyncio.ensure_future(coroutine2),
            asyncio.ensure_future(coroutine3)
        ]

        dones, pendings = await asyncio.wait(tasks)

        for task in dones:
            print('Task ret: ', task.result())

    start = now()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    print('TIME: ', now() - start)






if __name__ == '__main__':
    sample7()

