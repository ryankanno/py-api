#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from nose.tools import ok_
from py_api.errors import ApiClientError
from py_api.errors import ApiRequestError
import unittest


class TestApiClientError(unittest.TestCase):

    def setUp(self):
        self.client_error_message = "foobar"
        self.client_error = ApiClientError(self.client_error_message)

    def test_api_client_error(self):
        eq_(self.client_error.error_message, self.client_error_message)
        ok_(issubclass(type(self.client_error), Exception))


class TestApiRequestError(unittest.TestCase):

    def setUp(self):
        self.request_error_message = "foobar"
        self.request_status_code = 500
        self.request_error = ApiRequestError(self.request_status_code,
                                             self.request_error_message)

    def test_api_request_error(self):
        eq_(self.request_error.error_message, self.request_error_message)
        eq_(self.request_error.status_code, self.request_status_code)
        ok_(issubclass(type(self.request_error), Exception))

# vim: filetype=python
