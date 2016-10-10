import pytest
from background_worker import some_job

def test_identified_thread_object():
    assert some_job().getName() == 'MyName'
