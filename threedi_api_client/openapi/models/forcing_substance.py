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

class ForcingSubstance(object):
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
        'substance': 'str',
        'substance_id': 'int',
        'substance_name': 'str',
        'concentrations': 'list[list[float]]'
    }

    required_fields = [
       'substance',
       'concentrations'
    ]

    attribute_map = {
        'id': 'id',
        'substance': 'substance',
        'substance_id': 'substance_id',
        'substance_name': 'substance_name',
        'concentrations': 'concentrations'
    }

    def __init__(self, id=None, substance=None, substance_id=None, substance_name=None, concentrations=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """ForcingSubstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._id = None
        self._substance = None
        self._substance_id = None
        self._substance_name = None
        self._concentrations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.substance = substance
        if substance_id is not None:
            self.substance_id = substance_id
        if substance_name is not None:
            self.substance_name = substance_name
        self.concentrations = concentrations

    @property
    def id(self):
        """Gets the id of this ForcingSubstance.  # noqa: E501


        :return: The id of this ForcingSubstance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ForcingSubstance.


        :param id: The id of this ForcingSubstance.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def substance(self):
        """Gets the substance of this ForcingSubstance.  # noqa: E501


        :return: The substance of this ForcingSubstance.  # noqa: E501
        :rtype: str
        """
        return self._substance

    @substance.setter
    def substance(self, substance):
        """Sets the substance of this ForcingSubstance.


        :param substance: The substance of this ForcingSubstance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and substance is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `substance`, must not be `None`")  # noqa: E501

        self._substance = substance

    @property
    def substance_id(self):
        """Gets the substance_id of this ForcingSubstance.  # noqa: E501


        :return: The substance_id of this ForcingSubstance.  # noqa: E501
        :rtype: int
        """
        return self._substance_id

    @substance_id.setter
    def substance_id(self, substance_id):
        """Sets the substance_id of this ForcingSubstance.


        :param substance_id: The substance_id of this ForcingSubstance.  # noqa: E501
        :type: int
        """

        self._substance_id = substance_id

    @property
    def substance_name(self):
        """Gets the substance_name of this ForcingSubstance.  # noqa: E501


        :return: The substance_name of this ForcingSubstance.  # noqa: E501
        :rtype: str
        """
        return self._substance_name

    @substance_name.setter
    def substance_name(self, substance_name):
        """Sets the substance_name of this ForcingSubstance.


        :param substance_name: The substance_name of this ForcingSubstance.  # noqa: E501
        :type: str
        """

        self._substance_name = substance_name

    @property
    def concentrations(self):
        """Gets the concentrations of this ForcingSubstance.  # noqa: E501

        Timeseries provided as a nested list. The inner list consists of exactly 2 values: timestamp, value  # noqa: E501

        :return: The concentrations of this ForcingSubstance.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._concentrations

    @concentrations.setter
    def concentrations(self, concentrations):
        """Sets the concentrations of this ForcingSubstance.

        Timeseries provided as a nested list. The inner list consists of exactly 2 values: timestamp, value  # noqa: E501

        :param concentrations: The concentrations of this ForcingSubstance.  # noqa: E501
        :type: list[list[float]]
        """
        if self.local_vars_configuration.client_side_validation and concentrations is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `concentrations`, must not be `None`")  # noqa: E501

        self._concentrations = concentrations

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
        if not isinstance(other, ForcingSubstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForcingSubstance):
            return True

        return self.to_dict() != other.to_dict()
