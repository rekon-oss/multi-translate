# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import multitranslateclient
from multitranslateclient.api.default_api import DefaultApi  # noqa: E501
from multitranslateclient.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = multitranslateclient.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ready_get(self):
        """Test case for ready_get

        Ready  # noqa: E501
        """
        pass

    def test_translate_post_translate_post(self):
        """Test case for translate_post_translate_post

        Translate Post  # noqa: E501
        """
        pass

    def test_translate_translate_get(self):
        """Test case for translate_translate_get

        Translate  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
