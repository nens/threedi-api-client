# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.1.1   3Di core release: 2.1.9  deployed on:  10:36AM (UTC) on December 09, 2021  # noqa: E501

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

class Contract(object):
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
        'organisation': 'str',
        'organisation_name': 'str',
        'hours_bought': 'int',
        'hours_used': 'float',
        'session_limit': 'int',
        'current_sessions': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'organisation': 'organisation',
        'organisation_name': 'organisation_name',
        'hours_bought': 'hours_bought',
        'hours_used': 'hours_used',
        'session_limit': 'session_limit',
        'current_sessions': 'current_sessions'
    }

    def __init__(self, url=None, id=None, organisation=None, organisation_name=None, hours_bought=None, hours_used=None, session_limit=None, current_sessions=None, local_vars_configuration=None):  # noqa: E501
        """Contract - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._id = None
        self._organisation = None
        self._organisation_name = None
        self._hours_bought = None
        self._hours_used = None
        self._session_limit = None
        self._current_sessions = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        self.organisation = organisation
        if organisation_name is not None:
            self.organisation_name = organisation_name
        self.hours_bought = hours_bought
        if hours_used is not None:
            self.hours_used = hours_used
        self.session_limit = session_limit
        if current_sessions is not None:
            self.current_sessions = current_sessions

    @property
    def url(self):
        """Gets the url of this Contract.  # noqa: E501


        :return: The url of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Contract.


        :param url: The url of this Contract.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this Contract.  # noqa: E501


        :return: The id of this Contract.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Contract.


        :param id: The id of this Contract.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organisation(self):
        """Gets the organisation of this Contract.  # noqa: E501

        The unique_id of an organisation  # noqa: E501

        :return: The organisation of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this Contract.

        The unique_id of an organisation  # noqa: E501

        :param organisation: The organisation of this Contract.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organisation is None:  # noqa: E501
            raise ValueError("Invalid value for `organisation`, must not be `None`")  # noqa: E501

        self._organisation = organisation

    @property
    def organisation_name(self):
        """Gets the organisation_name of this Contract.  # noqa: E501


        :return: The organisation_name of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._organisation_name

    @organisation_name.setter
    def organisation_name(self, organisation_name):
        """Sets the organisation_name of this Contract.


        :param organisation_name: The organisation_name of this Contract.  # noqa: E501
        :type: str
        """

        self._organisation_name = organisation_name

    @property
    def hours_bought(self):
        """Gets the hours_bought of this Contract.  # noqa: E501


        :return: The hours_bought of this Contract.  # noqa: E501
        :rtype: int
        """
        return self._hours_bought

    @hours_bought.setter
    def hours_bought(self, hours_bought):
        """Sets the hours_bought of this Contract.


        :param hours_bought: The hours_bought of this Contract.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and hours_bought is None:  # noqa: E501
            raise ValueError("Invalid value for `hours_bought`, must not be `None`")  # noqa: E501

        self._hours_bought = hours_bought

    @property
    def hours_used(self):
        """Gets the hours_used of this Contract.  # noqa: E501


        :return: The hours_used of this Contract.  # noqa: E501
        :rtype: float
        """
        return self._hours_used

    @hours_used.setter
    def hours_used(self, hours_used):
        """Sets the hours_used of this Contract.


        :param hours_used: The hours_used of this Contract.  # noqa: E501
        :type: float
        """

        self._hours_used = hours_used

    @property
    def session_limit(self):
        """Gets the session_limit of this Contract.  # noqa: E501


        :return: The session_limit of this Contract.  # noqa: E501
        :rtype: int
        """
        return self._session_limit

    @session_limit.setter
    def session_limit(self, session_limit):
        """Sets the session_limit of this Contract.


        :param session_limit: The session_limit of this Contract.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and session_limit is None:  # noqa: E501
            raise ValueError("Invalid value for `session_limit`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                session_limit is not None and session_limit > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `session_limit`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                session_limit is not None and session_limit < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `session_limit`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._session_limit = session_limit

    @property
    def current_sessions(self):
        """Gets the current_sessions of this Contract.  # noqa: E501


        :return: The current_sessions of this Contract.  # noqa: E501
        :rtype: str
        """
        return self._current_sessions

    @current_sessions.setter
    def current_sessions(self, current_sessions):
        """Sets the current_sessions of this Contract.


        :param current_sessions: The current_sessions of this Contract.  # noqa: E501
        :type: str
        """

        self._current_sessions = current_sessions

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
        if not isinstance(other, Contract):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Contract):
            return True

        return self.to_dict() != other.to_dict()
