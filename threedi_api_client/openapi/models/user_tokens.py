# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.2.34   3Di core release: 2.4.3  deployed on:  05:50PM (UTC) on June 14, 2023  # noqa: E501

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

class UserTokens(object):
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
        'user': 'int',
        'external_user_id': 'str',
        'created': 'datetime',
        'last_modified': 'datetime',
        'id_token': 'str',
        'access_token': 'str',
        'refresh_token': 'str'
    }

    attribute_map = {
        'user': 'user',
        'external_user_id': 'external_user_id',
        'created': 'created',
        'last_modified': 'last_modified',
        'id_token': 'id_token',
        'access_token': 'access_token',
        'refresh_token': 'refresh_token'
    }

    def __init__(self, user=None, external_user_id=None, created=None, last_modified=None, id_token=None, access_token=None, refresh_token=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """UserTokens - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._user = None
        self._external_user_id = None
        self._created = None
        self._last_modified = None
        self._id_token = None
        self._access_token = None
        self._refresh_token = None
        self.discriminator = None

        self.user = user
        self.external_user_id = external_user_id
        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified
        if id_token is not None:
            self.id_token = id_token
        if access_token is not None:
            self.access_token = access_token
        if refresh_token is not None:
            self.refresh_token = refresh_token

    @property
    def user(self):
        """Gets the user of this UserTokens.  # noqa: E501


        :return: The user of this UserTokens.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserTokens.


        :param user: The user of this UserTokens.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def external_user_id(self):
        """Gets the external_user_id of this UserTokens.  # noqa: E501

        The user ID in the external identity provider, which is present as the 'sub' field in tokens.  # noqa: E501

        :return: The external_user_id of this UserTokens.  # noqa: E501
        :rtype: str
        """
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, external_user_id):
        """Sets the external_user_id of this UserTokens.

        The user ID in the external identity provider, which is present as the 'sub' field in tokens.  # noqa: E501

        :param external_user_id: The external_user_id of this UserTokens.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_user_id is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `external_user_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_user_id is not None and len(external_user_id) > 255):
            self.__handle_validation_error("Invalid value for `external_user_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_user_id is not None and len(external_user_id) < 1):
            self.__handle_validation_error("Invalid value for `external_user_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._external_user_id = external_user_id

    @property
    def created(self):
        """Gets the created of this UserTokens.  # noqa: E501


        :return: The created of this UserTokens.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserTokens.


        :param created: The created of this UserTokens.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_modified(self):
        """Gets the last_modified of this UserTokens.  # noqa: E501

        The last time this remote user logged in.  # noqa: E501

        :return: The last_modified of this UserTokens.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this UserTokens.

        The last time this remote user logged in.  # noqa: E501

        :param last_modified: The last_modified of this UserTokens.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def id_token(self):
        """Gets the id_token of this UserTokens.  # noqa: E501

        The most recent ID token provided by the external identity provider.  # noqa: E501

        :return: The id_token of this UserTokens.  # noqa: E501
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this UserTokens.

        The most recent ID token provided by the external identity provider.  # noqa: E501

        :param id_token: The id_token of this UserTokens.  # noqa: E501
        :type: str
        """

        self._id_token = id_token

    @property
    def access_token(self):
        """Gets the access_token of this UserTokens.  # noqa: E501

        The most recent access token provided by the external identity provider.  # noqa: E501

        :return: The access_token of this UserTokens.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this UserTokens.

        The most recent access token provided by the external identity provider.  # noqa: E501

        :param access_token: The access_token of this UserTokens.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this UserTokens.  # noqa: E501

        The most recent refresh token provided by the external identity provider.  # noqa: E501

        :return: The refresh_token of this UserTokens.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this UserTokens.

        The most recent refresh token provided by the external identity provider.  # noqa: E501

        :param refresh_token: The refresh_token of this UserTokens.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

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
        if not isinstance(other, UserTokens):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserTokens):
            return True

        return self.to_dict() != other.to_dict()
