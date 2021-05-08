import os
import psutil



def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))



def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(10000000)]
    #range(1000000)
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')

def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(10000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')

#test_iterator()
#print ("------------")
#test_generator()

class A():
    data = 0
    def __iter__(self):
        return self

    def next(self):
        if self.data > 3:
            raise StopIteration
        else:
            self.data += 1
            return self.data

# a = A()
# print a.next()
# print a.next()
# print a.next()
# print a.next()
# print a.next()

def fib(end = 1000):
    prev,curr=0,1
    while curr < end:
        print 'curr', curr
        yield curr
        prev,curr=curr,curr+prev

# a = fib()
# print a.next()
# print a.next()
# print a.next()
for item in fib():
    print item




