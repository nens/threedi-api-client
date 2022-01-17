# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.11.1   3Di core release: 2.2.3  deployed on:  02:06PM (UTC) on January 13, 2022  # noqa: E501

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

class MeasureSpecification(object):
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
        'id': 'int',
        'name': 'str',
        'locations': 'list[MeasureLocation]',
        'variable': 'str',
        'operator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'locations': 'locations',
        'variable': 'variable',
        'operator': 'operator'
    }

    def __init__(self, id=None, name=None, locations=None, variable=None, operator=None, local_vars_configuration=None):  # noqa: E501
        """MeasureSpecification - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._locations = None
        self._variable = None
        self._operator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.locations = locations
        self.variable = variable
        self.operator = operator

    @property
    def id(self):
        """Gets the id of this MeasureSpecification.  # noqa: E501


        :return: The id of this MeasureSpecification.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MeasureSpecification.


        :param id: The id of this MeasureSpecification.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MeasureSpecification.  # noqa: E501


        :return: The name of this MeasureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MeasureSpecification.


        :param name: The name of this MeasureSpecification.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def locations(self):
        """Gets the locations of this MeasureSpecification.  # noqa: E501


        :return: The locations of this MeasureSpecification.  # noqa: E501
        :rtype: list[MeasureLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this MeasureSpecification.


        :param locations: The locations of this MeasureSpecification.  # noqa: E501
        :type: list[MeasureLocation]
        """
        if self.local_vars_configuration.client_side_validation and locations is None:  # noqa: E501
            raise ValueError("Invalid value for `locations`, must not be `None`")  # noqa: E501

        self._locations = locations

    @property
    def variable(self):
        """Gets the variable of this MeasureSpecification.  # noqa: E501

        measurement variable, one of the following options:  s1 (waterlevel) vol1 (volume) q (discharge) u1 (velocity)   # noqa: E501

        :return: The variable of this MeasureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this MeasureSpecification.

        measurement variable, one of the following options:  s1 (waterlevel) vol1 (volume) q (discharge) u1 (velocity)   # noqa: E501

        :param variable: The variable of this MeasureSpecification.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and variable is None:  # noqa: E501
            raise ValueError("Invalid value for `variable`, must not be `None`")  # noqa: E501
        allowed_values = ["s1", "vol1", "q", "u1"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and variable not in allowed_values:  # noqa: E501
            logger.warning(
                "Warning: Unknown value for `variable` ({0}), must be one of {1}. Either your threedi-api-client version is out of date or this value is invalid."  # noqa: E501
                .format(variable, allowed_values)
            )

        self._variable = variable

    @property
    def operator(self):
        """Gets the operator of this MeasureSpecification.  # noqa: E501

        e.g. >, <, >=, <=  # noqa: E501

        :return: The operator of this MeasureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this MeasureSpecification.

        e.g. >, <, >=, <=  # noqa: E501

        :param operator: The operator of this MeasureSpecification.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501
        allowed_values = [">", ">=", "<", "<="]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operator not in allowed_values:  # noqa: E501
            logger.warning(
                "Warning: Unknown value for `operator` ({0}), must be one of {1}. Either your threedi-api-client version is out of date or this value is invalid."  # noqa: E501
                .format(operator, allowed_values)
            )

        self._operator = operator

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
        if not isinstance(other, MeasureSpecification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeasureSpecification):
            return True

        return self.to_dict() != other.to_dict()
