#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from py_api.api import ApiClient
import unittest


class FakeApiClient(ApiClient):

    HOST = "http://github.com"

    def _host(self):
        return self.HOST


class TestApi(unittest.TestCase):

    def setUp(self):
        self.api = FakeApiClient()

    def test_api(self):
        eq_(self.api.host, FakeApiClient.HOST)

# vim: filetype=python
