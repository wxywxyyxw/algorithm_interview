import weakref


def on_finalize(*args):
    print ("on_finalize ", args)

class ExpensiveObject:
    a=1
    def __del__(self):
        print('(Deleting {})'.format(self))

    def __call__(self):
        print("call me")

obj = ExpensiveObject()

#r = weakref.ref(obj, on_finalize)


r = weakref.finalize(obj, on_finalize)




# r = weakref.ref(obj)
#
# print('obj:', obj)
# print('ref:', r)
# print('r():', r())
# print('deleting obj')
del obj
print('r():', r())


# r =obj
#
# print('obj:', obj)
# print('ref:', r)
# print('deleting obj')
# del obj
# print('ref:', r,r.a)
# print('obj:', obj)
