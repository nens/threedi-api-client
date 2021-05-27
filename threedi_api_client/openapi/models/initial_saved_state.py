# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 1.0.16   3Di core release: 2.0.11  deployed on:  07:33AM (UTC) on September 04, 2020  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from threedi_api_client.openapi.configuration import Configuration


class InitialSavedState(object):
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
        'saved_state': 'str',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'saved_state': 'saved_state',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, url=None, simulation=None, saved_state=None, id=None, uuid=None, local_vars_configuration=None):  # noqa: E501
        """InitialSavedState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._simulation = None
        self._saved_state = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.saved_state = saved_state
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def url(self):
        """Gets the url of this InitialSavedState.  # noqa: E501


        :return: The url of this InitialSavedState.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InitialSavedState.


        :param url: The url of this InitialSavedState.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this InitialSavedState.  # noqa: E501


        :return: The simulation of this InitialSavedState.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this InitialSavedState.


        :param simulation: The simulation of this InitialSavedState.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def saved_state(self):
        """Gets the saved_state of this InitialSavedState.  # noqa: E501


        :return: The saved_state of this InitialSavedState.  # noqa: E501
        :rtype: str
        """
        return self._saved_state

    @saved_state.setter
    def saved_state(self, saved_state):
        """Sets the saved_state of this InitialSavedState.


        :param saved_state: The saved_state of this InitialSavedState.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and saved_state is None:  # noqa: E501
            raise ValueError("Invalid value for `saved_state`, must not be `None`")  # noqa: E501

        self._saved_state = saved_state

    @property
    def id(self):
        """Gets the id of this InitialSavedState.  # noqa: E501


        :return: The id of this InitialSavedState.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InitialSavedState.


        :param id: The id of this InitialSavedState.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this InitialSavedState.  # noqa: E501


        :return: The uuid of this InitialSavedState.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InitialSavedState.


        :param uuid: The uuid of this InitialSavedState.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, InitialSavedState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InitialSavedState):
            return True

        return self.to_dict() != other.to_dict()