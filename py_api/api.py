#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import logging

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


class Api(ApiBase):

    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)

# vim: filetype=python
