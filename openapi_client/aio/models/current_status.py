# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.10   3Di core release: 2.0.10  deployed on:  09:44AM (UTC) on July 02, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.aio.configuration import Configuration


class CurrentStatus(object):
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
        'created': 'datetime',
        'time': 'float',
        'paused': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created': 'created',
        'time': 'time',
        'paused': 'paused'
    }

    def __init__(self, id=None, name=None, created=None, time=None, paused=None, local_vars_configuration=None):  # noqa: E501
        """CurrentStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._created = None
        self._time = None
        self._paused = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.created = created
        if time is not None:
            self.time = time
        if paused is not None:
            self.paused = paused

    @property
    def id(self):
        """Gets the id of this CurrentStatus.  # noqa: E501


        :return: The id of this CurrentStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrentStatus.


        :param id: The id of this CurrentStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this CurrentStatus.  # noqa: E501


        :return: The name of this CurrentStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CurrentStatus.


        :param name: The name of this CurrentStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def created(self):
        """Gets the created of this CurrentStatus.  # noqa: E501


        :return: The created of this CurrentStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CurrentStatus.


        :param created: The created of this CurrentStatus.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def time(self):
        """Gets the time of this CurrentStatus.  # noqa: E501


        :return: The time of this CurrentStatus.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this CurrentStatus.


        :param time: The time of this CurrentStatus.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def paused(self):
        """Gets the paused of this CurrentStatus.  # noqa: E501


        :return: The paused of this CurrentStatus.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this CurrentStatus.


        :param paused: The paused of this CurrentStatus.  # noqa: E501
        :type: bool
        """

        self._paused = paused

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
        if not isinstance(other, CurrentStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrentStatus):
            return True

        return self.to_dict() != other.to_dict()
