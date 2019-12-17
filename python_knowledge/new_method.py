class A(object):
    pass

class C():
    pass

class B(A):
    def __new__(cls):
        print("__new__方法被执行")
        a = super().__new__(cls)
        print(type(a))
        #d = a()
        a.aa=1
        return C()

    def __init__(self):
        print("__init__方法被执行")

#b = B()
#print(type(B))
#print(b.aa)

class Single(object):
    __isstance = None
    __first_init = False
    def __new__(cls, *args, **kwargs):
        if not cls.__isstance:
            cls.__isstance = super().__new__(cls)
        return cls.__isstance
    def __init__(self, name):
        if not self.__first_init:
            self.name = name
            Single.__first_init = True

a = Single('aaa')
b = Single('bbb')
print(a == b)
print(a.name,b.name)


