def test_fun():
    list_a=[]

    def set_a(a):
        list_a.append(a)
    a = A()
    b = a(set_a)
    print (list_a, b)


class A:

    def __call__(self,fun):
        fun('a')
        return 'b'

test_fun()