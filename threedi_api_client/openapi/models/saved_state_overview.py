# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.11.1   3Di core release: 2.2.3  deployed on:  02:06PM (UTC) on January 13, 2022  # noqa: E501

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

class SavedStateOverview(object):
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
        'name': 'str',
        'type': 'str',
        'created': 'datetime',
        'created_time': 'int',
        'tags': 'list[str]',
        'expiry': 'datetime',
        'time': 'int',
        'thresholds': 'list[Threshold]',
        'file': 'FileReadOnly',
        'id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'created': 'created',
        'created_time': 'created_time',
        'tags': 'tags',
        'expiry': 'expiry',
        'time': 'time',
        'thresholds': 'thresholds',
        'file': 'file',
        'id': 'id',
        'uuid': 'uuid'
    }

    def __init__(self, name=None, type=None, created=None, created_time=None, tags=None, expiry=None, time=None, thresholds=None, file=None, id=None, uuid=None, local_vars_configuration=None):  # noqa: E501
        """SavedStateOverview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._created = None
        self._created_time = None
        self._tags = None
        self._expiry = None
        self._time = None
        self._thresholds = None
        self._file = None
        self._id = None
        self._uuid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.type = type
        self.created = created
        self.created_time = created_time
        if tags is not None:
            self.tags = tags
        self.expiry = expiry
        self.time = time
        self.thresholds = thresholds
        if file is not None:
            self.file = file
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid

    @property
    def name(self):
        """Gets the name of this SavedStateOverview.  # noqa: E501


        :return: The name of this SavedStateOverview.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SavedStateOverview.


        :param name: The name of this SavedStateOverview.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 80):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this SavedStateOverview.  # noqa: E501


        :return: The type of this SavedStateOverview.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SavedStateOverview.


        :param type: The type of this SavedStateOverview.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["stable_threshold", "timed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            logger.warning(
                "Warning: Unknown value for `type` ({0}), must be one of {1}. Either your threedi-api-client version is out of date or this value is invalid."  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def created(self):
        """Gets the created of this SavedStateOverview.  # noqa: E501


        :return: The created of this SavedStateOverview.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SavedStateOverview.


        :param created: The created of this SavedStateOverview.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def created_time(self):
        """Gets the created_time of this SavedStateOverview.  # noqa: E501

        Time in simulation the savedstate has been created  # noqa: E501

        :return: The created_time of this SavedStateOverview.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this SavedStateOverview.

        Time in simulation the savedstate has been created  # noqa: E501

        :param created_time: The created_time of this SavedStateOverview.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                created_time is not None and created_time > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `created_time`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                created_time is not None and created_time < 0):  # noqa: E501
            raise ValueError("Invalid value for `created_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._created_time = created_time

    @property
    def tags(self):
        """Gets the tags of this SavedStateOverview.  # noqa: E501

        tags provided as a list of strings  # noqa: E501

        :return: The tags of this SavedStateOverview.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SavedStateOverview.

        tags provided as a list of strings  # noqa: E501

        :param tags: The tags of this SavedStateOverview.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def expiry(self):
        """Gets the expiry of this SavedStateOverview.  # noqa: E501


        :return: The expiry of this SavedStateOverview.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this SavedStateOverview.


        :param expiry: The expiry of this SavedStateOverview.  # noqa: E501
        :type: datetime
        """

        self._expiry = expiry

    @property
    def time(self):
        """Gets the time of this SavedStateOverview.  # noqa: E501

        Time in simulation to create savedstate  # noqa: E501

        :return: The time of this SavedStateOverview.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SavedStateOverview.

        Time in simulation to create savedstate  # noqa: E501

        :param time: The time of this SavedStateOverview.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                time is not None and time > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time is not None and time < 0):  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._time = time

    @property
    def thresholds(self):
        """Gets the thresholds of this SavedStateOverview.  # noqa: E501


        :return: The thresholds of this SavedStateOverview.  # noqa: E501
        :rtype: list[Threshold]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this SavedStateOverview.


        :param thresholds: The thresholds of this SavedStateOverview.  # noqa: E501
        :type: list[Threshold]
        """
        if self.local_vars_configuration.client_side_validation and thresholds is None:  # noqa: E501
            raise ValueError("Invalid value for `thresholds`, must not be `None`")  # noqa: E501

        self._thresholds = thresholds

    @property
    def file(self):
        """Gets the file of this SavedStateOverview.  # noqa: E501


        :return: The file of this SavedStateOverview.  # noqa: E501
        :rtype: FileReadOnly
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this SavedStateOverview.


        :param file: The file of this SavedStateOverview.  # noqa: E501
        :type: FileReadOnly
        """

        self._file = file

    @property
    def id(self):
        """Gets the id of this SavedStateOverview.  # noqa: E501


        :return: The id of this SavedStateOverview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SavedStateOverview.


        :param id: The id of this SavedStateOverview.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this SavedStateOverview.  # noqa: E501


        :return: The uuid of this SavedStateOverview.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this SavedStateOverview.


        :param uuid: The uuid of this SavedStateOverview.  # noqa: E501
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
        if not isinstance(other, SavedStateOverview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SavedStateOverview):
            return True

        return self.to_dict() != other.to_dict()
