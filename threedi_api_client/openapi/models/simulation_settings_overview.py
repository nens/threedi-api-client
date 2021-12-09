# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.1.1   3Di core release: 2.1.9  deployed on:  10:36AM (UTC) on December 09, 2021  # noqa: E501

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

class SimulationSettingsOverview(object):
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
        'physical_settings': 'PhysicalSettings',
        'numerical_settings': 'NumericalSettings',
        'time_step_settings': 'TimeStepSettings',
        'aggregation_settings': 'list[AggregationSettings]'
    }

    attribute_map = {
        'physical_settings': 'physical_settings',
        'numerical_settings': 'numerical_settings',
        'time_step_settings': 'time_step_settings',
        'aggregation_settings': 'aggregation_settings'
    }

    def __init__(self, physical_settings=None, numerical_settings=None, time_step_settings=None, aggregation_settings=None, local_vars_configuration=None):  # noqa: E501
        """SimulationSettingsOverview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._physical_settings = None
        self._numerical_settings = None
        self._time_step_settings = None
        self._aggregation_settings = None
        self.discriminator = None

        if physical_settings is not None:
            self.physical_settings = physical_settings
        if numerical_settings is not None:
            self.numerical_settings = numerical_settings
        if time_step_settings is not None:
            self.time_step_settings = time_step_settings
        if aggregation_settings is not None:
            self.aggregation_settings = aggregation_settings

    @property
    def physical_settings(self):
        """Gets the physical_settings of this SimulationSettingsOverview.  # noqa: E501


        :return: The physical_settings of this SimulationSettingsOverview.  # noqa: E501
        :rtype: PhysicalSettings
        """
        return self._physical_settings

    @physical_settings.setter
    def physical_settings(self, physical_settings):
        """Sets the physical_settings of this SimulationSettingsOverview.


        :param physical_settings: The physical_settings of this SimulationSettingsOverview.  # noqa: E501
        :type: PhysicalSettings
        """

        self._physical_settings = physical_settings

    @property
    def numerical_settings(self):
        """Gets the numerical_settings of this SimulationSettingsOverview.  # noqa: E501


        :return: The numerical_settings of this SimulationSettingsOverview.  # noqa: E501
        :rtype: NumericalSettings
        """
        return self._numerical_settings

    @numerical_settings.setter
    def numerical_settings(self, numerical_settings):
        """Sets the numerical_settings of this SimulationSettingsOverview.


        :param numerical_settings: The numerical_settings of this SimulationSettingsOverview.  # noqa: E501
        :type: NumericalSettings
        """

        self._numerical_settings = numerical_settings

    @property
    def time_step_settings(self):
        """Gets the time_step_settings of this SimulationSettingsOverview.  # noqa: E501


        :return: The time_step_settings of this SimulationSettingsOverview.  # noqa: E501
        :rtype: TimeStepSettings
        """
        return self._time_step_settings

    @time_step_settings.setter
    def time_step_settings(self, time_step_settings):
        """Sets the time_step_settings of this SimulationSettingsOverview.


        :param time_step_settings: The time_step_settings of this SimulationSettingsOverview.  # noqa: E501
        :type: TimeStepSettings
        """

        self._time_step_settings = time_step_settings

    @property
    def aggregation_settings(self):
        """Gets the aggregation_settings of this SimulationSettingsOverview.  # noqa: E501


        :return: The aggregation_settings of this SimulationSettingsOverview.  # noqa: E501
        :rtype: list[AggregationSettings]
        """
        return self._aggregation_settings

    @aggregation_settings.setter
    def aggregation_settings(self, aggregation_settings):
        """Sets the aggregation_settings of this SimulationSettingsOverview.


        :param aggregation_settings: The aggregation_settings of this SimulationSettingsOverview.  # noqa: E501
        :type: list[AggregationSettings]
        """

        self._aggregation_settings = aggregation_settings

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
        if not isinstance(other, SimulationSettingsOverview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationSettingsOverview):
            return True

        return self.to_dict() != other.to_dict()
