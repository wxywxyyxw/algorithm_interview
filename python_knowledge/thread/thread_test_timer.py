import threading
import time

def hello(name):
    print ("hello %s\n" % name)
    global timer
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()

if __name__ == "__main__":
    timer = threading.Timer(2.0, hello, ["Hawk"])   ##每隔两秒调用函数hello
    timer.start()