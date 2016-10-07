#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from threading import Thread
from threading import Timer
import datetime
now = datetime.datetime.now

def background_worker(second):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            def TaskManager():
                func()
                t = Timer(second, TaskManager);
                t.start()
                return t
            func_hl = Thread(target=TaskManager, args=args, kwargs=kwargs)
            #func_hl.daemon = True
            func_hl.start()
            return func_hl
        return wrapper
    return my_decorator

@background_worker(10)
def some_job():
    print 'job', now()

some_job()


