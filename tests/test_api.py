#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from py_api.api import Api
import unittest


class FakeApi(Api):

    HOST = "http://github.com"

    def _host(self):
        return self.HOST


class TestApi(unittest.TestCase):

    def setUp(self):
        self.api = FakeApi()

    def test_api(self):
        eq_(self.api.host, FakeApi.HOST)

# vim: filetype=python
