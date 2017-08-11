import pytest
import sys 
from aslo import init_app


class TestSimple(object):
    def test_simple(self):
        print("It works")

    def test_if_app_starts(self):
        app = init_app()
        assert(app)    