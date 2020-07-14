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


class FileMeta(object):
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
        'values_reference': 'str',
        'units': 'str',
        'timestamps': 'list[int]',
        'offset': 'int',
        'duration': 'int',
        'geotransform': 'list[float]',
        'epsg_code': 'int',
        'interval': 'int',
        'error': 'str',
        'fill_value': 'str'
    }

    attribute_map = {
        'values_reference': 'values_reference',
        'units': 'units',
        'timestamps': 'timestamps',
        'offset': 'offset',
        'duration': 'duration',
        'geotransform': 'geotransform',
        'epsg_code': 'epsg_code',
        'interval': 'interval',
        'error': 'error',
        'fill_value': 'fill_value'
    }

    def __init__(self, values_reference=None, units=None, timestamps=None, offset=None, duration=None, geotransform=None, epsg_code=None, interval=None, error=None, fill_value=None, local_vars_configuration=None):  # noqa: E501
        """FileMeta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._values_reference = None
        self._units = None
        self._timestamps = None
        self._offset = None
        self._duration = None
        self._geotransform = None
        self._epsg_code = None
        self._interval = None
        self._error = None
        self._fill_value = None
        self.discriminator = None

        if values_reference is not None:
            self.values_reference = values_reference
        if units is not None:
            self.units = units
        if timestamps is not None:
            self.timestamps = timestamps
        if offset is not None:
            self.offset = offset
        if duration is not None:
            self.duration = duration
        if geotransform is not None:
            self.geotransform = geotransform
        if epsg_code is not None:
            self.epsg_code = epsg_code
        if interval is not None:
            self.interval = interval
        if error is not None:
            self.error = error
        if fill_value is not None:
            self.fill_value = fill_value

    @property
    def values_reference(self):
        """Gets the values_reference of this FileMeta.  # noqa: E501


        :return: The values_reference of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._values_reference

    @values_reference.setter
    def values_reference(self, values_reference):
        """Sets the values_reference of this FileMeta.


        :param values_reference: The values_reference of this FileMeta.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                values_reference is not None and len(values_reference) > 255):
            raise ValueError("Invalid value for `values_reference`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                values_reference is not None and len(values_reference) < 1):
            raise ValueError("Invalid value for `values_reference`, length must be greater than or equal to `1`")  # noqa: E501

        self._values_reference = values_reference

    @property
    def units(self):
        """Gets the units of this FileMeta.  # noqa: E501


        :return: The units of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this FileMeta.


        :param units: The units of this FileMeta.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                units is not None and len(units) > 64):
            raise ValueError("Invalid value for `units`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                units is not None and len(units) < 1):
            raise ValueError("Invalid value for `units`, length must be greater than or equal to `1`")  # noqa: E501

        self._units = units

    @property
    def timestamps(self):
        """Gets the timestamps of this FileMeta.  # noqa: E501

        seconds in the simulation  # noqa: E501

        :return: The timestamps of this FileMeta.  # noqa: E501
        :rtype: list[int]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this FileMeta.

        seconds in the simulation  # noqa: E501

        :param timestamps: The timestamps of this FileMeta.  # noqa: E501
        :type: list[int]
        """

        self._timestamps = timestamps

    @property
    def offset(self):
        """Gets the offset of this FileMeta.  # noqa: E501

        seconds in the simulation  # noqa: E501

        :return: The offset of this FileMeta.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this FileMeta.

        seconds in the simulation  # noqa: E501

        :param offset: The offset of this FileMeta.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def duration(self):
        """Gets the duration of this FileMeta.  # noqa: E501

        seconds  # noqa: E501

        :return: The duration of this FileMeta.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this FileMeta.

        seconds  # noqa: E501

        :param duration: The duration of this FileMeta.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration < 0):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration = duration

    @property
    def geotransform(self):
        """Gets the geotransform of this FileMeta.  # noqa: E501


        :return: The geotransform of this FileMeta.  # noqa: E501
        :rtype: list[float]
        """
        return self._geotransform

    @geotransform.setter
    def geotransform(self, geotransform):
        """Sets the geotransform of this FileMeta.


        :param geotransform: The geotransform of this FileMeta.  # noqa: E501
        :type: list[float]
        """

        self._geotransform = geotransform

    @property
    def epsg_code(self):
        """Gets the epsg_code of this FileMeta.  # noqa: E501


        :return: The epsg_code of this FileMeta.  # noqa: E501
        :rtype: int
        """
        return self._epsg_code

    @epsg_code.setter
    def epsg_code(self, epsg_code):
        """Sets the epsg_code of this FileMeta.


        :param epsg_code: The epsg_code of this FileMeta.  # noqa: E501
        :type: int
        """

        self._epsg_code = epsg_code

    @property
    def interval(self):
        """Gets the interval of this FileMeta.  # noqa: E501


        :return: The interval of this FileMeta.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this FileMeta.


        :param interval: The interval of this FileMeta.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def error(self):
        """Gets the error of this FileMeta.  # noqa: E501


        :return: The error of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this FileMeta.


        :param error: The error of this FileMeta.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                error is not None and len(error) > 512):
            raise ValueError("Invalid value for `error`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                error is not None and len(error) < 1):
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `1`")  # noqa: E501

        self._error = error

    @property
    def fill_value(self):
        """Gets the fill_value of this FileMeta.  # noqa: E501


        :return: The fill_value of this FileMeta.  # noqa: E501
        :rtype: str
        """
        return self._fill_value

    @fill_value.setter
    def fill_value(self, fill_value):
        """Sets the fill_value of this FileMeta.


        :param fill_value: The fill_value of this FileMeta.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                fill_value is not None and len(fill_value) > 128):
            raise ValueError("Invalid value for `fill_value`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fill_value is not None and len(fill_value) < 1):
            raise ValueError("Invalid value for `fill_value`, length must be greater than or equal to `1`")  # noqa: E501

        self._fill_value = fill_value

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
        if not isinstance(other, FileMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileMeta):
            return True

        return self.to_dict() != other.to_dict()