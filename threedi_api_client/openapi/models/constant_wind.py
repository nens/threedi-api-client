# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 1.0.61   3Di core release: 2.1.2  deployed on:  07:26AM (UTC) on August 17, 2021  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from threedi_api_client.openapi.configuration import Configuration


class ConstantWind(object):
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
        'uid': 'str',
        'url': 'str',
        'simulation': 'str',
        'offset': 'int',
        'duration': 'int',
        'values': 'list[list[float]]',
        'units': 'str',
        'speed_interpolate': 'bool',
        'speed_constant': 'bool',
        'direction_interpolate': 'bool',
        'direction_constant': 'bool',
        'speed_value': 'float',
        'direction_value': 'int'
    }

    attribute_map = {
        'id': 'id',
        'uid': 'uid',
        'url': 'url',
        'simulation': 'simulation',
        'offset': 'offset',
        'duration': 'duration',
        'values': 'values',
        'units': 'units',
        'speed_interpolate': 'speed_interpolate',
        'speed_constant': 'speed_constant',
        'direction_interpolate': 'direction_interpolate',
        'direction_constant': 'direction_constant',
        'speed_value': 'speed_value',
        'direction_value': 'direction_value'
    }

    def __init__(self, id=None, uid=None, url=None, simulation=None, offset=None, duration=None, values=None, units=None, speed_interpolate=None, speed_constant=None, direction_interpolate=None, direction_constant=None, speed_value=None, direction_value=None, local_vars_configuration=None):  # noqa: E501
        """ConstantWind - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._uid = None
        self._url = None
        self._simulation = None
        self._offset = None
        self._duration = None
        self._values = None
        self._units = None
        self._speed_interpolate = None
        self._speed_constant = None
        self._direction_interpolate = None
        self._direction_constant = None
        self._speed_value = None
        self._direction_value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uid is not None:
            self.uid = uid
        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        self.duration = duration
        if values is not None:
            self.values = values
        if units is not None:
            self.units = units
        if speed_interpolate is not None:
            self.speed_interpolate = speed_interpolate
        if speed_constant is not None:
            self.speed_constant = speed_constant
        if direction_interpolate is not None:
            self.direction_interpolate = direction_interpolate
        if direction_constant is not None:
            self.direction_constant = direction_constant
        if speed_value is not None:
            self.speed_value = speed_value
        if direction_value is not None:
            self.direction_value = direction_value

    @property
    def id(self):
        """Gets the id of this ConstantWind.  # noqa: E501


        :return: The id of this ConstantWind.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConstantWind.


        :param id: The id of this ConstantWind.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uid(self):
        """Gets the uid of this ConstantWind.  # noqa: E501


        :return: The uid of this ConstantWind.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ConstantWind.


        :param uid: The uid of this ConstantWind.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def url(self):
        """Gets the url of this ConstantWind.  # noqa: E501


        :return: The url of this ConstantWind.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ConstantWind.


        :param url: The url of this ConstantWind.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this ConstantWind.  # noqa: E501


        :return: The simulation of this ConstantWind.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this ConstantWind.


        :param simulation: The simulation of this ConstantWind.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this ConstantWind.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this ConstantWind.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ConstantWind.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this ConstantWind.  # noqa: E501
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
        """Gets the duration of this ConstantWind.  # noqa: E501

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :return: The duration of this ConstantWind.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ConstantWind.

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :param duration: The duration of this ConstantWind.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._duration = duration

    @property
    def values(self):
        """Gets the values of this ConstantWind.  # noqa: E501

        [time, speed, direction]  # noqa: E501

        :return: The values of this ConstantWind.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ConstantWind.

        [time, speed, direction]  # noqa: E501

        :param values: The values of this ConstantWind.  # noqa: E501
        :type: list[list[float]]
        """

        self._values = values

    @property
    def units(self):
        """Gets the units of this ConstantWind.  # noqa: E501

        wind speed unit (default 'm/s')  # noqa: E501

        :return: The units of this ConstantWind.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this ConstantWind.

        wind speed unit (default 'm/s')  # noqa: E501

        :param units: The units of this ConstantWind.  # noqa: E501
        :type: str
        """
        allowed_values = ["m/s", "km/h"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and units not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

    @property
    def speed_interpolate(self):
        """Gets the speed_interpolate of this ConstantWind.  # noqa: E501

        interpolate wind speed  # noqa: E501

        :return: The speed_interpolate of this ConstantWind.  # noqa: E501
        :rtype: bool
        """
        return self._speed_interpolate

    @speed_interpolate.setter
    def speed_interpolate(self, speed_interpolate):
        """Sets the speed_interpolate of this ConstantWind.

        interpolate wind speed  # noqa: E501

        :param speed_interpolate: The speed_interpolate of this ConstantWind.  # noqa: E501
        :type: bool
        """

        self._speed_interpolate = speed_interpolate

    @property
    def speed_constant(self):
        """Gets the speed_constant of this ConstantWind.  # noqa: E501

        constant wind speed  # noqa: E501

        :return: The speed_constant of this ConstantWind.  # noqa: E501
        :rtype: bool
        """
        return self._speed_constant

    @speed_constant.setter
    def speed_constant(self, speed_constant):
        """Sets the speed_constant of this ConstantWind.

        constant wind speed  # noqa: E501

        :param speed_constant: The speed_constant of this ConstantWind.  # noqa: E501
        :type: bool
        """

        self._speed_constant = speed_constant

    @property
    def direction_interpolate(self):
        """Gets the direction_interpolate of this ConstantWind.  # noqa: E501

        interpolate wind direction  # noqa: E501

        :return: The direction_interpolate of this ConstantWind.  # noqa: E501
        :rtype: bool
        """
        return self._direction_interpolate

    @direction_interpolate.setter
    def direction_interpolate(self, direction_interpolate):
        """Sets the direction_interpolate of this ConstantWind.

        interpolate wind direction  # noqa: E501

        :param direction_interpolate: The direction_interpolate of this ConstantWind.  # noqa: E501
        :type: bool
        """

        self._direction_interpolate = direction_interpolate

    @property
    def direction_constant(self):
        """Gets the direction_constant of this ConstantWind.  # noqa: E501

        constant wind direction  # noqa: E501

        :return: The direction_constant of this ConstantWind.  # noqa: E501
        :rtype: bool
        """
        return self._direction_constant

    @direction_constant.setter
    def direction_constant(self, direction_constant):
        """Sets the direction_constant of this ConstantWind.

        constant wind direction  # noqa: E501

        :param direction_constant: The direction_constant of this ConstantWind.  # noqa: E501
        :type: bool
        """

        self._direction_constant = direction_constant

    @property
    def speed_value(self):
        """Gets the speed_value of this ConstantWind.  # noqa: E501

        constant wind speed  # noqa: E501

        :return: The speed_value of this ConstantWind.  # noqa: E501
        :rtype: float
        """
        return self._speed_value

    @speed_value.setter
    def speed_value(self, speed_value):
        """Sets the speed_value of this ConstantWind.

        constant wind speed  # noqa: E501

        :param speed_value: The speed_value of this ConstantWind.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                speed_value is not None and speed_value < 0):  # noqa: E501
            raise ValueError("Invalid value for `speed_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._speed_value = speed_value

    @property
    def direction_value(self):
        """Gets the direction_value of this ConstantWind.  # noqa: E501

        constant wind direction in degrees (0-360) from north - meteorological standard (thus, 180 is a southern wind)  # noqa: E501

        :return: The direction_value of this ConstantWind.  # noqa: E501
        :rtype: int
        """
        return self._direction_value

    @direction_value.setter
    def direction_value(self, direction_value):
        """Sets the direction_value of this ConstantWind.

        constant wind direction in degrees (0-360) from north - meteorological standard (thus, 180 is a southern wind)  # noqa: E501

        :param direction_value: The direction_value of this ConstantWind.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                direction_value is not None and direction_value > 360):  # noqa: E501
            raise ValueError("Invalid value for `direction_value`, must be a value less than or equal to `360`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                direction_value is not None and direction_value < 0):  # noqa: E501
            raise ValueError("Invalid value for `direction_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._direction_value = direction_value

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
        if not isinstance(other, ConstantWind):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConstantWind):
            return True

        return self.to_dict() != other.to_dict()
