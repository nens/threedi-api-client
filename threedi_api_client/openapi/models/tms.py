# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.4.40   3Di core release: 3.6.6  deployed on:  02:50PM (UTC) on March 25, 2025  # noqa: E501

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

class TMS(object):
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
        'tms_url': 'str',
        'minmax_url': 'str'
    }

    required_fields = [
       'tms_url',
       'minmax_url'
    ]

    attribute_map = {
        'tms_url': 'tms_url',
        'minmax_url': 'minmax_url'
    }

    def __init__(self, tms_url=None, minmax_url=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """TMS - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._tms_url = None
        self._minmax_url = None
        self.discriminator = None

        self.tms_url = tms_url
        self.minmax_url = minmax_url

    @property
    def tms_url(self):
        """Gets the tms_url of this TMS.  # noqa: E501


        :return: The tms_url of this TMS.  # noqa: E501
        :rtype: str
        """
        return self._tms_url

    @tms_url.setter
    def tms_url(self, tms_url):
        """Sets the tms_url of this TMS.


        :param tms_url: The tms_url of this TMS.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tms_url is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `tms_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tms_url is not None and len(tms_url) < 1):
            self.__handle_validation_error("Invalid value for `tms_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._tms_url = tms_url

    @property
    def minmax_url(self):
        """Gets the minmax_url of this TMS.  # noqa: E501


        :return: The minmax_url of this TMS.  # noqa: E501
        :rtype: str
        """
        return self._minmax_url

    @minmax_url.setter
    def minmax_url(self, minmax_url):
        """Sets the minmax_url of this TMS.


        :param minmax_url: The minmax_url of this TMS.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and minmax_url is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `minmax_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                minmax_url is not None and len(minmax_url) < 1):
            self.__handle_validation_error("Invalid value for `minmax_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._minmax_url = minmax_url

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
        if not isinstance(other, TMS):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TMS):
            return True

        return self.to_dict() != other.to_dict()
