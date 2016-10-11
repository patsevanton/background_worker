#!/usr/bin/env python
from sys import exit
from datetime import datetime
from time import sleep
from background_worker import BackgroundWorker as background_worker


now = datetime.now


@background_worker(1)
def some_job(*args, **kwargs):
    print("running into separated thread", now())
    print("args is %s, kwargs is %s" % (args, kwargs))



some_job(1,2,4, ebola=True)
print("going to sleep...")
sleep(10)
print("I'm here with you again!")
exit(0)
