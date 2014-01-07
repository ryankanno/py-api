#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class Endpoint(object):
    def __init__(self, method, raw_path, *args, **kwargs):
        self._method = method
        self._raw_path = raw_path

    @property
    def method(self):
        return self._method

    @property
    def path(self):
        return self._raw_path


def Get(path, *args, **kwargs):
    return _method('GET', path, args, kwargs)


def Post(path, *args, **kwargs):
    return _method('POST', path, args, kwargs)


def _method(method, path, *args, **kwargs):
    endpoint = Endpoint(method, path, *args, **kwargs)

    def _create_endpoint(api, *call_args, **call_kwargs):
        return api.request(endpoint, call_args, call_kwargs)

    return _create_endpoint

# vim: filetype=python
