#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class Endpoint(object):
    def __init__(self, raw_path, method, *args, **kwargs):
        self._raw_path = raw_path
        self._method = method

    @property
    def path(self):
        return self._raw_path

    @property
    def method(self):
        return self._method


def Get(path, *args, **kwargs):
    endpoint = Endpoint(path, 'GET', *args, **kwargs)

    def _create_endpoint(api, *call_args, **call_kwargs):
        return api.request(endpoint)

    return _create_endpoint

# vim: filetype=python
