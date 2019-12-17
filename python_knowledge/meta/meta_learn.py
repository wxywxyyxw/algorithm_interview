def with_metaclass(meta, *bases):
    """Compatible metaclass

    :param meta: the metaclass
    :param *bases: base classes
    """
    return meta('temp_class', bases, {})

# Testing:
class TestMeta(type):
    def __new__(cls, name, bases, d):
        d['a'] = 'xyz'
        return type.__new__(cls, name, bases, d)


class Foo(object):pass

class Bar(with_metaclass(TestMeta, Foo)): pass

print (Bar.a)
print (Bar.__mro__)



def with_metaclass2(meta, *bases):
    class metaclass(type):
        def __new__(cls, name, this_bases, d):
            print(cls, "new is called",this_bases)
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temp_class', (), {})

# Testing:
class TestMeta2(type):
    def __new__(cls, name, bases, d):
        d['a'] = 'xyz'
        print(cls, "new is called")
        return type.__new__(cls, name, bases, d)

temp = with_metaclass2(TestMeta2, Foo)
class Bar2(temp): pass

print (Bar2.__mro__)

