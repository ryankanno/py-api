#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from py_api.api import ApiClient
from py_api.endpoint import Endpoint
import unittest


class FakeApiClient(ApiClient):

    HOST = "http://github.com"

    def _host(self):
        return self.HOST


class TestEndpoint(unittest.TestCase):

    def setUp(self):
        self.api = FakeApiClient()
        self.path = "/foo/bar"
        self.method = 'GET'
        self.endpoint = Endpoint(self.method, self.path)

    def test_endpoint(self):
        eq_(self.endpoint.path, self.path)
        eq_(self.endpoint.method, self.method)

# vim: filetype=python
