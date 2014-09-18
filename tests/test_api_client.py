#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from py_api.api import ApiClient
from py_api.endpoint import Endpoint
import unittest


class GoogleApiClient(ApiClient):

    HOST = "http://google.com"

    def _host(self):
        return self.HOST


class TestApiClient(unittest.TestCase):

    def setUp(self):
        self.api = GoogleApiClient()

    def test_request(self):
        endpoint = Endpoint('GET', '/')
        response = self.api.request(endpoint)
        ok_(response.response.status_code == 200)

# vim: filetype=python
