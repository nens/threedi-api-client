# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.16   3Di core release: 2.0.11  deployed on:  07:33AM (UTC) on September 04, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


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
        'general_settings': 'GeneralSettings',
        'numerical_settings': 'NumericalSettings',
        'time_step_settings': 'TimeStepSettings',
        'aggregation_settings': 'list[AggregationSettings]'
    }

    attribute_map = {
        'general_settings': 'general_settings',
        'numerical_settings': 'numerical_settings',
        'time_step_settings': 'time_step_settings',
        'aggregation_settings': 'aggregation_settings'
    }

    def __init__(self, general_settings=None, numerical_settings=None, time_step_settings=None, aggregation_settings=None, local_vars_configuration=None):  # noqa: E501
        """SimulationSettingsOverview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._general_settings = None
        self._numerical_settings = None
        self._time_step_settings = None
        self._aggregation_settings = None
        self.discriminator = None

        if general_settings is not None:
            self.general_settings = general_settings
        if numerical_settings is not None:
            self.numerical_settings = numerical_settings
        if time_step_settings is not None:
            self.time_step_settings = time_step_settings
        if aggregation_settings is not None:
            self.aggregation_settings = aggregation_settings

    @property
    def general_settings(self):
        """Gets the general_settings of this SimulationSettingsOverview.  # noqa: E501


        :return: The general_settings of this SimulationSettingsOverview.  # noqa: E501
        :rtype: GeneralSettings
        """
        return self._general_settings

    @general_settings.setter
    def general_settings(self, general_settings):
        """Sets the general_settings of this SimulationSettingsOverview.


        :param general_settings: The general_settings of this SimulationSettingsOverview.  # noqa: E501
        :type: GeneralSettings
        """

        self._general_settings = general_settings

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