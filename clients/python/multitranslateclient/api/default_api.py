# coding: utf-8

"""
    multi-translate

    Multi-Translate is a unified interface on top of various translate APIs providing optimal translations, persistence, fallback.  # noqa: E501

    The version of the OpenAPI document: 0.2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from multitranslateclient.api_client import ApiClient
from multitranslateclient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ready_get(self, **kwargs):  # noqa: E501
        """Ready  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ready_get(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """
        kwargs['_return_http_data_only'] = True
        return self.ready_get_with_http_info(**kwargs)  # noqa: E501

    def ready_get_with_http_info(self, **kwargs):  # noqa: E501
        """Ready  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ready_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ready_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def translate_post_translate_post(self, translation_request, **kwargs):  # noqa: E501
        """Translate Post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.translate_post_translate_post(translation_request, async_req=True)
        >>> result = thread.get()

        :param translation_request: (required)
        :type translation_request: TranslationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TranslationResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.translate_post_translate_post_with_http_info(translation_request, **kwargs)  # noqa: E501

    def translate_post_translate_post_with_http_info(self, translation_request, **kwargs):  # noqa: E501
        """Translate Post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.translate_post_translate_post_with_http_info(translation_request, async_req=True)
        >>> result = thread.get()

        :param translation_request: (required)
        :type translation_request: TranslationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TranslationResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'translation_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method translate_post_translate_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'translation_request' is set
        if self.api_client.client_side_validation and ('translation_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['translation_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `translation_request` when calling `translate_post_translate_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'translation_request' in local_var_params:
            body_params = local_var_params['translation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/translate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TranslationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def translate_translate_get(self, source_text, to_language, **kwargs):  # noqa: E501
        """Translate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.translate_translate_get(source_text, to_language, async_req=True)
        >>> result = thread.get()

        :param source_text: The text to be translated (required)
        :type source_text: str
        :param to_language: The ISO-639-1 code of the language to translate the text to (required)
        :type to_language: str
        :param from_language: The ISO-639-1 code of the language to translate the text from - if notspecified then detection will be attempted
        :type from_language: str
        :param preferred_engine: Which translation engine to use. Choices are microsoft, google, amazon, papago, deepl, yandex and best
        :type preferred_engine: str
        :param with_alignment: Whether to return word alignment information or not
        :type with_alignment: bool
        :param fallback: Whether to fallback to the best available engine if the preferred engine does not succeed
        :type fallback: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TranslationResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.translate_translate_get_with_http_info(source_text, to_language, **kwargs)  # noqa: E501

    def translate_translate_get_with_http_info(self, source_text, to_language, **kwargs):  # noqa: E501
        """Translate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.translate_translate_get_with_http_info(source_text, to_language, async_req=True)
        >>> result = thread.get()

        :param source_text: The text to be translated (required)
        :type source_text: str
        :param to_language: The ISO-639-1 code of the language to translate the text to (required)
        :type to_language: str
        :param from_language: The ISO-639-1 code of the language to translate the text from - if notspecified then detection will be attempted
        :type from_language: str
        :param preferred_engine: Which translation engine to use. Choices are microsoft, google, amazon, papago, deepl, yandex and best
        :type preferred_engine: str
        :param with_alignment: Whether to return word alignment information or not
        :type with_alignment: bool
        :param fallback: Whether to fallback to the best available engine if the preferred engine does not succeed
        :type fallback: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TranslationResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'source_text',
            'to_language',
            'from_language',
            'preferred_engine',
            'with_alignment',
            'fallback'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method translate_translate_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'source_text' is set
        if self.api_client.client_side_validation and ('source_text' not in local_var_params or  # noqa: E501
                                                        local_var_params['source_text'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `source_text` when calling `translate_translate_get`")  # noqa: E501
        # verify the required parameter 'to_language' is set
        if self.api_client.client_side_validation and ('to_language' not in local_var_params or  # noqa: E501
                                                        local_var_params['to_language'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_language` when calling `translate_translate_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('to_language' in local_var_params and  # noqa: E501
                                                        len(local_var_params['to_language']) > 2):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `to_language` when calling `translate_translate_get`, length must be less than or equal to `2`")  # noqa: E501
        if self.api_client.client_side_validation and ('from_language' in local_var_params and  # noqa: E501
                                                        len(local_var_params['from_language']) > 2):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `from_language` when calling `translate_translate_get`, length must be less than or equal to `2`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source_text' in local_var_params and local_var_params['source_text'] is not None:  # noqa: E501
            query_params.append(('source_text', local_var_params['source_text']))  # noqa: E501
        if 'to_language' in local_var_params and local_var_params['to_language'] is not None:  # noqa: E501
            query_params.append(('to_language', local_var_params['to_language']))  # noqa: E501
        if 'from_language' in local_var_params and local_var_params['from_language'] is not None:  # noqa: E501
            query_params.append(('from_language', local_var_params['from_language']))  # noqa: E501
        if 'preferred_engine' in local_var_params and local_var_params['preferred_engine'] is not None:  # noqa: E501
            query_params.append(('preferred_engine', local_var_params['preferred_engine']))  # noqa: E501
        if 'with_alignment' in local_var_params and local_var_params['with_alignment'] is not None:  # noqa: E501
            query_params.append(('with_alignment', local_var_params['with_alignment']))  # noqa: E501
        if 'fallback' in local_var_params and local_var_params['fallback'] is not None:  # noqa: E501
            query_params.append(('fallback', local_var_params['fallback']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/translate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TranslationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
