#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests

logger = logging.getLogger(__name__)


class Endpoint(object):

    def __init__(self, api, path, method, *args, **kwargs):
        self._api = api
        self._path = path
        self._method = method

    @property
    def path(self):
        return self._path

    @property
    def method(self):
        return self._method

    # TODO
    @property
    def url(self):
        return ""

    def __call__(self, *args, **kwargs):
        def _call_endpoint(api, *args, **kwargs):
            return EndpointMethod(api, self, *args, **kwargs)()
        return _call_endpoint


class EndpointMethod(object):

    def __init__(self, api, endpoint, *args, **kwargs):
        self.api = api
        self.endpoint = endpoint

    def __call__(self):
        method = self.endpoint.method
        url = self.endpoint.url
        return request(method, url, **kwargs)

# vim: filetype=python
