def run():
    print('start running')
    yield 2     # 跑步用时2小时

def eat():
    print('start eating')
    yield 1     # 吃饭用时1小时

def time():
    run_time = yield run()
    eat_time = yield eat()
    print(run_time+eat_time)

def Runner(gen):
    r = next(gen)
    return r

t = time()
try:
    action = t.send(Runner(next(t)))
    print (action)
    t.send(Runner(action))
    t.send(Runner(action))
    t.send(Runner(action))
except StopIteration:
    pass