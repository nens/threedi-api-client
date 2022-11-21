# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.0.8   3Di core release: 2.3.1  deployed on:  01:12PM (UTC) on November 15, 2022  # noqa: E501

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

class GridEventState(object):
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
        'state': 'str',
        'state_detail': 'object',
        'grid_id': 'int'
    }

    attribute_map = {
        'state': 'state',
        'state_detail': 'state_detail',
        'grid_id': 'grid_id'
    }

    def __init__(self, state=None, state_detail=None, grid_id=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """GridEventState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._state = None
        self._state_detail = None
        self._grid_id = None
        self.discriminator = None

        self.state = state
        self.state_detail = state_detail
        self.grid_id = grid_id

    @property
    def state(self):
        """Gets the state of this GridEventState.  # noqa: E501


        :return: The state of this GridEventState.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GridEventState.


        :param state: The state of this GridEventState.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["processing", "valid", "invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            self.__handle_validation_error(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_detail(self):
        """Gets the state_detail of this GridEventState.  # noqa: E501


        :return: The state_detail of this GridEventState.  # noqa: E501
        :rtype: object
        """
        return self._state_detail

    @state_detail.setter
    def state_detail(self, state_detail):
        """Sets the state_detail of this GridEventState.


        :param state_detail: The state_detail of this GridEventState.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and state_detail is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `state_detail`, must not be `None`")  # noqa: E501

        self._state_detail = state_detail

    @property
    def grid_id(self):
        """Gets the grid_id of this GridEventState.  # noqa: E501


        :return: The grid_id of this GridEventState.  # noqa: E501
        :rtype: int
        """
        return self._grid_id

    @grid_id.setter
    def grid_id(self, grid_id):
        """Sets the grid_id of this GridEventState.


        :param grid_id: The grid_id of this GridEventState.  # noqa: E501
        :type: int
        """

        self._grid_id = grid_id

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
        if not isinstance(other, GridEventState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GridEventState):
            return True

        return self.to_dict() != other.to_dict()
