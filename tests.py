import pytest
import background_worker

def test_identified_thread_object():
    assert some_job().getName() == 'MyName'
