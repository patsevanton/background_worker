#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from functools import wraps
from threading import Thread
from threading import Timer
import datetime

now = datetime.datetime.now


class background_worker(object):
    def __init__(self, argument):
        self.arg = argument
        self.daemon = False

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            def task_manager():
                func()
                t = Timer(self.arg, task_manager)
                t.start()
                return t

            func_hl = Thread(name='MyName',target=task_manager, args=args, kwargs=kwargs)
            func_hl.daemon = True
            func_hl.run()
            self.daemon = True
            return func_hl

        return decorated


@background_worker(10)
def some_job():
    print 'job', now()


some_job()
