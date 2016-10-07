#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import datetime
import time
import threading
now = datetime.datetime.now

def background_worker(second):
    def wrapper(func):
        while True:
            time.sleep(second)
            threading.Thread(target=func())
        return func()
    return wrapper


@background_worker(10)
def some_job():
    print 'job', now()

some_job()
