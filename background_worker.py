#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

from functools import wraps
from threading import Thread
from threading import Timer
import datetime
from time import sleep

now = datetime.datetime.now


class BackgroundWorker(object):

    def __init__(self, argument):
        self.arg = argument
        self.daemon = True

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            def task_manager(*args, **kwargs):
                while True:
                    sleep(self.arg)
                    func(args, **kwargs)
            func_hl = Thread(name='MyName', target=task_manager, args=args, kwargs=kwargs)
            func_hl.daemon = True
            func_hl.start()
            return func_hl
        return decorated
