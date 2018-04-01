# -*- coding: utf-8 -*-
from basics import *


def quotation_marks():
    str1 = "123"
    print str1

    str2 = """123
    123
    123"""
    print str2


"""
依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)，
提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass
"""


def new_and_init():
    class Person(object):
        """Silly Person"""

        def __new__(cls, name, age):
            print '__new__ called.'
            # __new__和__init__在类创建的时候都传入了(相同)的参数
            return super(Person, cls).__new__(cls, name, age)

        def __init__(self, name, age):
            print '__init__ called.'
            self.name = name
            self.age = age

        def __str__(self):
            return '<Person: %s(%s)>' % (self.name, self.age)

    piglei = Person('piglei', 24)
    print piglei

    class Client(object):
        def __new__(cls, id, is_vip):
            print '__new__ called.'
            return super(Client, cls).__new__(cls, id, is_vip)

        def __init__(self, id, is_vip):
            print '__init__ called.'
            self.id = id
            self.is_vip = is_vip

        def __str__(self):
            return '<Client {id} {is_vip}>'.format(id=self.id, is_vip=self.is_vip)

    client = Client(1, 'is_vip')
    print client

    # 假如我们需要一个永远都是正数的整数类型，通过集成int
    class PositiveInteger(int):
        def __new__(cls, value):
            return super(PositiveInteger, cls).__new__(cls, abs(value))

    i = PositiveInteger(-3)
    print i

    # 通过重新new方法实现一个永远都是负数的类
    class NegativeInteger(int):
        def __new__(cls, value):
            return super(NegativeInteger, cls).__new__(cls, -abs(value))

    i = NegativeInteger(8)
    print i

    """
    事实上，当我们理解了__new__方法后，我们还可以利用它来做一些其他有趣的事情，比如实现 设计模式中的 单例模式(singleton) 。
    因为类每一次实例化后产生的过程都是通过__new__来控制的，所以通过重载__new__方法，我们 可以很简单的实现单例模式。
    """

    class Singleton(object):
        def __new__(cls):
            # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
            if not hasattr(cls, 'instance'):
                cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    obj1 = Singleton()
    obj2 = Singleton()
    obj1.attr1 = 'value1'
    print (obj1.attr1, obj2.attr1)
    print (obj1 is obj2)


# 实现但例模式
def test_singleton():
    # cls是类
    def Singleton(cls):
        print (cls)
        # _instance {A:a} a=A() class是key,class的实例是value
        _instance = {}

        def _singleton(*args, **kargs):
            # 如果这个class不在key中
            if cls not in _instance:
                # 加入到key中
                _instance[cls] = cls(*args, **kargs)
            return _instance[cls]

        return _singleton

    @Singleton
    class A(object):
        a = 1

        def __init__(self, x=0):
            self.x = x

    a1 = A(2)
    # 当第二次生成实例时，其实是返回的第一次的实例
    a2 = A(3)
    print a2.x  # 2


# lambda函数
def test_lambada():
    li = [lambda: x for x in range(10)]

    res = li[0]
    print(res)

    a = lambda: 100  # 不加参数的lambda

    print a()


if __name__ == '__main__':
    # _test(1) 下划线的方法不能被 import * 调用
    # new_and_init()
    test_lambada()
