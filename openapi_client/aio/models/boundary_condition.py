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


class BoundaryCondition(object):
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
        'url': 'str',
        'boundary_id': 'int',
        'threedimodel': 'str',
        'type': 'str',
        'dimension': 'str'
    }

    attribute_map = {
        'url': 'url',
        'boundary_id': 'boundary_id',
        'threedimodel': 'threedimodel',
        'type': 'type',
        'dimension': 'dimension'
    }

    def __init__(self, url=None, boundary_id=None, threedimodel=None, type=None, dimension=None, local_vars_configuration=None):  # noqa: E501
        """BoundaryCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._boundary_id = None
        self._threedimodel = None
        self._type = None
        self._dimension = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.boundary_id = boundary_id
        if threedimodel is not None:
            self.threedimodel = threedimodel
        self.type = type
        self.dimension = dimension

    @property
    def url(self):
        """Gets the url of this BoundaryCondition.  # noqa: E501


        :return: The url of this BoundaryCondition.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BoundaryCondition.


        :param url: The url of this BoundaryCondition.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def boundary_id(self):
        """Gets the boundary_id of this BoundaryCondition.  # noqa: E501


        :return: The boundary_id of this BoundaryCondition.  # noqa: E501
        :rtype: int
        """
        return self._boundary_id

    @boundary_id.setter
    def boundary_id(self, boundary_id):
        """Sets the boundary_id of this BoundaryCondition.


        :param boundary_id: The boundary_id of this BoundaryCondition.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and boundary_id is None:  # noqa: E501
            raise ValueError("Invalid value for `boundary_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                boundary_id is not None and boundary_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `boundary_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                boundary_id is not None and boundary_id < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `boundary_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._boundary_id = boundary_id

    @property
    def threedimodel(self):
        """Gets the threedimodel of this BoundaryCondition.  # noqa: E501


        :return: The threedimodel of this BoundaryCondition.  # noqa: E501
        :rtype: str
        """
        return self._threedimodel

    @threedimodel.setter
    def threedimodel(self, threedimodel):
        """Sets the threedimodel of this BoundaryCondition.


        :param threedimodel: The threedimodel of this BoundaryCondition.  # noqa: E501
        :type: str
        """

        self._threedimodel = threedimodel

    @property
    def type(self):
        """Gets the type of this BoundaryCondition.  # noqa: E501


        :return: The type of this BoundaryCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BoundaryCondition.


        :param type: The type of this BoundaryCondition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["velocity", "sommerfeldt", "riemann", "water_level", "discharge"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def dimension(self):
        """Gets the dimension of this BoundaryCondition.  # noqa: E501


        :return: The dimension of this BoundaryCondition.  # noqa: E501
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this BoundaryCondition.


        :param dimension: The dimension of this BoundaryCondition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dimension is None:  # noqa: E501
            raise ValueError("Invalid value for `dimension`, must not be `None`")  # noqa: E501
        allowed_values = ["one_d", "two_d"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dimension not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dimension` ({0}), must be one of {1}"  # noqa: E501
                .format(dimension, allowed_values)
            )

        self._dimension = dimension

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
        if not isinstance(other, BoundaryCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoundaryCondition):
            return True

        return self.to_dict() != other.to_dict()
