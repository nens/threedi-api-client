# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 0.0.37   3Di core release: 2.0.6  deployed on:  02:00PM (UTC) on March 17, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ThreediModelSavedState(object):
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
        'name': 'str',
        'created': 'datetime',
        'type': 'str',
        'tags': 'str',
        'expiry': 'datetime',
        'time': 'int',
        'variables': 'list[str]',
        'thresholds': 'list[float]'
    }

    attribute_map = {
        'url': 'url',
        'name': 'name',
        'created': 'created',
        'type': 'type',
        'tags': 'tags',
        'expiry': 'expiry',
        'time': 'time',
        'variables': 'variables',
        'thresholds': 'thresholds'
    }

    def __init__(self, url=None, name=None, created=None, type=None, tags=None, expiry=None, time=None, variables=None, thresholds=None):  # noqa: E501
        """ThreediModelSavedState - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._name = None
        self._created = None
        self._type = None
        self._tags = None
        self._expiry = None
        self._time = None
        self._variables = None
        self._thresholds = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.name = name
        self.created = created
        self.type = type
        if tags is not None:
            self.tags = tags
        self.expiry = expiry
        self.time = time
        self.variables = variables
        self.thresholds = thresholds

    @property
    def url(self):
        """Gets the url of this ThreediModelSavedState.  # noqa: E501


        :return: The url of this ThreediModelSavedState.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ThreediModelSavedState.


        :param url: The url of this ThreediModelSavedState.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this ThreediModelSavedState.  # noqa: E501


        :return: The name of this ThreediModelSavedState.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThreediModelSavedState.


        :param name: The name of this ThreediModelSavedState.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 80:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `80`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def created(self):
        """Gets the created of this ThreediModelSavedState.  # noqa: E501


        :return: The created of this ThreediModelSavedState.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ThreediModelSavedState.


        :param created: The created of this ThreediModelSavedState.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def type(self):
        """Gets the type of this ThreediModelSavedState.  # noqa: E501


        :return: The type of this ThreediModelSavedState.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThreediModelSavedState.


        :param type: The type of this ThreediModelSavedState.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["stable_threshold", "timed"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def tags(self):
        """Gets the tags of this ThreediModelSavedState.  # noqa: E501


        :return: The tags of this ThreediModelSavedState.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ThreediModelSavedState.


        :param tags: The tags of this ThreediModelSavedState.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def expiry(self):
        """Gets the expiry of this ThreediModelSavedState.  # noqa: E501


        :return: The expiry of this ThreediModelSavedState.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this ThreediModelSavedState.


        :param expiry: The expiry of this ThreediModelSavedState.  # noqa: E501
        :type: datetime
        """

        self._expiry = expiry

    @property
    def time(self):
        """Gets the time of this ThreediModelSavedState.  # noqa: E501

        Time in simulation to create savedstate  # noqa: E501

        :return: The time of this ThreediModelSavedState.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ThreediModelSavedState.

        Time in simulation to create savedstate  # noqa: E501

        :param time: The time of this ThreediModelSavedState.  # noqa: E501
        :type: int
        """
        if time is not None and time > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if time is not None and time < 0:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._time = time

    @property
    def variables(self):
        """Gets the variables of this ThreediModelSavedState.  # noqa: E501


        :return: The variables of this ThreediModelSavedState.  # noqa: E501
        :rtype: list[str]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this ThreediModelSavedState.


        :param variables: The variables of this ThreediModelSavedState.  # noqa: E501
        :type: list[str]
        """
        allowed_values = [None,"s1", "u1"]  # noqa: E501
        if not set(variables).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `variables` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(variables) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._variables = variables

    @property
    def thresholds(self):
        """Gets the thresholds of this ThreediModelSavedState.  # noqa: E501


        :return: The thresholds of this ThreediModelSavedState.  # noqa: E501
        :rtype: list[float]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this ThreediModelSavedState.


        :param thresholds: The thresholds of this ThreediModelSavedState.  # noqa: E501
        :type: list[float]
        """

        self._thresholds = thresholds

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
        if not isinstance(other, ThreediModelSavedState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
