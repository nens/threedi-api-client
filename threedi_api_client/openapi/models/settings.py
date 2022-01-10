# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.7.0   3Di core release: 2.2.2  deployed on:  01:00PM (UTC) on January 10, 2022  # noqa: E501

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

class Settings(object):
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
        'damage_estimation': 'DamageEstimation'
    }

    attribute_map = {
        'damage_estimation': 'damage_estimation'
    }

    def __init__(self, damage_estimation=None, local_vars_configuration=None):  # noqa: E501
        """Settings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._damage_estimation = None
        self.discriminator = None

        if damage_estimation is not None:
            self.damage_estimation = damage_estimation

    @property
    def damage_estimation(self):
        """Gets the damage_estimation of this Settings.  # noqa: E501


        :return: The damage_estimation of this Settings.  # noqa: E501
        :rtype: DamageEstimation
        """
        return self._damage_estimation

    @damage_estimation.setter
    def damage_estimation(self, damage_estimation):
        """Sets the damage_estimation of this Settings.


        :param damage_estimation: The damage_estimation of this Settings.  # noqa: E501
        :type: DamageEstimation
        """

        self._damage_estimation = damage_estimation

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
        if not isinstance(other, Settings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Settings):
            return True

        return self.to_dict() != other.to_dict()
