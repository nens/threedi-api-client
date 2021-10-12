# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 1.0.64   3Di core release: 2.1.2  deployed on:  03:05PM (UTC) on September 15, 2021  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from threedi_api_client.openapi.configuration import Configuration


class TimeseriesRainOverview(object):
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
        'simulation': 'str',
        'offset': 'int',
        'duration': 'int',
        'interpolate': 'bool',
        'values': 'list[list[float]]',
        'units': 'str',
        'constant': 'bool',
        'uid': 'str',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'offset': 'offset',
        'duration': 'duration',
        'interpolate': 'interpolate',
        'values': 'values',
        'units': 'units',
        'constant': 'constant',
        'uid': 'uid',
        'id': 'id'
    }

    def __init__(self, url=None, simulation=None, offset=None, duration=None, interpolate=None, values=None, units=None, constant=None, uid=None, id=None, local_vars_configuration=None):  # noqa: E501
        """TimeseriesRainOverview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._simulation = None
        self._offset = None
        self._duration = None
        self._interpolate = None
        self._values = None
        self._units = None
        self._constant = None
        self._uid = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        if duration is not None:
            self.duration = duration
        if interpolate is not None:
            self.interpolate = interpolate
        self.values = values
        self.units = units
        if constant is not None:
            self.constant = constant
        if uid is not None:
            self.uid = uid
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this TimeseriesRainOverview.  # noqa: E501


        :return: The url of this TimeseriesRainOverview.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TimeseriesRainOverview.


        :param url: The url of this TimeseriesRainOverview.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this TimeseriesRainOverview.  # noqa: E501


        :return: The simulation of this TimeseriesRainOverview.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this TimeseriesRainOverview.


        :param simulation: The simulation of this TimeseriesRainOverview.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this TimeseriesRainOverview.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this TimeseriesRainOverview.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TimeseriesRainOverview.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this TimeseriesRainOverview.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def duration(self):
        """Gets the duration of this TimeseriesRainOverview.  # noqa: E501

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :return: The duration of this TimeseriesRainOverview.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TimeseriesRainOverview.

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :param duration: The duration of this TimeseriesRainOverview.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def interpolate(self):
        """Gets the interpolate of this TimeseriesRainOverview.  # noqa: E501


        :return: The interpolate of this TimeseriesRainOverview.  # noqa: E501
        :rtype: bool
        """
        return self._interpolate

    @interpolate.setter
    def interpolate(self, interpolate):
        """Sets the interpolate of this TimeseriesRainOverview.


        :param interpolate: The interpolate of this TimeseriesRainOverview.  # noqa: E501
        :type: bool
        """

        self._interpolate = interpolate

    @property
    def values(self):
        """Gets the values of this TimeseriesRainOverview.  # noqa: E501

        Timeseries provided as a nested list. The inner list consists of exactly 2 values: timestamp, value  # noqa: E501

        :return: The values of this TimeseriesRainOverview.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TimeseriesRainOverview.

        Timeseries provided as a nested list. The inner list consists of exactly 2 values: timestamp, value  # noqa: E501

        :param values: The values of this TimeseriesRainOverview.  # noqa: E501
        :type: list[list[float]]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def units(self):
        """Gets the units of this TimeseriesRainOverview.  # noqa: E501

        m/s is only option for now  # noqa: E501

        :return: The units of this TimeseriesRainOverview.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this TimeseriesRainOverview.

        m/s is only option for now  # noqa: E501

        :param units: The units of this TimeseriesRainOverview.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and units is None:  # noqa: E501
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501
        allowed_values = ["m/s"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and units not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

    @property
    def constant(self):
        """Gets the constant of this TimeseriesRainOverview.  # noqa: E501


        :return: The constant of this TimeseriesRainOverview.  # noqa: E501
        :rtype: bool
        """
        return self._constant

    @constant.setter
    def constant(self, constant):
        """Sets the constant of this TimeseriesRainOverview.


        :param constant: The constant of this TimeseriesRainOverview.  # noqa: E501
        :type: bool
        """

        self._constant = constant

    @property
    def uid(self):
        """Gets the uid of this TimeseriesRainOverview.  # noqa: E501


        :return: The uid of this TimeseriesRainOverview.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this TimeseriesRainOverview.


        :param uid: The uid of this TimeseriesRainOverview.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def id(self):
        """Gets the id of this TimeseriesRainOverview.  # noqa: E501


        :return: The id of this TimeseriesRainOverview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimeseriesRainOverview.


        :param id: The id of this TimeseriesRainOverview.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, TimeseriesRainOverview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeseriesRainOverview):
            return True

        return self.to_dict() != other.to_dict()
