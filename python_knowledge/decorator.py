from collections import Iterable
#闭包就是引用了自有变量的函数，这个函数保存了执行的上下文，可以脱离原本的作用域独立存在。
# print_msg是外围函数
def print_msg():
    msg = "I'm closure"

    # printer是嵌套函数
    def printer():
        print(msg)

    return printer


# 这里获得的就是一个闭包
closure = print_msg()
# 输出 I'm closure
closure()

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper

@log
def test(p):
    print(test.__name__ + " param: " + p)

test("I'm a param")


wrapper = log(test)
wrapper("I'm a param")

print('-----------------')

def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator

@log_with_param("eeeee")
def test_with_param(p):
    print(test_with_param.__name__)

test_with_param('aa')

print('-----------------')

def test2_with_param(p):
    print(test_with_param.__name__)

# 传入装饰器的参数，并接收返回的decorator函数
decorator = log_with_param("param")

# 传入test_with_param函数
wrapper = decorator(test2_with_param)
# 调用装饰器函数
wrapper("I'm a param")

print('-----------------')

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)