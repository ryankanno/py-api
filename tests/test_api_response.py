#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from py_api.api import ApiResponse
import unittest


class TestApiResponse(unittest.TestCase):

    def test_response(self):
        ar = ApiResponse("foo")
        ok_(ar.response == "foo")

# vim: filetype=python
