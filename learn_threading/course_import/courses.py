import os
import requests
import gevent



def _get_request(i=""):
    print ('request {} {}'.format(i,os.getpid()))
    requests.get('http://www.baidu.com')

def test_request():
    task_list = []
    for i in range(10):
        task_list.append(gevent.spawn(_get_request,i
        ))

    #logger.info('{} get www.baidu.com'.format(os.getppid()))

