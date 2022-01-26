# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.15.1   3Di core release: 2.2.4  deployed on:  01:07PM (UTC) on January 26, 2022  # noqa: E501

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

class OneDWaterLevelFile(object):
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
        'initial_waterlevel': 'str',
        'initial_waterlevel_id': 'int',
        'uid': 'str',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'initial_waterlevel': 'initial_waterlevel',
        'initial_waterlevel_id': 'initial_waterlevel_id',
        'uid': 'uid',
        'id': 'id'
    }

    def __init__(self, url=None, simulation=None, initial_waterlevel=None, initial_waterlevel_id=None, uid=None, id=None, local_vars_configuration=None):  # noqa: E501
        """OneDWaterLevelFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._simulation = None
        self._initial_waterlevel = None
        self._initial_waterlevel_id = None
        self._uid = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.initial_waterlevel = initial_waterlevel
        if initial_waterlevel_id is not None:
            self.initial_waterlevel_id = initial_waterlevel_id
        if uid is not None:
            self.uid = uid
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this OneDWaterLevelFile.  # noqa: E501


        :return: The url of this OneDWaterLevelFile.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OneDWaterLevelFile.


        :param url: The url of this OneDWaterLevelFile.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this OneDWaterLevelFile.  # noqa: E501


        :return: The simulation of this OneDWaterLevelFile.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this OneDWaterLevelFile.


        :param simulation: The simulation of this OneDWaterLevelFile.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def initial_waterlevel(self):
        """Gets the initial_waterlevel of this OneDWaterLevelFile.  # noqa: E501


        :return: The initial_waterlevel of this OneDWaterLevelFile.  # noqa: E501
        :rtype: str
        """
        return self._initial_waterlevel

    @initial_waterlevel.setter
    def initial_waterlevel(self, initial_waterlevel):
        """Sets the initial_waterlevel of this OneDWaterLevelFile.


        :param initial_waterlevel: The initial_waterlevel of this OneDWaterLevelFile.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and initial_waterlevel is None:  # noqa: E501
            raise ValueError("Invalid value for `initial_waterlevel`, must not be `None`")  # noqa: E501

        self._initial_waterlevel = initial_waterlevel

    @property
    def initial_waterlevel_id(self):
        """Gets the initial_waterlevel_id of this OneDWaterLevelFile.  # noqa: E501


        :return: The initial_waterlevel_id of this OneDWaterLevelFile.  # noqa: E501
        :rtype: int
        """
        return self._initial_waterlevel_id

    @initial_waterlevel_id.setter
    def initial_waterlevel_id(self, initial_waterlevel_id):
        """Sets the initial_waterlevel_id of this OneDWaterLevelFile.


        :param initial_waterlevel_id: The initial_waterlevel_id of this OneDWaterLevelFile.  # noqa: E501
        :type: int
        """

        self._initial_waterlevel_id = initial_waterlevel_id

    @property
    def uid(self):
        """Gets the uid of this OneDWaterLevelFile.  # noqa: E501


        :return: The uid of this OneDWaterLevelFile.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this OneDWaterLevelFile.


        :param uid: The uid of this OneDWaterLevelFile.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def id(self):
        """Gets the id of this OneDWaterLevelFile.  # noqa: E501


        :return: The id of this OneDWaterLevelFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OneDWaterLevelFile.


        :param id: The id of this OneDWaterLevelFile.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, OneDWaterLevelFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneDWaterLevelFile):
            return True

        return self.to_dict() != other.to_dict()
