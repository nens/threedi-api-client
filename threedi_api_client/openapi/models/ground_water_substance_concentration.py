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

class GroundWaterSubstanceConcentration(object):
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
        'substance': 'str',
        'substance_id': 'int',
        'substance_name': 'str',
        'initial_concentration': 'str',
        'initial_concentration_id': 'int',
        'uid': 'str',
        'id': 'int',
        'aggregation_method': 'str'
    }

    required_fields = [
       'substance',
       'initial_concentration',
       'aggregation_method'
    ]

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'substance': 'substance',
        'substance_id': 'substance_id',
        'substance_name': 'substance_name',
        'initial_concentration': 'initial_concentration',
        'initial_concentration_id': 'initial_concentration_id',
        'uid': 'uid',
        'id': 'id',
        'aggregation_method': 'aggregation_method'
    }

    def __init__(self, url=None, simulation=None, substance=None, substance_id=None, substance_name=None, initial_concentration=None, initial_concentration_id=None, uid=None, id=None, aggregation_method=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """GroundWaterSubstanceConcentration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._simulation = None
        self._substance = None
        self._substance_id = None
        self._substance_name = None
        self._initial_concentration = None
        self._initial_concentration_id = None
        self._uid = None
        self._id = None
        self._aggregation_method = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.substance = substance
        if substance_id is not None:
            self.substance_id = substance_id
        if substance_name is not None:
            self.substance_name = substance_name
        self.initial_concentration = initial_concentration
        if initial_concentration_id is not None:
            self.initial_concentration_id = initial_concentration_id
        if uid is not None:
            self.uid = uid
        if id is not None:
            self.id = id
        self.aggregation_method = aggregation_method

    @property
    def url(self):
        """Gets the url of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The url of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GroundWaterSubstanceConcentration.


        :param url: The url of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The simulation of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this GroundWaterSubstanceConcentration.


        :param simulation: The simulation of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def substance(self):
        """Gets the substance of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The substance of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: str
        """
        return self._substance

    @substance.setter
    def substance(self, substance):
        """Sets the substance of this GroundWaterSubstanceConcentration.


        :param substance: The substance of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and substance is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `substance`, must not be `None`")  # noqa: E501

        self._substance = substance

    @property
    def substance_id(self):
        """Gets the substance_id of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The substance_id of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: int
        """
        return self._substance_id

    @substance_id.setter
    def substance_id(self, substance_id):
        """Sets the substance_id of this GroundWaterSubstanceConcentration.


        :param substance_id: The substance_id of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: int
        """

        self._substance_id = substance_id

    @property
    def substance_name(self):
        """Gets the substance_name of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The substance_name of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: str
        """
        return self._substance_name

    @substance_name.setter
    def substance_name(self, substance_name):
        """Sets the substance_name of this GroundWaterSubstanceConcentration.


        :param substance_name: The substance_name of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: str
        """

        self._substance_name = substance_name

    @property
    def initial_concentration(self):
        """Gets the initial_concentration of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The initial_concentration of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: str
        """
        return self._initial_concentration

    @initial_concentration.setter
    def initial_concentration(self, initial_concentration):
        """Sets the initial_concentration of this GroundWaterSubstanceConcentration.


        :param initial_concentration: The initial_concentration of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and initial_concentration is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `initial_concentration`, must not be `None`")  # noqa: E501

        self._initial_concentration = initial_concentration

    @property
    def initial_concentration_id(self):
        """Gets the initial_concentration_id of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The initial_concentration_id of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: int
        """
        return self._initial_concentration_id

    @initial_concentration_id.setter
    def initial_concentration_id(self, initial_concentration_id):
        """Sets the initial_concentration_id of this GroundWaterSubstanceConcentration.


        :param initial_concentration_id: The initial_concentration_id of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: int
        """

        self._initial_concentration_id = initial_concentration_id

    @property
    def uid(self):
        """Gets the uid of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The uid of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this GroundWaterSubstanceConcentration.


        :param uid: The uid of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def id(self):
        """Gets the id of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The id of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroundWaterSubstanceConcentration.


        :param id: The id of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def aggregation_method(self):
        """Gets the aggregation_method of this GroundWaterSubstanceConcentration.  # noqa: E501


        :return: The aggregation_method of this GroundWaterSubstanceConcentration.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_method

    @aggregation_method.setter
    def aggregation_method(self, aggregation_method):
        """Sets the aggregation_method of this GroundWaterSubstanceConcentration.


        :param aggregation_method: The aggregation_method of this GroundWaterSubstanceConcentration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and aggregation_method is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `aggregation_method`, must not be `None`")  # noqa: E501
        allowed_values = ["mean", "max", "min"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and aggregation_method not in allowed_values:  # noqa: E501
            self.__handle_validation_error(
                "Invalid value for `aggregation_method` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_method, allowed_values)
            )

        self._aggregation_method = aggregation_method

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
        if not isinstance(other, GroundWaterSubstanceConcentration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroundWaterSubstanceConcentration):
            return True

        return self.to_dict() != other.to_dict()
