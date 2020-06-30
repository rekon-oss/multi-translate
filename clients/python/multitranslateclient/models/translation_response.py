# coding: utf-8

"""
    multi-translate

    Multi-Translate is a unified interface on top of various translate APIs providing optimal translations, persistence, fallback.  # noqa: E501

    The version of the OpenAPI document: 0.2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from multitranslateclient.configuration import Configuration


class TranslationResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'engine': 'str',
        'engine_version': 'str',
        'detected_language_confidence': 'float',
        'from_language': 'str',
        'to_language': 'str',
        'source_text': 'str',
        'translated_text': 'str',
        'alignment': 'list[dict(str, dict(str, str))]'
    }

    attribute_map = {
        'engine': 'engine',
        'engine_version': 'engine_version',
        'detected_language_confidence': 'detected_language_confidence',
        'from_language': 'from_language',
        'to_language': 'to_language',
        'source_text': 'source_text',
        'translated_text': 'translated_text',
        'alignment': 'alignment'
    }

    def __init__(self, engine=None, engine_version=None, detected_language_confidence=None, from_language=None, to_language=None, source_text=None, translated_text=None, alignment=None, local_vars_configuration=None):  # noqa: E501
        """TranslationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._engine = None
        self._engine_version = None
        self._detected_language_confidence = None
        self._from_language = None
        self._to_language = None
        self._source_text = None
        self._translated_text = None
        self._alignment = None
        self.discriminator = None

        self.engine = engine
        self.engine_version = engine_version
        if detected_language_confidence is not None:
            self.detected_language_confidence = detected_language_confidence
        self.from_language = from_language
        self.to_language = to_language
        self.source_text = source_text
        self.translated_text = translated_text
        if alignment is not None:
            self.alignment = alignment

    @property
    def engine(self):
        """Gets the engine of this TranslationResponse.  # noqa: E501


        :return: The engine of this TranslationResponse.  # noqa: E501
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this TranslationResponse.


        :param engine: The engine of this TranslationResponse.  # noqa: E501
        :type engine: str
        """
        if self.local_vars_configuration.client_side_validation and engine is None:  # noqa: E501
            raise ValueError("Invalid value for `engine`, must not be `None`")  # noqa: E501

        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this TranslationResponse.  # noqa: E501


        :return: The engine_version of this TranslationResponse.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this TranslationResponse.


        :param engine_version: The engine_version of this TranslationResponse.  # noqa: E501
        :type engine_version: str
        """
        if self.local_vars_configuration.client_side_validation and engine_version is None:  # noqa: E501
            raise ValueError("Invalid value for `engine_version`, must not be `None`")  # noqa: E501

        self._engine_version = engine_version

    @property
    def detected_language_confidence(self):
        """Gets the detected_language_confidence of this TranslationResponse.  # noqa: E501


        :return: The detected_language_confidence of this TranslationResponse.  # noqa: E501
        :rtype: float
        """
        return self._detected_language_confidence

    @detected_language_confidence.setter
    def detected_language_confidence(self, detected_language_confidence):
        """Sets the detected_language_confidence of this TranslationResponse.


        :param detected_language_confidence: The detected_language_confidence of this TranslationResponse.  # noqa: E501
        :type detected_language_confidence: float
        """

        self._detected_language_confidence = detected_language_confidence

    @property
    def from_language(self):
        """Gets the from_language of this TranslationResponse.  # noqa: E501


        :return: The from_language of this TranslationResponse.  # noqa: E501
        :rtype: str
        """
        return self._from_language

    @from_language.setter
    def from_language(self, from_language):
        """Sets the from_language of this TranslationResponse.


        :param from_language: The from_language of this TranslationResponse.  # noqa: E501
        :type from_language: str
        """
        if self.local_vars_configuration.client_side_validation and from_language is None:  # noqa: E501
            raise ValueError("Invalid value for `from_language`, must not be `None`")  # noqa: E501

        self._from_language = from_language

    @property
    def to_language(self):
        """Gets the to_language of this TranslationResponse.  # noqa: E501


        :return: The to_language of this TranslationResponse.  # noqa: E501
        :rtype: str
        """
        return self._to_language

    @to_language.setter
    def to_language(self, to_language):
        """Sets the to_language of this TranslationResponse.


        :param to_language: The to_language of this TranslationResponse.  # noqa: E501
        :type to_language: str
        """
        if self.local_vars_configuration.client_side_validation and to_language is None:  # noqa: E501
            raise ValueError("Invalid value for `to_language`, must not be `None`")  # noqa: E501

        self._to_language = to_language

    @property
    def source_text(self):
        """Gets the source_text of this TranslationResponse.  # noqa: E501


        :return: The source_text of this TranslationResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_text

    @source_text.setter
    def source_text(self, source_text):
        """Sets the source_text of this TranslationResponse.


        :param source_text: The source_text of this TranslationResponse.  # noqa: E501
        :type source_text: str
        """
        if self.local_vars_configuration.client_side_validation and source_text is None:  # noqa: E501
            raise ValueError("Invalid value for `source_text`, must not be `None`")  # noqa: E501

        self._source_text = source_text

    @property
    def translated_text(self):
        """Gets the translated_text of this TranslationResponse.  # noqa: E501


        :return: The translated_text of this TranslationResponse.  # noqa: E501
        :rtype: str
        """
        return self._translated_text

    @translated_text.setter
    def translated_text(self, translated_text):
        """Sets the translated_text of this TranslationResponse.


        :param translated_text: The translated_text of this TranslationResponse.  # noqa: E501
        :type translated_text: str
        """
        if self.local_vars_configuration.client_side_validation and translated_text is None:  # noqa: E501
            raise ValueError("Invalid value for `translated_text`, must not be `None`")  # noqa: E501

        self._translated_text = translated_text

    @property
    def alignment(self):
        """Gets the alignment of this TranslationResponse.  # noqa: E501


        :return: The alignment of this TranslationResponse.  # noqa: E501
        :rtype: list[dict(str, dict(str, str))]
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this TranslationResponse.


        :param alignment: The alignment of this TranslationResponse.  # noqa: E501
        :type alignment: list[dict(str, dict(str, str))]
        """

        self._alignment = alignment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TranslationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationResponse):
            return True

        return self.to_dict() != other.to_dict()
