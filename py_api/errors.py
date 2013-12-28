#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ApiRequestError(Exception):
    def __init__(self, status_code, error_message, *args, **kwargs):
        super(ApiRequestError, self).__init__(*args, **kwargs)
        self.status_code = status_code
        self.error_message = error_message


class ApiClientError(Exception):
    def __init__(self, error_message, *args, **kwargs):
        super(ApiClientError, self).__init__(*args, **kwargs)
        self.error_message = error_message

# vim: filetype=python
