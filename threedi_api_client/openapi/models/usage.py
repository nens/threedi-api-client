# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.14.0   3Di core release: 2.2.4  deployed on:  04:05PM (UTC) on January 25, 2022  # noqa: E501

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

class Usage(object):
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
        'simulation': 'Simulation',
        'started': 'datetime',
        'finished': 'datetime',
        'total_time': 'int',
        'status': 'str',
        'simulation_type': 'str',
        'user_name': 'str',
        'organisation_uuid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'simulation': 'simulation',
        'started': 'started',
        'finished': 'finished',
        'total_time': 'total_time',
        'status': 'status',
        'simulation_type': 'simulation_type',
        'user_name': 'user_name',
        'organisation_uuid': 'organisation_uuid'
    }

    def __init__(self, id=None, simulation=None, started=None, finished=None, total_time=None, status=None, simulation_type=None, user_name=None, organisation_uuid=None, local_vars_configuration=None):  # noqa: E501
        """Usage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._simulation = None
        self._started = None
        self._finished = None
        self._total_time = None
        self._status = None
        self._simulation_type = None
        self._user_name = None
        self._organisation_uuid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if simulation is not None:
            self.simulation = simulation
        self.started = started
        self.finished = finished
        self.total_time = total_time
        if status is not None:
            self.status = status
        if simulation_type is not None:
            self.simulation_type = simulation_type
        if user_name is not None:
            self.user_name = user_name
        if organisation_uuid is not None:
            self.organisation_uuid = organisation_uuid

    @property
    def id(self):
        """Gets the id of this Usage.  # noqa: E501


        :return: The id of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Usage.


        :param id: The id of this Usage.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def simulation(self):
        """Gets the simulation of this Usage.  # noqa: E501


        :return: The simulation of this Usage.  # noqa: E501
        :rtype: Simulation
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this Usage.


        :param simulation: The simulation of this Usage.  # noqa: E501
        :type: Simulation
        """

        self._simulation = simulation

    @property
    def started(self):
        """Gets the started of this Usage.  # noqa: E501


        :return: The started of this Usage.  # noqa: E501
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this Usage.


        :param started: The started of this Usage.  # noqa: E501
        :type: datetime
        """

        self._started = started

    @property
    def finished(self):
        """Gets the finished of this Usage.  # noqa: E501


        :return: The finished of this Usage.  # noqa: E501
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this Usage.


        :param finished: The finished of this Usage.  # noqa: E501
        :type: datetime
        """

        self._finished = finished

    @property
    def total_time(self):
        """Gets the total_time of this Usage.  # noqa: E501


        :return: The total_time of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this Usage.


        :param total_time: The total_time of this Usage.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                total_time is not None and total_time > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `total_time`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                total_time is not None and total_time < 0):  # noqa: E501
            raise ValueError("Invalid value for `total_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_time = total_time

    @property
    def status(self):
        """Gets the status of this Usage.  # noqa: E501


        :return: The status of this Usage.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Usage.


        :param status: The status of this Usage.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def simulation_type(self):
        """Gets the simulation_type of this Usage.  # noqa: E501


        :return: The simulation_type of this Usage.  # noqa: E501
        :rtype: str
        """
        return self._simulation_type

    @simulation_type.setter
    def simulation_type(self, simulation_type):
        """Sets the simulation_type of this Usage.


        :param simulation_type: The simulation_type of this Usage.  # noqa: E501
        :type: str
        """

        self._simulation_type = simulation_type

    @property
    def user_name(self):
        """Gets the user_name of this Usage.  # noqa: E501


        :return: The user_name of this Usage.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this Usage.


        :param user_name: The user_name of this Usage.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def organisation_uuid(self):
        """Gets the organisation_uuid of this Usage.  # noqa: E501


        :return: The organisation_uuid of this Usage.  # noqa: E501
        :rtype: str
        """
        return self._organisation_uuid

    @organisation_uuid.setter
    def organisation_uuid(self, organisation_uuid):
        """Sets the organisation_uuid of this Usage.


        :param organisation_uuid: The organisation_uuid of this Usage.  # noqa: E501
        :type: str
        """

        self._organisation_uuid = organisation_uuid

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
        if not isinstance(other, Usage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Usage):
            return True

        return self.to_dict() != other.to_dict()
