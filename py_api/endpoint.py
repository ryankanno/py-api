#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class Endpoint(object):

    def __init__(self, api, path, method, *args, **kwargs):
        self.api = api
        self.path = path
        self.method = method

    def __call__(self, *args, **kwargs):
        def _call_endpoint(api, *args, **kwargs):
            return EndpointMethod(api, *args, **kwargs)()
        return _call_endpoint


class EndpointMethod(object):

    def __init__(self, api, *args, **kwargs):
        pass

    def __call__(self):
        pass

# vim: filetype=python
