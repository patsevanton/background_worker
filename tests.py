import pytest
from threading import Thread
# from background_worker import some_job
from background_worker import BackgroundWorker as background_worker


def test__is_returned_a_thread():
    @background_worker(2)
    def t1(args, **kwargs):
        return
    assert isinstance(t1(), Thread)



def test__thread_works_in_background():
    from time import sleep
    times = 10

    @background_worker(1)
    def t1(x, **kwargs):
        y=kwargs.get("y")
        x.append(1)
        y.append(1)
    _listx = []
    _listy = []
    t1(_listx, y=_listy)
    sleep(times)
    assert len(_listx) == times
    assert len(_listy) == times


