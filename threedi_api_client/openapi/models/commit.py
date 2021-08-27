# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 1.0.61   3Di core release: 2.1.2  deployed on:  07:26AM (UTC) on August 17, 2021  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from threedi_api_client.openapi.configuration import Configuration


class Commit(object):
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
        'commit_message': 'str',
        'force_as': 'str',
        'schematisation_name': 'str'
    }

    attribute_map = {
        'commit_message': 'commit_message',
        'force_as': 'force_as',
        'schematisation_name': 'schematisation_name'
    }

    def __init__(self, commit_message=None, force_as=None, schematisation_name=None, local_vars_configuration=None):  # noqa: E501
        """Commit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._commit_message = None
        self._force_as = None
        self._schematisation_name = None
        self.discriminator = None

        self.commit_message = commit_message
        if force_as is not None:
            self.force_as = force_as
        if schematisation_name is not None:
            self.schematisation_name = schematisation_name

    @property
    def commit_message(self):
        """Gets the commit_message of this Commit.  # noqa: E501


        :return: The commit_message of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this Commit.


        :param commit_message: The commit_message of this Commit.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commit_message is not None and len(commit_message) > 512):
            raise ValueError("Invalid value for `commit_message`, length must be less than or equal to `512`")  # noqa: E501

        self._commit_message = commit_message

    @property
    def force_as(self):
        """Gets the force_as of this Commit.  # noqa: E501


        :return: The force_as of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._force_as

    @force_as.setter
    def force_as(self, force_as):
        """Sets the force_as of this Commit.


        :param force_as: The force_as of this Commit.  # noqa: E501
        :type: str
        """
        allowed_values = ["default", "new_revision", "new_schematisation"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and force_as not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `force_as` ({0}), must be one of {1}"  # noqa: E501
                .format(force_as, allowed_values)
            )

        self._force_as = force_as

    @property
    def schematisation_name(self):
        """Gets the schematisation_name of this Commit.  # noqa: E501


        :return: The schematisation_name of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._schematisation_name

    @schematisation_name.setter
    def schematisation_name(self, schematisation_name):
        """Sets the schematisation_name of this Commit.


        :param schematisation_name: The schematisation_name of this Commit.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                schematisation_name is not None and len(schematisation_name) > 256):
            raise ValueError("Invalid value for `schematisation_name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                schematisation_name is not None and len(schematisation_name) < 1):
            raise ValueError("Invalid value for `schematisation_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._schematisation_name = schematisation_name

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
        if not isinstance(other, Commit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Commit):
            return True

        return self.to_dict() != other.to_dict()
