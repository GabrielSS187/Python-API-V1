# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

class CustomError(Exception):
    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code = status_code
