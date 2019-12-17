import inspect
class ModelBase(type):
    def __new__(cls, name, bases, attrs):
        print ('ModelBase __new__ ',locals())
        super_new = super(ModelBase, cls).__new__
        print (super_new == type.__new__)
        new_class = super_new(cls, name, bases, attrs)
        print ('after')
        return new_class

def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):

        def __new__(cls, name, this_bases, d):
            print ('metaclass __new__: ',locals())
            new_class = meta(name, bases, d)
            print ('new class: ',new_class)
            return new_class
    print ("with_metaclass locals: ",meta)
    return type.__new__(metaclass, 'temporary_class', (), {})

class Model(with_metaclass(ModelBase)):
    def __init__(self):
        super(Model, self).__init__()


print (Model.__base__.__name__)


# class A(Model):
#     a1 = 1
#     b1 = 2

#a = A()
# w = with_metaclass(ModelBase)
# print ('w: ',w)
# a = inspect.getmro(w)
# print ('a: ',a)
# class Model(w):
#     pass

# class Model(with_metaclass(ModelBase)):
#     pass



# class B(Model):
#     a=1
#print (inspect.getmro(Model))




#m = Model()
#print (inspect.getmro(m))

# print ('with_metaclass: ', with_metaclass(ModelBase))
# class A(type):
#     pass
# b = type.__new__(A,'a',(),{})
# print (b)

# class A(object):
#     def __init__(self):
#         print "init"
#     def __new__(cls,*args, **kwargs):
#         print "new %s"%cls
#         c = object.__new__(cls, *args, **kwargs)
#         print id(c)
#         return c
#
#
# a = A()
# print id(a)


# class B(type):
#     def __init__(self):
#         super(b).__init__()
#     def __new__(cls, *args, **kwargs):
#         print (cls)
#         return type.__new__(cls,'asdadfa',(), {})
#
# b = B()


