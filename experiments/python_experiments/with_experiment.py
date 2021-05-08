# -*- coding: utf-8 -*-
import time
from contextlib import contextmanager

"""
实验名称：如何让一个类能使用with

它是一种上下文管理协议，目的在于从流程图中把 try,except 和finally 关键字和

资源分配释放相关代码统统去掉，简化try….except….finlally的处理流程。

用类实现with的方法:
    只要一个类实现 一个带返回值的__enter__方法 和 一个 __exit__ 方法。就能用with调用。

用method实现with的方法:
    实现一个新的上下文管理器的最简单的方法就是使用 contexlib 模块中的 @contextmanager 装饰器。
    下面是一个实现了代码块计时功能的上下文管理器例子：

import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))
　　
#Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1
　　
注:
在函数 timethis() 中，yield 之前的代码会在上下文管理器中作为 __enter__() 方法执行， 
所有在 yield 之后的代码会作为 __exit__() 方法执行。 如果出现了异常，异常会在yield语句那里抛出。

参考资料:
https://www.cnblogs.com/xiaxiaoxu/p/9747551.html
https://www.cnblogs.com/feifeifeisir/p/11475732.html
"""

class TestWith(object):
    def __init__(self):
        print ('init')
        self.handle = 'handle'

    def __enter__(self):
        print ('enter')
        return self.handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print ("[Exit %s]:Exited without exception."%self.handle)
        else:
            print ("[Exit %s]: Exited with exception raised."%self.handle)

class TestWithClass(object):
    handle = 'handle_class'

    @classmethod
    def __enter__(cls):
        print ('enter')
        return cls.handle

    @classmethod
    def __exit__(cls, exc_type, exc_val, exc_tb):
        """
        exc_type： 错误的类型
        exc_val：　错误类型对应的值
        exc_tb：　 代码中错误发生的位置
        """
        if exc_tb is None:
            print ("[Exit %s]:Exited without exception."%cls.handle)

        else:
            print ("[Exit %s]: Exited with exception raised."%cls.handle)
        print('error is {}'.format(exc_tb))

# with TestWith() as fb:
#     print (fb)
#
# with TestWith() as fb:
#     print (fb/0)

# with TestWithClass() as fb:
#     print (fb)
#
# with TestWithClass() as fb:
#     print (fb/0)

#print ('end')

@contextmanager
def timethis(label):
    start = time.time()
    try:
        print ('timethis')
        yield 5
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))

#Example use
with timethis('counting') as fb:
    print (fb)
    n = 10
    while n > 0:
        n -= 1