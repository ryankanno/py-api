#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import logging

logger = logging.getLogger(__name__)


class ApiBase(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        pass


class Api(ApiBase):

    def __init__(self, *args, **kwargs):
        pass

# vim: filetype=python
