# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.3.4   3Di core release: 3.3.1  deployed on:  08:44AM (UTC) on December 14, 2023  # noqa: E501

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

class Revision(object):
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
        'repository': 'str',
        'number': 'int',
        'hash': 'str',
        'commit_date': 'datetime',
        'user': 'str',
        'is_pinned': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'repository': 'repository',
        'number': 'number',
        'hash': 'hash',
        'commit_date': 'commit_date',
        'user': 'user',
        'is_pinned': 'is_pinned'
    }

    def __init__(self, url=None, id=None, repository=None, number=None, hash=None, commit_date=None, user=None, is_pinned=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """Revision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._id = None
        self._repository = None
        self._number = None
        self._hash = None
        self._commit_date = None
        self._user = None
        self._is_pinned = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        self.repository = repository
        if number is not None:
            self.number = number
        self.hash = hash
        self.commit_date = commit_date
        self.user = user
        self.is_pinned = is_pinned

    @property
    def url(self):
        """Gets the url of this Revision.  # noqa: E501


        :return: The url of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Revision.


        :param url: The url of this Revision.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this Revision.  # noqa: E501


        :return: The id of this Revision.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Revision.


        :param id: The id of this Revision.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def repository(self):
        """Gets the repository of this Revision.  # noqa: E501


        :return: The repository of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this Revision.


        :param repository: The repository of this Revision.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and repository is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `repository`, must not be `None`")  # noqa: E501

        self._repository = repository

    @property
    def number(self):
        """Gets the number of this Revision.  # noqa: E501


        :return: The number of this Revision.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Revision.


        :param number: The number of this Revision.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number is not None and number > 2147483647):  # noqa: E501
            self.__handle_validation_error("Invalid value for `number`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number is not None and number < -2147483648):  # noqa: E501
            self.__handle_validation_error("Invalid value for `number`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._number = number

    @property
    def hash(self):
        """Gets the hash of this Revision.  # noqa: E501

        unique identifier for changeset  # noqa: E501

        :return: The hash of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Revision.

        unique identifier for changeset  # noqa: E501

        :param hash: The hash of this Revision.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hash is not None and len(hash) > 200):
            self.__handle_validation_error("Invalid value for `hash`, length must be less than or equal to `200`")  # noqa: E501

        self._hash = hash

    @property
    def commit_date(self):
        """Gets the commit_date of this Revision.  # noqa: E501


        :return: The commit_date of this Revision.  # noqa: E501
        :rtype: datetime
        """
        return self._commit_date

    @commit_date.setter
    def commit_date(self, commit_date):
        """Sets the commit_date of this Revision.


        :param commit_date: The commit_date of this Revision.  # noqa: E501
        :type: datetime
        """

        self._commit_date = commit_date

    @property
    def user(self):
        """Gets the user of this Revision.  # noqa: E501

        user that committed the changeset for this revision  # noqa: E501

        :return: The user of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Revision.

        user that committed the changeset for this revision  # noqa: E501

        :param user: The user of this Revision.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                user is not None and len(user) > 128):
            self.__handle_validation_error("Invalid value for `user`, length must be less than or equal to `128`")  # noqa: E501

        self._user = user

    @property
    def is_pinned(self):
        """Gets the is_pinned of this Revision.  # noqa: E501


        :return: The is_pinned of this Revision.  # noqa: E501
        :rtype: bool
        """
        return self._is_pinned

    @is_pinned.setter
    def is_pinned(self, is_pinned):
        """Sets the is_pinned of this Revision.


        :param is_pinned: The is_pinned of this Revision.  # noqa: E501
        :type: bool
        """

        self._is_pinned = is_pinned

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
        if not isinstance(other, Revision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Revision):
            return True

        return self.to_dict() != other.to_dict()
