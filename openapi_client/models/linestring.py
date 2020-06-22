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

from openapi_client.configuration import Configuration


class Linestring(object):
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
        'type': 'str',
        'coordinates': 'list[list[float]]'
    }

    attribute_map = {
        'type': 'type',
        'coordinates': 'coordinates'
    }

    def __init__(self, type='Linestring', coordinates=None, local_vars_configuration=None):  # noqa: E501
        """Linestring - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._coordinates = None
        self.discriminator = None

        self.type = type
        self.coordinates = coordinates

    @property
    def type(self):
        """Gets the type of this Linestring.  # noqa: E501

        Type should always be 'linestring' or 'LINESTRING'  # noqa: E501

        :return: The type of this Linestring.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Linestring.

        Type should always be 'linestring' or 'LINESTRING'  # noqa: E501

        :param type: The type of this Linestring.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def coordinates(self):
        """Gets the coordinates of this Linestring.  # noqa: E501

        List of coordinates  # noqa: E501

        :return: The coordinates of this Linestring.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Linestring.

        List of coordinates  # noqa: E501

        :param coordinates: The coordinates of this Linestring.  # noqa: E501
        :type: list[list[float]]
        """
        if self.local_vars_configuration.client_side_validation and coordinates is None:  # noqa: E501
            raise ValueError("Invalid value for `coordinates`, must not be `None`")  # noqa: E501

        self._coordinates = coordinates

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
        if not isinstance(other, Linestring):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Linestring):
            return True

        return self.to_dict() != other.to_dict()
