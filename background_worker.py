#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import datetime
import time
import threading
now = datetime.datetime.now

def background_worker(second):
    def my_decorator(func):
        def wrapper():
            while True:
                time.sleep(second)
                func()
            return func()

        t = threading.Thread(target=wrapper)
        t.daemon = True
        t.start()
        return wrapper
    return my_decorator


@background_worker(10)
def some_job():
    print 'job', now()

some_job()

