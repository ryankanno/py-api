#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import logging
import requests

logger = logging.getLogger(__name__)


class ApiBase(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def _host(self):
        """ must implement """
        return

    @property
    def host(self):
        return self.__class__._host(self)


class ApiClient(ApiBase):

    def __init__(self, *args, **kwargs):
        super(ApiClient, self).__init__(*args, **kwargs)

    def request(self, endpoint):
        request = ApiRequest(self, endpoint)
        return request.execute()


class ApiRequest(object):

    def __init__(self, api, endpoint, *args, **kwargs):
        super(ApiRequest, self).__init__(*args, **kwargs)
        self.api = api
        self.endpoint = endpoint

    def execute(self):
        url = self._construct_url(self.api, self.endpoint)
        resp = requests.request(self.endpoint.method, url)
        return ApiResponse(resp)

    def _construct_url(self, api, endpoint):
        return api.host + endpoint.path


class ApiResponse(object):

    def __init__(self, response, *args, **kwargs):
        super(ApiResponse, self).__init__(*args, **kwargs)
        self.response = response

    def __str__(self):
        return self.response.text

# vim: filetype=python
