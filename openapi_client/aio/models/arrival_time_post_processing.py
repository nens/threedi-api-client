# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.8   3Di core release: 2.0.9  deployed on:  12:56PM (UTC) on June 22, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.aio.configuration import Configuration


class ArrivalTimePostProcessing(object):
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
        'basic_post_processing': 'int'
    }

    attribute_map = {
        'basic_post_processing': 'basic_post_processing'
    }

    def __init__(self, basic_post_processing=None, local_vars_configuration=None):  # noqa: E501
        """ArrivalTimePostProcessing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._basic_post_processing = None
        self.discriminator = None

        if basic_post_processing is not None:
            self.basic_post_processing = basic_post_processing

    @property
    def basic_post_processing(self):
        """Gets the basic_post_processing of this ArrivalTimePostProcessing.  # noqa: E501


        :return: The basic_post_processing of this ArrivalTimePostProcessing.  # noqa: E501
        :rtype: int
        """
        return self._basic_post_processing

    @basic_post_processing.setter
    def basic_post_processing(self, basic_post_processing):
        """Sets the basic_post_processing of this ArrivalTimePostProcessing.


        :param basic_post_processing: The basic_post_processing of this ArrivalTimePostProcessing.  # noqa: E501
        :type: int
        """

        self._basic_post_processing = basic_post_processing

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
        if not isinstance(other, ArrivalTimePostProcessing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArrivalTimePostProcessing):
            return True

        return self.to_dict() != other.to_dict()
