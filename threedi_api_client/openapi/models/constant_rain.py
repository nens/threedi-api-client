# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.4.24   3Di core release: 3.5.4.1  deployed on:  08:40AM (UTC) on December 20, 2024  # noqa: E501

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

class ConstantRain(object):
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
        'value': 'float',
        'units': 'str',
        'uid': 'str',
        'id': 'int',
        'substances': 'list[ForcingSubstanceWithZone]'
    }

    required_fields = [
       'offset',
       'duration',
       'value',
       'units',
    ]

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'offset': 'offset',
        'duration': 'duration',
        'value': 'value',
        'units': 'units',
        'uid': 'uid',
        'id': 'id',
        'substances': 'substances'
    }

    def __init__(self, url=None, simulation=None, offset=None, duration=None, value=None, units=None, uid=None, id=None, substances=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """ConstantRain - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._simulation = None
        self._offset = None
        self._duration = None
        self._value = None
        self._units = None
        self._uid = None
        self._id = None
        self._substances = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        self.duration = duration
        self.value = value
        self.units = units
        if uid is not None:
            self.uid = uid
        if id is not None:
            self.id = id
        if substances is not None:
            self.substances = substances

    @property
    def url(self):
        """Gets the url of this ConstantRain.  # noqa: E501


        :return: The url of this ConstantRain.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ConstantRain.


        :param url: The url of this ConstantRain.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this ConstantRain.  # noqa: E501


        :return: The simulation of this ConstantRain.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this ConstantRain.


        :param simulation: The simulation of this ConstantRain.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this ConstantRain.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this ConstantRain.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ConstantRain.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this ConstantRain.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset > 2147483647):  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def duration(self):
        """Gets the duration of this ConstantRain.  # noqa: E501

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :return: The duration of this ConstantRain.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ConstantRain.

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :param duration: The duration of this ConstantRain.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration > 9223372036854775807):  # noqa: E501
            self.__handle_validation_error("Invalid value for `duration`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration < -9223372036854775808):  # noqa: E501
            self.__handle_validation_error("Invalid value for `duration`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._duration = duration

    @property
    def value(self):
        """Gets the value of this ConstantRain.  # noqa: E501

        Rain intensity  # noqa: E501

        :return: The value of this ConstantRain.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConstantRain.

        Rain intensity  # noqa: E501

        :param value: The value of this ConstantRain.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def units(self):
        """Gets the units of this ConstantRain.  # noqa: E501

        m/s is only option for now  # noqa: E501

        :return: The units of this ConstantRain.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this ConstantRain.

        m/s is only option for now  # noqa: E501

        :param units: The units of this ConstantRain.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and units is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `units`, must not be `None`")  # noqa: E501
        allowed_values = ["m/s"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and units not in allowed_values:  # noqa: E501
            self.__handle_validation_error(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

    @property
    def uid(self):
        """Gets the uid of this ConstantRain.  # noqa: E501


        :return: The uid of this ConstantRain.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ConstantRain.


        :param uid: The uid of this ConstantRain.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def id(self):
        """Gets the id of this ConstantRain.  # noqa: E501


        :return: The id of this ConstantRain.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConstantRain.


        :param id: The id of this ConstantRain.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def substances(self):
        """Gets the substances of this ConstantRain.  # noqa: E501


        :return: The substances of this ConstantRain.  # noqa: E501
        :rtype: list[ForcingSubstanceWithZone]
        """
        return self._substances

    @substances.setter
    def substances(self, substances):
        """Sets the substances of this ConstantRain.


        :param substances: The substances of this ConstantRain.  # noqa: E501
        :type: list[ForcingSubstanceWithZone]
        """

        self._substances = substances

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

    def __handle_validation_error(self, message):
        # Only raise ValueError when not fetched from API
        from threedi_api_client import __version__ as VERSION

        if not self._fetched_from_api:
            raise ValueError(message + f" It is possible that the current threedi-api-client version ({VERSION}) is out of date: consult https://pypi.org/project/threedi-api-client/ and consider upgrading.")  # noqa: E501
        logger.warning(message + " Please update to the latest threedi-api-client version.")  # noqa: E501

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConstantRain):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConstantRain):
            return True

        return self.to_dict() != other.to_dict()
