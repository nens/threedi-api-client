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


class Action(object):
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
        "name": "str",
        "duration": "int",
        "timeout": "int",
        "max_rate": "float",
    }

    attribute_map = {
        "name": "name",
        "duration": "duration",
        "timeout": "timeout",
        "max_rate": "max_rate",
    }

    def __init__(
        self,
        name=None,
        duration=None,
        timeout=None,
        max_rate=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Action - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._duration = None
        self._timeout = None
        self._max_rate = None
        self.discriminator = None

        self.name = name
        if duration is not None:
            self.duration = duration
        if timeout is not None:
            self.timeout = timeout
        if max_rate is not None:
            self.max_rate = max_rate

    @property
    def name(self):
        """Gets the name of this Action.  # noqa: E501


        :return: The name of this Action.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Action.


        :param name: The name of this Action.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "initialize",
            "start",
            "pause",
            "shutdown",
            "queue",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and name not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}".format(  # noqa: E501
                    name, allowed_values
                )
            )

        self._name = name

    @property
    def duration(self):
        """Gets the duration of this Action.  # noqa: E501

        Only valid for name='start'. Run simulation for given duration (in seconds) and pause  # noqa: E501

        :return: The duration of this Action.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Action.

        Only valid for name='start'. Run simulation for given duration (in seconds) and pause  # noqa: E501

        :param duration: The duration of this Action.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and duration is not None
            and duration < 1
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `duration`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._duration = duration

    @property
    def timeout(self):
        """Gets the timeout of this Action.  # noqa: E501

        Only valid for name='pause'. Remove simulation after given timeout (in seconds). Defaults to 300 seconds  # noqa: E501

        :return: The timeout of this Action.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Action.

        Only valid for name='pause'. Remove simulation after given timeout (in seconds). Defaults to 300 seconds  # noqa: E501

        :param timeout: The timeout of this Action.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and timeout is not None
            and timeout < 30
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `timeout`, must be a value greater than or equal to `30`"
            )  # noqa: E501

        self._timeout = timeout

    @property
    def max_rate(self):
        """Gets the max_rate of this Action.  # noqa: E501

        Only valid for name='start'. Limit maximum speed of the simulation. The max_rate is a multiplier relative to real time For example max_rate '60' means max 60 simulation seconds in 1 real second   # noqa: E501

        :return: The max_rate of this Action.  # noqa: E501
        :rtype: float
        """
        return self._max_rate

    @max_rate.setter
    def max_rate(self, max_rate):
        """Sets the max_rate of this Action.

        Only valid for name='start'. Limit maximum speed of the simulation. The max_rate is a multiplier relative to real time For example max_rate '60' means max 60 simulation seconds in 1 real second   # noqa: E501

        :param max_rate: The max_rate of this Action.  # noqa: E501
        :type: float
        """
        if (
            self.local_vars_configuration.client_side_validation
            and max_rate is not None
            and max_rate < 1
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `max_rate`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._max_rate = max_rate

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
        if not isinstance(other, Action):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Action):
            return True

        return self.to_dict() != other.to_dict()
