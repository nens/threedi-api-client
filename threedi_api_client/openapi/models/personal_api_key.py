# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.19.3   3Di core release: 2.2.11  deployed on:  10:31AM (UTC) on June 01, 2022  # noqa: E501

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

class PersonalAPIKey(object):
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
        'prefix': 'str',
        'scope': 'str',
        'name': 'str',
        'expiry_date': 'datetime',
        'created': 'datetime',
        'revoked': 'bool',
        'last_used': 'date'
    }

    attribute_map = {
        'prefix': 'prefix',
        'scope': 'scope',
        'name': 'name',
        'expiry_date': 'expiry_date',
        'created': 'created',
        'revoked': 'revoked',
        'last_used': 'last_used'
    }

    def __init__(self, prefix=None, scope=None, name=None, expiry_date=None, created=None, revoked=None, last_used=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """PersonalAPIKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._prefix = None
        self._scope = None
        self._name = None
        self._expiry_date = None
        self._created = None
        self._revoked = None
        self._last_used = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        self.scope = scope
        self.name = name
        self.expiry_date = expiry_date
        if created is not None:
            self.created = created
        if revoked is not None:
            self.revoked = revoked
        if last_used is not None:
            self.last_used = last_used

    @property
    def prefix(self):
        """Gets the prefix of this PersonalAPIKey.  # noqa: E501


        :return: The prefix of this PersonalAPIKey.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this PersonalAPIKey.


        :param prefix: The prefix of this PersonalAPIKey.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                prefix is not None and len(prefix) < 1):
            self.__handle_validation_error("Invalid value for `prefix`, length must be greater than or equal to `1`")  # noqa: E501

        self._prefix = prefix

    @property
    def scope(self):
        """Gets the scope of this PersonalAPIKey.  # noqa: E501

        A space-separated list of {endpoint|*}:{read|readwrite}.  # noqa: E501

        :return: The scope of this PersonalAPIKey.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PersonalAPIKey.

        A space-separated list of {endpoint|*}:{read|readwrite}.  # noqa: E501

        :param scope: The scope of this PersonalAPIKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) < 1):
            self.__handle_validation_error("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501

        self._scope = scope

    @property
    def name(self):
        """Gets the name of this PersonalAPIKey.  # noqa: E501

        A free-form name for the API key. Need not be unique. 50 characters max.  # noqa: E501

        :return: The name of this PersonalAPIKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersonalAPIKey.

        A free-form name for the API key. Need not be unique. 50 characters max.  # noqa: E501

        :param name: The name of this PersonalAPIKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 50):
            self.__handle_validation_error("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            self.__handle_validation_error("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def expiry_date(self):
        """Gets the expiry_date of this PersonalAPIKey.  # noqa: E501

        Once API key expires, clients cannot use it anymore.  # noqa: E501

        :return: The expiry_date of this PersonalAPIKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this PersonalAPIKey.

        Once API key expires, clients cannot use it anymore.  # noqa: E501

        :param expiry_date: The expiry_date of this PersonalAPIKey.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def created(self):
        """Gets the created of this PersonalAPIKey.  # noqa: E501


        :return: The created of this PersonalAPIKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PersonalAPIKey.


        :param created: The created of this PersonalAPIKey.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def revoked(self):
        """Gets the revoked of this PersonalAPIKey.  # noqa: E501

        If the API key is revoked, clients cannot use it anymore. (This cannot be undone.)  # noqa: E501

        :return: The revoked of this PersonalAPIKey.  # noqa: E501
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this PersonalAPIKey.

        If the API key is revoked, clients cannot use it anymore. (This cannot be undone.)  # noqa: E501

        :param revoked: The revoked of this PersonalAPIKey.  # noqa: E501
        :type: bool
        """

        self._revoked = revoked

    @property
    def last_used(self):
        """Gets the last_used of this PersonalAPIKey.  # noqa: E501

        Last time the API key was used.  # noqa: E501

        :return: The last_used of this PersonalAPIKey.  # noqa: E501
        :rtype: date
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this PersonalAPIKey.

        Last time the API key was used.  # noqa: E501

        :param last_used: The last_used of this PersonalAPIKey.  # noqa: E501
        :type: date
        """

        self._last_used = last_used

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
        if not isinstance(other, PersonalAPIKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PersonalAPIKey):
            return True

        return self.to_dict() != other.to_dict()
