# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.15.1   3Di core release: 2.2.4  deployed on:  01:07PM (UTC) on January 26, 2022  # noqa: E501

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

class CreateRevision(object):
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
        'empty': 'bool',
        'number': 'int',
        'created': 'datetime'
    }

    attribute_map = {
        'empty': 'empty',
        'number': 'number',
        'created': 'created'
    }

    def __init__(self, empty=False, number=None, created=None, local_vars_configuration=None):  # noqa: E501
        """CreateRevision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._empty = None
        self._number = None
        self._created = None
        self.discriminator = None

        if empty is not None:
            self.empty = empty
        if number is not None:
            self.number = number
        if created is not None:
            self.created = created

    @property
    def empty(self):
        """Gets the empty of this CreateRevision.  # noqa: E501

        Create an empty revision  # noqa: E501

        :return: The empty of this CreateRevision.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this CreateRevision.

        Create an empty revision  # noqa: E501

        :param empty: The empty of this CreateRevision.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def number(self):
        """Gets the number of this CreateRevision.  # noqa: E501

        An optional revision number (only superusers can modify)  # noqa: E501

        :return: The number of this CreateRevision.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreateRevision.

        An optional revision number (only superusers can modify)  # noqa: E501

        :param number: The number of this CreateRevision.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def created(self):
        """Gets the created of this CreateRevision.  # noqa: E501

        An optional creation datetime (only superusers can modify)  # noqa: E501

        :return: The created of this CreateRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CreateRevision.

        An optional creation datetime (only superusers can modify)  # noqa: E501

        :param created: The created of this CreateRevision.  # noqa: E501
        :type: datetime
        """

        self._created = created

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
        if not isinstance(other, CreateRevision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateRevision):
            return True

        return self.to_dict() != other.to_dict()
