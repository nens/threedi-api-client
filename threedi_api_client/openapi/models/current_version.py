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

class CurrentVersion(object):
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
        'threedi_version': 'str',
        'threedicore_version': 'str'
    }

    attribute_map = {
        'threedi_version': 'threedi_version',
        'threedicore_version': 'threedicore_version'
    }

    def __init__(self, threedi_version=None, threedicore_version=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """CurrentVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._threedi_version = None
        self._threedicore_version = None
        self.discriminator = None

        if threedi_version is not None:
            self.threedi_version = threedi_version
        if threedicore_version is not None:
            self.threedicore_version = threedicore_version

    @property
    def threedi_version(self):
        """Gets the threedi_version of this CurrentVersion.  # noqa: E501


        :return: The threedi_version of this CurrentVersion.  # noqa: E501
        :rtype: str
        """
        return self._threedi_version

    @threedi_version.setter
    def threedi_version(self, threedi_version):
        """Sets the threedi_version of this CurrentVersion.


        :param threedi_version: The threedi_version of this CurrentVersion.  # noqa: E501
        :type: str
        """

        self._threedi_version = threedi_version

    @property
    def threedicore_version(self):
        """Gets the threedicore_version of this CurrentVersion.  # noqa: E501


        :return: The threedicore_version of this CurrentVersion.  # noqa: E501
        :rtype: str
        """
        return self._threedicore_version

    @threedicore_version.setter
    def threedicore_version(self, threedicore_version):
        """Sets the threedicore_version of this CurrentVersion.


        :param threedicore_version: The threedicore_version of this CurrentVersion.  # noqa: E501
        :type: str
        """

        self._threedicore_version = threedicore_version

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
        if not isinstance(other, CurrentVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrentVersion):
            return True

        return self.to_dict() != other.to_dict()
