# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.16   3Di core release: 2.0.11  deployed on:  07:33AM (UTC) on September 04, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Tokens(object):
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
    openapi_types = {"access": "str", "refresh": "str"}

    attribute_map = {"access": "access", "refresh": "refresh"}

    def __init__(
        self, access=None, refresh=None, local_vars_configuration=None
    ):  # noqa: E501
        """Tokens - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access = None
        self._refresh = None
        self.discriminator = None

        if access is not None:
            self.access = access
        if refresh is not None:
            self.refresh = refresh

    @property
    def access(self):
        """Gets the access of this Tokens.  # noqa: E501


        :return: The access of this Tokens.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this Tokens.


        :param access: The access of this Tokens.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and access is not None
            and len(access) < 1
        ):
            raise ValueError(
                "Invalid value for `access`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._access = access

    @property
    def refresh(self):
        """Gets the refresh of this Tokens.  # noqa: E501


        :return: The refresh of this Tokens.  # noqa: E501
        :rtype: str
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this Tokens.


        :param refresh: The refresh of this Tokens.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and refresh is not None
            and len(refresh) < 1
        ):
            raise ValueError(
                "Invalid value for `refresh`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._refresh = refresh

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, Tokens):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tokens):
            return True

        return self.to_dict() != other.to_dict()
