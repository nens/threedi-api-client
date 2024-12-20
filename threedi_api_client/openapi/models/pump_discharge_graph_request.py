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

class PumpDischargeGraphRequest(object):
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
        'start_time': 'int',
        'history_points_limit': 'int',
        'subscribe': 'bool',
        'subscribe_rate_limit': 'float',
        'pump_id': 'int'
    }

    required_fields = [
       'start_time',
       'subscribe',
       'pump_id'
    ]

    attribute_map = {
        'start_time': 'start_time',
        'history_points_limit': 'history_points_limit',
        'subscribe': 'subscribe',
        'subscribe_rate_limit': 'subscribe_rate_limit',
        'pump_id': 'pump_id'
    }

    def __init__(self, start_time=None, history_points_limit=None, subscribe=None, subscribe_rate_limit=None, pump_id=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """PumpDischargeGraphRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._start_time = None
        self._history_points_limit = None
        self._subscribe = None
        self._subscribe_rate_limit = None
        self._pump_id = None
        self.discriminator = None

        self.start_time = start_time
        if history_points_limit is not None:
            self.history_points_limit = history_points_limit
        self.subscribe = subscribe
        if subscribe_rate_limit is not None:
            self.subscribe_rate_limit = subscribe_rate_limit
        self.pump_id = pump_id

    @property
    def start_time(self):
        """Gets the start_time of this PumpDischargeGraphRequest.  # noqa: E501

        simulation time in seconds  # noqa: E501

        :return: The start_time of this PumpDischargeGraphRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PumpDischargeGraphRequest.

        simulation time in seconds  # noqa: E501

        :param start_time: The start_time of this PumpDischargeGraphRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and start_time is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `start_time`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                start_time is not None and start_time < 0):  # noqa: E501
            self.__handle_validation_error("Invalid value for `start_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start_time = start_time

    @property
    def history_points_limit(self):
        """Gets the history_points_limit of this PumpDischargeGraphRequest.  # noqa: E501

        Maximum number of points of history to return  # noqa: E501

        :return: The history_points_limit of this PumpDischargeGraphRequest.  # noqa: E501
        :rtype: int
        """
        return self._history_points_limit

    @history_points_limit.setter
    def history_points_limit(self, history_points_limit):
        """Sets the history_points_limit of this PumpDischargeGraphRequest.

        Maximum number of points of history to return  # noqa: E501

        :param history_points_limit: The history_points_limit of this PumpDischargeGraphRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                history_points_limit is not None and history_points_limit > 500):  # noqa: E501
            self.__handle_validation_error("Invalid value for `history_points_limit`, must be a value less than or equal to `500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                history_points_limit is not None and history_points_limit < 1):  # noqa: E501
            self.__handle_validation_error("Invalid value for `history_points_limit`, must be a value greater than or equal to `1`")  # noqa: E501

        self._history_points_limit = history_points_limit

    @property
    def subscribe(self):
        """Gets the subscribe of this PumpDischargeGraphRequest.  # noqa: E501

        Subscribe for new results during simulation  # noqa: E501

        :return: The subscribe of this PumpDischargeGraphRequest.  # noqa: E501
        :rtype: bool
        """
        return self._subscribe

    @subscribe.setter
    def subscribe(self, subscribe):
        """Sets the subscribe of this PumpDischargeGraphRequest.

        Subscribe for new results during simulation  # noqa: E501

        :param subscribe: The subscribe of this PumpDischargeGraphRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and subscribe is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `subscribe`, must not be `None`")  # noqa: E501

        self._subscribe = subscribe

    @property
    def subscribe_rate_limit(self):
        """Gets the subscribe_rate_limit of this PumpDischargeGraphRequest.  # noqa: E501

        Max number of items per second for subscription  # noqa: E501

        :return: The subscribe_rate_limit of this PumpDischargeGraphRequest.  # noqa: E501
        :rtype: float
        """
        return self._subscribe_rate_limit

    @subscribe_rate_limit.setter
    def subscribe_rate_limit(self, subscribe_rate_limit):
        """Sets the subscribe_rate_limit of this PumpDischargeGraphRequest.

        Max number of items per second for subscription  # noqa: E501

        :param subscribe_rate_limit: The subscribe_rate_limit of this PumpDischargeGraphRequest.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                subscribe_rate_limit is not None and subscribe_rate_limit > 2):  # noqa: E501
            self.__handle_validation_error("Invalid value for `subscribe_rate_limit`, must be a value less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subscribe_rate_limit is not None and subscribe_rate_limit < 0.25):  # noqa: E501
            self.__handle_validation_error("Invalid value for `subscribe_rate_limit`, must be a value greater than or equal to `0.25`")  # noqa: E501

        self._subscribe_rate_limit = subscribe_rate_limit

    @property
    def pump_id(self):
        """Gets the pump_id of this PumpDischargeGraphRequest.  # noqa: E501


        :return: The pump_id of this PumpDischargeGraphRequest.  # noqa: E501
        :rtype: int
        """
        return self._pump_id

    @pump_id.setter
    def pump_id(self, pump_id):
        """Sets the pump_id of this PumpDischargeGraphRequest.


        :param pump_id: The pump_id of this PumpDischargeGraphRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pump_id is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `pump_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pump_id is not None and pump_id < 1):  # noqa: E501
            self.__handle_validation_error("Invalid value for `pump_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._pump_id = pump_id

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
        if not isinstance(other, PumpDischargeGraphRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PumpDischargeGraphRequest):
            return True

        return self.to_dict() != other.to_dict()
