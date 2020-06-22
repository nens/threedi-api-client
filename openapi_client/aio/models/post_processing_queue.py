# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.8   3Di core release: 2.0.9  deployed on:  12:56PM (UTC) on June 22, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.aio.configuration import Configuration


class PostProcessingQueue(object):
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
        'simulation': 'int',
        'status': 'str',
        'created': 'datetime'
    }

    attribute_map = {
        'simulation': 'simulation',
        'status': 'status',
        'created': 'created'
    }

    def __init__(self, simulation=None, status=None, created=None, local_vars_configuration=None):  # noqa: E501
        """PostProcessingQueue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._simulation = None
        self._status = None
        self._created = None
        self.discriminator = None

        self.simulation = simulation
        self.status = status
        if created is not None:
            self.created = created

    @property
    def simulation(self):
        """Gets the simulation of this PostProcessingQueue.  # noqa: E501


        :return: The simulation of this PostProcessingQueue.  # noqa: E501
        :rtype: int
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this PostProcessingQueue.


        :param simulation: The simulation of this PostProcessingQueue.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and simulation is None:  # noqa: E501
            raise ValueError("Invalid value for `simulation`, must not be `None`")  # noqa: E501

        self._simulation = simulation

    @property
    def status(self):
        """Gets the status of this PostProcessingQueue.  # noqa: E501


        :return: The status of this PostProcessingQueue.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostProcessingQueue.


        :param status: The status of this PostProcessingQueue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["created", "requested", "archiving", "archiving_failed", "archived"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created(self):
        """Gets the created of this PostProcessingQueue.  # noqa: E501


        :return: The created of this PostProcessingQueue.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PostProcessingQueue.


        :param created: The created of this PostProcessingQueue.  # noqa: E501
        :type: datetime
        """

        self._created = created

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
        if not isinstance(other, PostProcessingQueue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostProcessingQueue):
            return True

        return self.to_dict() != other.to_dict()
