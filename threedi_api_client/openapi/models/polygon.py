# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.2.65   3Di core release: 3.2.1  deployed on:  12:21PM (UTC) on October 03, 2023  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import logging
import pprint
import re  # noqa: F401

import six

from threedi_api_client.openapi.configuration import Configuration

logger = logging.getLogger(__name__)

class Polygon(object):
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
        'coordinates': 'list[list[list[float]]]'
    }

    attribute_map = {
        'type': 'type',
        'coordinates': 'coordinates'
    }

    def __init__(self, type='Polygon', coordinates=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """Polygon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._type = None
        self._coordinates = None
        self.discriminator = None

        self.type = type
        self.coordinates = coordinates

    @property
    def type(self):
        """Gets the type of this Polygon.  # noqa: E501

        Type should always be 'Polygon'  # noqa: E501

        :return: The type of this Polygon.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Polygon.

        Type should always be 'Polygon'  # noqa: E501

        :param type: The type of this Polygon.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def coordinates(self):
        """Gets the coordinates of this Polygon.  # noqa: E501

        List of coordinates (longitude, latitude order)  # noqa: E501

        :return: The coordinates of this Polygon.  # noqa: E501
        :rtype: list[list[list[float]]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Polygon.

        List of coordinates (longitude, latitude order)  # noqa: E501

        :param coordinates: The coordinates of this Polygon.  # noqa: E501
        :type: list[list[list[float]]]
        """
        if self.local_vars_configuration.client_side_validation and coordinates is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `coordinates`, must not be `None`")  # noqa: E501

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

    def __handle_validation_error(self, message):
        # Only raise ValueError when not fetched from API
        from threedi_api_client import __version__ as VERSION

        if not self._fetched_from_api:
            raise ValueError(message + f" It is possible that the current threedi-api-client version ({VERSION}) is out of date: consult https://pypi.org/project/threedi-api-client/ and consider upgrading.")  # noqa: E501
        logger.warning(message + " Please update to the latest threedi-api-client version.")  # noqa: E501

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Polygon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Polygon):
            return True

        return self.to_dict() != other.to_dict()
