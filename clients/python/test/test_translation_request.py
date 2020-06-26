# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import multitranslateclient
from multitranslateclient.models.translation_request import TranslationRequest  # noqa: E501
from multitranslateclient.rest import ApiException

class TestTranslationRequest(unittest.TestCase):
    """TranslationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TranslationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = multitranslateclient.models.translation_request.TranslationRequest()  # noqa: E501
        if include_optional :
            return TranslationRequest(
                source_text = '0', 
                to_language = '0', 
                from_language = '0', 
                preferred_engine = 'best', 
                with_alignment = True, 
                fallback = True
            )
        else :
            return TranslationRequest(
                source_text = '0',
                to_language = '0',
        )

    def testTranslationRequest(self):
        """Test TranslationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()