# coding: utf-8

"""
    3DI API

    3DI simulation API   Framework release: 0.0.16   3Di core release: 2.0.2  deployed on:  03:33PM (UTC) on October 29, 2019  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FileRasterSourcesSinks(object):
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
        'multiplier': 'float',
        'simulation': 'str',
        'offset': 'int',
        'duration': 'int',
        'timestamps': 'list[int]',
        'interval': 'int',
        'values_reference': 'str',
        'fill_value': 'str',
        'units': 'str',
        'geotransform': 'list[float]',
        'epsg_code': 'int',
        'file': 'FileReadOnly',
        'type': 'str'
    }

    attribute_map = {
        'url': 'url',
        'multiplier': 'multiplier',
        'simulation': 'simulation',
        'offset': 'offset',
        'duration': 'duration',
        'timestamps': 'timestamps',
        'interval': 'interval',
        'values_reference': 'values_reference',
        'fill_value': 'fill_value',
        'units': 'units',
        'geotransform': 'geotransform',
        'epsg_code': 'epsg_code',
        'file': 'file',
        'type': 'type'
    }

    def __init__(self, url=None, multiplier=None, simulation=None, offset=None, duration=None, timestamps=None, interval=None, values_reference=None, fill_value=None, units=None, geotransform=None, epsg_code=None, file=None, type=None):  # noqa: E501
        """FileRasterSourcesSinks - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._multiplier = None
        self._simulation = None
        self._offset = None
        self._duration = None
        self._timestamps = None
        self._interval = None
        self._values_reference = None
        self._fill_value = None
        self._units = None
        self._geotransform = None
        self._epsg_code = None
        self._file = None
        self._type = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if multiplier is not None:
            self.multiplier = multiplier
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        self.duration = duration
        self.timestamps = timestamps
        self.interval = interval
        self.values_reference = values_reference
        if fill_value is not None:
            self.fill_value = fill_value
        self.units = units
        if geotransform is not None:
            self.geotransform = geotransform
        if epsg_code is not None:
            self.epsg_code = epsg_code
        if file is not None:
            self.file = file
        if type is not None:
            self.type = type

    @property
    def url(self):
        """Gets the url of this FileRasterSourcesSinks.  # noqa: E501


        :return: The url of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FileRasterSourcesSinks.


        :param url: The url of this FileRasterSourcesSinks.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def multiplier(self):
        """Gets the multiplier of this FileRasterSourcesSinks.  # noqa: E501


        :return: The multiplier of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this FileRasterSourcesSinks.


        :param multiplier: The multiplier of this FileRasterSourcesSinks.  # noqa: E501
        :type: float
        """

        self._multiplier = multiplier

    @property
    def simulation(self):
        """Gets the simulation of this FileRasterSourcesSinks.  # noqa: E501


        :return: The simulation of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this FileRasterSourcesSinks.


        :param simulation: The simulation of this FileRasterSourcesSinks.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this FileRasterSourcesSinks.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this FileRasterSourcesSinks.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this FileRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if offset is not None and offset > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if offset is not None and offset < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._offset = offset

    @property
    def duration(self):
        """Gets the duration of this FileRasterSourcesSinks.  # noqa: E501

        Duration of event in seconds  # noqa: E501

        :return: The duration of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this FileRasterSourcesSinks.

        Duration of event in seconds  # noqa: E501

        :param duration: The duration of this FileRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if duration is not None and duration > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if duration is not None and duration < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._duration = duration

    @property
    def timestamps(self):
        """Gets the timestamps of this FileRasterSourcesSinks.  # noqa: E501

        in simulation in seconds  # noqa: E501

        :return: The timestamps of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: list[int]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this FileRasterSourcesSinks.

        in simulation in seconds  # noqa: E501

        :param timestamps: The timestamps of this FileRasterSourcesSinks.  # noqa: E501
        :type: list[int]
        """

        self._timestamps = timestamps

    @property
    def interval(self):
        """Gets the interval of this FileRasterSourcesSinks.  # noqa: E501

        interval in seconds  # noqa: E501

        :return: The interval of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this FileRasterSourcesSinks.

        interval in seconds  # noqa: E501

        :param interval: The interval of this FileRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if interval is not None and interval > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if interval is not None and interval < 0:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `0`")  # noqa: E501

        self._interval = interval

    @property
    def values_reference(self):
        """Gets the values_reference of this FileRasterSourcesSinks.  # noqa: E501


        :return: The values_reference of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._values_reference

    @values_reference.setter
    def values_reference(self, values_reference):
        """Sets the values_reference of this FileRasterSourcesSinks.


        :param values_reference: The values_reference of this FileRasterSourcesSinks.  # noqa: E501
        :type: str
        """
        if values_reference is not None and len(values_reference) > 255:
            raise ValueError("Invalid value for `values_reference`, length must be less than or equal to `255`")  # noqa: E501

        self._values_reference = values_reference

    @property
    def fill_value(self):
        """Gets the fill_value of this FileRasterSourcesSinks.  # noqa: E501


        :return: The fill_value of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._fill_value

    @fill_value.setter
    def fill_value(self, fill_value):
        """Sets the fill_value of this FileRasterSourcesSinks.


        :param fill_value: The fill_value of this FileRasterSourcesSinks.  # noqa: E501
        :type: str
        """
        if fill_value is not None and len(fill_value) > 128:
            raise ValueError("Invalid value for `fill_value`, length must be less than or equal to `128`")  # noqa: E501
        if fill_value is not None and len(fill_value) < 1:
            raise ValueError("Invalid value for `fill_value`, length must be greater than or equal to `1`")  # noqa: E501

        self._fill_value = fill_value

    @property
    def units(self):
        """Gets the units of this FileRasterSourcesSinks.  # noqa: E501


        :return: The units of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this FileRasterSourcesSinks.


        :param units: The units of this FileRasterSourcesSinks.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"m/s", "mm", "mm/h", "mm/hr"]  # noqa: E501
        if units not in allowed_values:
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

    @property
    def geotransform(self):
        """Gets the geotransform of this FileRasterSourcesSinks.  # noqa: E501


        :return: The geotransform of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: list[float]
        """
        return self._geotransform

    @geotransform.setter
    def geotransform(self, geotransform):
        """Sets the geotransform of this FileRasterSourcesSinks.


        :param geotransform: The geotransform of this FileRasterSourcesSinks.  # noqa: E501
        :type: list[float]
        """

        self._geotransform = geotransform

    @property
    def epsg_code(self):
        """Gets the epsg_code of this FileRasterSourcesSinks.  # noqa: E501


        :return: The epsg_code of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._epsg_code

    @epsg_code.setter
    def epsg_code(self, epsg_code):
        """Sets the epsg_code of this FileRasterSourcesSinks.


        :param epsg_code: The epsg_code of this FileRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if epsg_code is not None and epsg_code > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `epsg_code`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if epsg_code is not None and epsg_code < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `epsg_code`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._epsg_code = epsg_code

    @property
    def file(self):
        """Gets the file of this FileRasterSourcesSinks.  # noqa: E501


        :return: The file of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: FileReadOnly
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FileRasterSourcesSinks.


        :param file: The file of this FileRasterSourcesSinks.  # noqa: E501
        :type: FileReadOnly
        """

        self._file = file

    @property
    def type(self):
        """Gets the type of this FileRasterSourcesSinks.  # noqa: E501


        :return: The type of this FileRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileRasterSourcesSinks.


        :param type: The type of this FileRasterSourcesSinks.  # noqa: E501
        :type: str
        """
        allowed_values = ["netcdf4"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, FileRasterSourcesSinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
