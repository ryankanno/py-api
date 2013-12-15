from nose.tools import *
from py_api.api import Api
from py_api.endpoint import Endpoint
import unittest


class FakeApi(Api):
    pass


class TestEndpoint(unittest.TestCase):

    def setUp(self):
        self.api = FakeApi()
        self.path = "/foo/bar"
        self.method = 'GET'
        self.endpoint = Endpoint(self.api, self.path, method=self.method)

    def tearDown(self):
        pass

    def test_endpoint(self):
        eq_(self.endpoint.path, self.path)
        eq_(self.endpoint.method, self.method)
