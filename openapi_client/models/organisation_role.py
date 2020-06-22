# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.8   3Di core release: 2.0.9  deployed on:  12:56PM (UTC) on June 22, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class OrganisationRole(object):
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
        'user': 'str',
        'role': 'str',
        'organisation': 'str',
        'organisation_name': 'str'
    }

    attribute_map = {
        'url': 'url',
        'user': 'user',
        'role': 'role',
        'organisation': 'organisation',
        'organisation_name': 'organisation_name'
    }

    def __init__(self, url=None, user=None, role=None, organisation=None, organisation_name=None, local_vars_configuration=None):  # noqa: E501
        """OrganisationRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._user = None
        self._role = None
        self._organisation = None
        self._organisation_name = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.user = user
        self.role = role
        self.organisation = organisation
        if organisation_name is not None:
            self.organisation_name = organisation_name

    @property
    def url(self):
        """Gets the url of this OrganisationRole.  # noqa: E501


        :return: The url of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OrganisationRole.


        :param url: The url of this OrganisationRole.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user(self):
        """Gets the user of this OrganisationRole.  # noqa: E501

        The username of a user  # noqa: E501

        :return: The user of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OrganisationRole.

        The username of a user  # noqa: E501

        :param user: The user of this OrganisationRole.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user is not None and not re.search(r'^[\w.@+-]+$', user)):  # noqa: E501
            raise ValueError(r"Invalid value for `user`, must be a follow pattern or equal to `/^[\w.@+-]+$/`")  # noqa: E501

        self._user = user

    @property
    def role(self):
        """Gets the role of this OrganisationRole.  # noqa: E501


        :return: The role of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this OrganisationRole.


        :param role: The role of this OrganisationRole.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def organisation(self):
        """Gets the organisation of this OrganisationRole.  # noqa: E501

        The unique_id of an organisation  # noqa: E501

        :return: The organisation of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this OrganisationRole.

        The unique_id of an organisation  # noqa: E501

        :param organisation: The organisation of this OrganisationRole.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organisation is None:  # noqa: E501
            raise ValueError("Invalid value for `organisation`, must not be `None`")  # noqa: E501

        self._organisation = organisation

    @property
    def organisation_name(self):
        """Gets the organisation_name of this OrganisationRole.  # noqa: E501


        :return: The organisation_name of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._organisation_name

    @organisation_name.setter
    def organisation_name(self, organisation_name):
        """Sets the organisation_name of this OrganisationRole.


        :param organisation_name: The organisation_name of this OrganisationRole.  # noqa: E501
        :type: str
        """

        self._organisation_name = organisation_name

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
        if not isinstance(other, OrganisationRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganisationRole):
            return True

        return self.to_dict() != other.to_dict()
