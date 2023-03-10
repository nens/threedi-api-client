# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.2.6   3Di core release: 2.3.6  deployed on:  07:54AM (UTC) on March 10, 2023  # noqa: E501

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

class FileStructureControl(object):
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
        'id': 'int',
        'uid': 'str',
        'simulation': 'str',
        'offset': 'int',
        'file': 'File',
        'state': 'str',
        'state_detail': 'object'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'uid': 'uid',
        'simulation': 'simulation',
        'offset': 'offset',
        'file': 'file',
        'state': 'state',
        'state_detail': 'state_detail'
    }

    def __init__(self, url=None, id=None, uid=None, simulation=None, offset=None, file=None, state=None, state_detail=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """FileStructureControl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._id = None
        self._uid = None
        self._simulation = None
        self._offset = None
        self._file = None
        self._state = None
        self._state_detail = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if uid is not None:
            self.uid = uid
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        if file is not None:
            self.file = file
        if state is not None:
            self.state = state
        if state_detail is not None:
            self.state_detail = state_detail

    @property
    def url(self):
        """Gets the url of this FileStructureControl.  # noqa: E501


        :return: The url of this FileStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FileStructureControl.


        :param url: The url of this FileStructureControl.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this FileStructureControl.  # noqa: E501


        :return: The id of this FileStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileStructureControl.


        :param id: The id of this FileStructureControl.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uid(self):
        """Gets the uid of this FileStructureControl.  # noqa: E501


        :return: The uid of this FileStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this FileStructureControl.


        :param uid: The uid of this FileStructureControl.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def simulation(self):
        """Gets the simulation of this FileStructureControl.  # noqa: E501


        :return: The simulation of this FileStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this FileStructureControl.


        :param simulation: The simulation of this FileStructureControl.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this FileStructureControl.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this FileStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this FileStructureControl.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this FileStructureControl.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset > 2147483647):  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def file(self):
        """Gets the file of this FileStructureControl.  # noqa: E501


        :return: The file of this FileStructureControl.  # noqa: E501
        :rtype: File
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FileStructureControl.


        :param file: The file of this FileStructureControl.  # noqa: E501
        :type: File
        """

        self._file = file

    @property
    def state(self):
        """Gets the state of this FileStructureControl.  # noqa: E501


        :return: The state of this FileStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FileStructureControl.


        :param state: The state of this FileStructureControl.  # noqa: E501
        :type: str
        """
        allowed_values = ["processing", "valid", "invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            self.__handle_validation_error(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_detail(self):
        """Gets the state_detail of this FileStructureControl.  # noqa: E501


        :return: The state_detail of this FileStructureControl.  # noqa: E501
        :rtype: object
        """
        return self._state_detail

    @state_detail.setter
    def state_detail(self, state_detail):
        """Sets the state_detail of this FileStructureControl.


        :param state_detail: The state_detail of this FileStructureControl.  # noqa: E501
        :type: object
        """

        self._state_detail = state_detail

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
        if not isinstance(other, FileStructureControl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileStructureControl):
            return True

        return self.to_dict() != other.to_dict()
