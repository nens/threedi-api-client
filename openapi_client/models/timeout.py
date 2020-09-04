# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.15   3Di core release: 2.0.11  deployed on:  12:24PM (UTC) on September 02, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Timeout(object):
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
        'timeout': 'int'
    }

    attribute_map = {
        'timeout': 'timeout'
    }

    def __init__(self, timeout=None, local_vars_configuration=None):  # noqa: E501
        """Timeout - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timeout = None
        self.discriminator = None

        self.timeout = timeout

    @property
    def timeout(self):
        """Gets the timeout of this Timeout.  # noqa: E501

        Only valid for when the simulation is paused. Reset the simulation timeout to the given value. Defaults to 300 seconds  # noqa: E501

        :return: The timeout of this Timeout.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Timeout.

        Only valid for when the simulation is paused. Reset the simulation timeout to the given value. Defaults to 300 seconds  # noqa: E501

        :param timeout: The timeout of this Timeout.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timeout is None:  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                timeout is not None and timeout < 30):  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `30`")  # noqa: E501

        self._timeout = timeout

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
        if not isinstance(other, Timeout):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Timeout):
            return True

        return self.to_dict() != other.to_dict()