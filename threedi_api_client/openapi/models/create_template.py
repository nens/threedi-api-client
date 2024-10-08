# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.4.3   3Di core release: 3.5.0  deployed on:  03:07PM (UTC) on October 02, 2024  # noqa: E501

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

class CreateTemplate(object):
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
        'name': 'str',
        'simulation': 'str',
        'include_events': 'bool',
        'include_initials': 'bool',
        'include_settings': 'bool'
    }

    required_fields = [
       'name',
       'simulation',
    ]

    attribute_map = {
        'name': 'name',
        'simulation': 'simulation',
        'include_events': 'include_events',
        'include_initials': 'include_initials',
        'include_settings': 'include_settings'
    }

    def __init__(self, name=None, simulation=None, include_events=True, include_initials=True, include_settings=True, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """CreateTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._name = None
        self._simulation = None
        self._include_events = None
        self._include_initials = None
        self._include_settings = None
        self.discriminator = None

        self.name = name
        self.simulation = simulation
        if include_events is not None:
            self.include_events = include_events
        if include_initials is not None:
            self.include_initials = include_initials
        if include_settings is not None:
            self.include_settings = include_settings

    @property
    def name(self):
        """Gets the name of this CreateTemplate.  # noqa: E501


        :return: The name of this CreateTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTemplate.


        :param name: The name of this CreateTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            self.__handle_validation_error("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            self.__handle_validation_error("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def simulation(self):
        """Gets the simulation of this CreateTemplate.  # noqa: E501


        :return: The simulation of this CreateTemplate.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this CreateTemplate.


        :param simulation: The simulation of this CreateTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and simulation is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `simulation`, must not be `None`")  # noqa: E501

        self._simulation = simulation

    @property
    def include_events(self):
        """Gets the include_events of this CreateTemplate.  # noqa: E501


        :return: The include_events of this CreateTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._include_events

    @include_events.setter
    def include_events(self, include_events):
        """Sets the include_events of this CreateTemplate.


        :param include_events: The include_events of this CreateTemplate.  # noqa: E501
        :type: bool
        """

        self._include_events = include_events

    @property
    def include_initials(self):
        """Gets the include_initials of this CreateTemplate.  # noqa: E501


        :return: The include_initials of this CreateTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._include_initials

    @include_initials.setter
    def include_initials(self, include_initials):
        """Sets the include_initials of this CreateTemplate.


        :param include_initials: The include_initials of this CreateTemplate.  # noqa: E501
        :type: bool
        """

        self._include_initials = include_initials

    @property
    def include_settings(self):
        """Gets the include_settings of this CreateTemplate.  # noqa: E501


        :return: The include_settings of this CreateTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._include_settings

    @include_settings.setter
    def include_settings(self, include_settings):
        """Sets the include_settings of this CreateTemplate.


        :param include_settings: The include_settings of this CreateTemplate.  # noqa: E501
        :type: bool
        """

        self._include_settings = include_settings

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
        if not isinstance(other, CreateTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTemplate):
            return True

        return self.to_dict() != other.to_dict()
