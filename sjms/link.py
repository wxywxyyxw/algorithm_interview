# -*- coding: utf-8 -*-
from functools import wraps
from django.utils import six
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__')
import inspect

class SaveLink(object):
    def __init__(self):
        self.save_list = []

    def save(self,name):
        self.save_list.append(name)

save_obj = SaveLink()




def available_attrs(fn):
    """
    Return the list of functools-wrappable attributes on a callable.
    This is required as a workaround for http://bugs.python.org/issue3445
    under Python 2.
    """
    if six.PY3:
        return WRAPPER_ASSIGNMENTS
    else:
        return tuple(a for a in WRAPPER_ASSIGNMENTS if hasattr(fn, a))

def convert_exception_to_response(get_response):
    """
    Wrap the given get_response callable in exception-to-response conversion.

    All exceptions will be converted. All known 4xx exceptions (Http404,
    PermissionDenied, MultiPartParserError, SuspiciousOperation) will be
    converted to the appropriate response, and all other exceptions will be
    converted to 500 responses.

    This decorator is automatically applied to all middleware to ensure that
    no middleware leaks an exception and that the next middleware in the stack
    can rely on getting a response instead of an exception.
    """
    @wraps(get_response, assigned=available_attrs(get_response))
    def inner(request):
        if hasattr(get_response,'process_request'):
            print "name:", get_response.process_request.__name__
            name = get_response.process_request.__name__
        else:
            print "name:", get_response.__name__
            name = get_response.__name__

        save_obj.save(name)
        try:
            response = get_response(request)
        except Exception as exc:
            print 'exc:',exc
            response = exc
        return response
    return inner

def get_res(item):
    print "get_res {}".format(item)
    #raise  Exception('i am a exception')
    return "{} ok".format(item)


class M(object):
    def __init__(self,get_res):
        self.get_res = get_res

    def __call__(self, item):
        response = None
        if hasattr(self, 'process_request'):
            response,self.id = self.process_request(item)
        if not response:
            response = self.get_res(item)
        elif hasattr(self, 'process_response'):
            response = self.process_response(self.id)

        return response

class M1(M):
    def process_request(self,item):
        print "M1 {}".format(item)


class M2(M):
    def process_request(self,item):
        print "M2 {}".format(item)
        #raise  Exception('i am a exception')




#test

#@need(respon'a')
def test_func(a):
    c = 0
    return c

class A(object):
    pass

def a1(item):
    print "M1 {}".format(item)
    #raise  Exception('i am a exception')
def a1_d(item):
    print "M1D {}".format(item)

def a2(item):
    print "M2 {}".format(item)

def a2_d(item):
    print "M2D {}".format(item)



if __name__ == '__main__':
    m0 = convert_exception_to_response(get_res)

    mm1 = M(m0)
    mm1.process_request = a1

    m1 = convert_exception_to_response(mm1)

    mm2 = M(m1)
    mm2.process_request = a2

    m2 = convert_exception_to_response(mm2)

    #test_func('a')
    #res = inspect.getargspec(test_func)
    print m2('a')
    print save_obj.save_list

    # a = A()
    # a.c = test_func
    # print a.c(1)
    # print a.c.__name__