# -*- coding: utf-8 -*-
import sys

def _test(a):
    print a

class A(object):
    def _test(self):
        print "test"
    def __another_test(self):
        print "another_test"

    def test2(self):
        self.__another_test()

class B(A):
    def __init__(self):
        super(B)

    def __another_test(self):
        print "B another_test"

    def _test(self):
        print "B test"

    def test3(self):
        self.__another_test()

def _funa(a):
    print sys.getrefcount(a)
    return a


def test_count():
    a = 1
    print sys.getrefcount(a) #x

    b= a

    print sys.getrefcount(a) #x+1

    _funa(a)

    print sys.getrefcount(a) #x+1

    list1 = [a,1,2,3]

    print sys.getrefcount(a) #x+2

    del list1

    print sys.getrefcount(a) #x+1

def list_or_tuple(x):
      return isinstance(x, (list, tuple))
def flatten(sequence, to_expand=list_or_tuple):
      for item in sequence:
            if to_expand(item):
                  for subitem in flatten(item, to_expand):
                        print 'subitem'
                        yield subitem
            else:
                  print 'item'
                  yield item


def flatten2(sequence):
    for item in sequence:
        if isinstance(item,(list,tuple)):
            for subitem in flatten2(item):
                print 'subitem'
                yield  subitem
        else:
            print 'item'
            yield item

def test_yield(sequence):
    for i in sequence:
        if isinstance(i,list):
            for item in i:
                print 'item'
                yield item
        else:
            print 'i'
            yield i




if __name__ == '__main__':
    # a = A()
    # print dir(a)
    # a.test2()
    #
    # b = B()
    # b._test()

    # for i in flatten2([1, 2, [3, [  ], 4, [5, 6], 7, [8,], ], 9]):
    #     print i
    # a =  flatten2([1, 2, [3, [  ], 4, [5, 6], 7, [8,], ], 9])
    # print a
    # print a
    # print a

    for i in flatten2([1,2,[3,[4,5]],6]):
        print i
