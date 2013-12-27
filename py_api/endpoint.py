#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests

logger = logging.getLogger(__name__)


class Endpoint(object):

    def __init__(self, path, method, *args, **kwargs):
        self._path = path
        self._method = method
        self._args = args
        self._kwargs = kwargs

    @property
    def path(self):
        return self._path

    @property
    def method(self):
        return self._method

    def __call__(self, *args, **kwargs):
        def _call_endpoint(api, *args, **kwargs):
            return Requestor(api, self, *args, **kwargs)()
        return _call_endpoint


class Get(Endpoint):
    def __init__(self, path, *args, **kwargs):
        super(Get, self).__init__(path, 'GET', *args, **kwargs)


class Requestor(object):

    def __init__(self, api, endpoint, *args, **kwargs):
        self.api = api
        self.endpoint = endpoint
        self._args = args
        self._kwargs = kwargs

    def _construct_url(self, api, endpoint):
        return (api.host + endpoint.path).format(**self._kwargs)

    def __call__(self):
        url = self._construct_url(self.api, self.endpoint)
        logger.debug("Making call to {0}".format(url))
        return requests.request(self.endpoint.method, url).text

# vim: filetype=python
