#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from py_api.api import Api
from py_api.endpoint import Endpoint
import unittest


class FakeApi(Api):

    HOST = "http://github.com"

    def _host(self):
        return self.HOST


class TestEndpoint(unittest.TestCase):

    def setUp(self):
        self.api = FakeApi()
        self.path = "/foo/bar"
        self.method = 'GET'
        self.endpoint = Endpoint(self.path, self.method)

    def test_endpoint(self):
        eq_(self.endpoint.path, self.path)
        eq_(self.endpoint.method, self.method)

# vim: filetype=python
