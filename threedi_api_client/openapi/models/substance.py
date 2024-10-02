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

class Substance(object):
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
        'name': 'str',
        'id': 'int',
        'diffusion_coefficient': 'float',
        'growth_coefficient': 'float',
        'decay_coefficient': 'float',
        'numerical_diffusion_limiter': 'int',
        'units': 'str',
        'uid': 'str'
    }

    required_fields = [
       'name',
    ]

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'name': 'name',
        'id': 'id',
        'diffusion_coefficient': 'diffusion_coefficient',
        'growth_coefficient': 'growth_coefficient',
        'decay_coefficient': 'decay_coefficient',
        'numerical_diffusion_limiter': 'numerical_diffusion_limiter',
        'units': 'units',
        'uid': 'uid'
    }

    def __init__(self, url=None, simulation=None, name=None, id=None, diffusion_coefficient=None, growth_coefficient=None, decay_coefficient=None, numerical_diffusion_limiter=None, units=None, uid=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """Substance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._simulation = None
        self._name = None
        self._id = None
        self._diffusion_coefficient = None
        self._growth_coefficient = None
        self._decay_coefficient = None
        self._numerical_diffusion_limiter = None
        self._units = None
        self._uid = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.name = name
        if id is not None:
            self.id = id
        if diffusion_coefficient is not None:
            self.diffusion_coefficient = diffusion_coefficient
        if growth_coefficient is not None:
            self.growth_coefficient = growth_coefficient
        if decay_coefficient is not None:
            self.decay_coefficient = decay_coefficient
        if numerical_diffusion_limiter is not None:
            self.numerical_diffusion_limiter = numerical_diffusion_limiter
        if units is not None:
            self.units = units
        if uid is not None:
            self.uid = uid

    @property
    def url(self):
        """Gets the url of this Substance.  # noqa: E501


        :return: The url of this Substance.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Substance.


        :param url: The url of this Substance.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this Substance.  # noqa: E501


        :return: The simulation of this Substance.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this Substance.


        :param simulation: The simulation of this Substance.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def name(self):
        """Gets the name of this Substance.  # noqa: E501


        :return: The name of this Substance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Substance.


        :param name: The name of this Substance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 1024):
            self.__handle_validation_error("Invalid value for `name`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            self.__handle_validation_error("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this Substance.  # noqa: E501


        :return: The id of this Substance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Substance.


        :param id: The id of this Substance.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def diffusion_coefficient(self):
        """Gets the diffusion_coefficient of this Substance.  # noqa: E501

        The diffusion coefficient (m2/s) for the substance.  # noqa: E501

        :return: The diffusion_coefficient of this Substance.  # noqa: E501
        :rtype: float
        """
        return self._diffusion_coefficient

    @diffusion_coefficient.setter
    def diffusion_coefficient(self, diffusion_coefficient):
        """Sets the diffusion_coefficient of this Substance.

        The diffusion coefficient (m2/s) for the substance.  # noqa: E501

        :param diffusion_coefficient: The diffusion_coefficient of this Substance.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                diffusion_coefficient is not None and diffusion_coefficient > 1):  # noqa: E501
            self.__handle_validation_error("Invalid value for `diffusion_coefficient`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                diffusion_coefficient is not None and diffusion_coefficient < 0):  # noqa: E501
            self.__handle_validation_error("Invalid value for `diffusion_coefficient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._diffusion_coefficient = diffusion_coefficient

    @property
    def growth_coefficient(self):
        """Gets the growth_coefficient of this Substance.  # noqa: E501

        The growth coefficient for the substance.  # noqa: E501

        :return: The growth_coefficient of this Substance.  # noqa: E501
        :rtype: float
        """
        return self._growth_coefficient

    @growth_coefficient.setter
    def growth_coefficient(self, growth_coefficient):
        """Sets the growth_coefficient of this Substance.

        The growth coefficient for the substance.  # noqa: E501

        :param growth_coefficient: The growth_coefficient of this Substance.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                growth_coefficient is not None and growth_coefficient < 0):  # noqa: E501
            self.__handle_validation_error("Invalid value for `growth_coefficient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._growth_coefficient = growth_coefficient

    @property
    def decay_coefficient(self):
        """Gets the decay_coefficient of this Substance.  # noqa: E501

        The decay coefficient for the substance.  # noqa: E501

        :return: The decay_coefficient of this Substance.  # noqa: E501
        :rtype: float
        """
        return self._decay_coefficient

    @decay_coefficient.setter
    def decay_coefficient(self, decay_coefficient):
        """Sets the decay_coefficient of this Substance.

        The decay coefficient for the substance.  # noqa: E501

        :param decay_coefficient: The decay_coefficient of this Substance.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                decay_coefficient is not None and decay_coefficient < 0):  # noqa: E501
            self.__handle_validation_error("Invalid value for `decay_coefficient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._decay_coefficient = decay_coefficient

    @property
    def numerical_diffusion_limiter(self):
        """Gets the numerical_diffusion_limiter of this Substance.  # noqa: E501

        The numerical diffusion limiter for the substance.   Options:  0 = off 1 = standard   # noqa: E501

        :return: The numerical_diffusion_limiter of this Substance.  # noqa: E501
        :rtype: int
        """
        return self._numerical_diffusion_limiter

    @numerical_diffusion_limiter.setter
    def numerical_diffusion_limiter(self, numerical_diffusion_limiter):
        """Sets the numerical_diffusion_limiter of this Substance.

        The numerical diffusion limiter for the substance.   Options:  0 = off 1 = standard   # noqa: E501

        :param numerical_diffusion_limiter: The numerical_diffusion_limiter of this Substance.  # noqa: E501
        :type: int
        """

        self._numerical_diffusion_limiter = numerical_diffusion_limiter

    @property
    def units(self):
        """Gets the units of this Substance.  # noqa: E501

        The units of the substance.  # noqa: E501

        :return: The units of this Substance.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Substance.

        The units of the substance.  # noqa: E501

        :param units: The units of this Substance.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                units is not None and len(units) > 16):
            self.__handle_validation_error("Invalid value for `units`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                units is not None and len(units) < 1):
            self.__handle_validation_error("Invalid value for `units`, length must be greater than or equal to `1`")  # noqa: E501

        self._units = units

    @property
    def uid(self):
        """Gets the uid of this Substance.  # noqa: E501


        :return: The uid of this Substance.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Substance.


        :param uid: The uid of this Substance.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if not isinstance(other, Substance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Substance):
            return True

        return self.to_dict() != other.to_dict()
