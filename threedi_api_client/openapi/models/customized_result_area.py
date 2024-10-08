# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.4.3   3Di core release: 3.5.0  deployed on:  03:07PM (UTC) on October 02, 2024  # noqa: E501

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

class CustomizedResultArea(object):
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
        'subsets': 'list[str]',
        'geometry': 'str'
    }

    required_fields = [
       'name',
       'subsets',
       'geometry'
    ]

    attribute_map = {
        'url': 'url',
        'name': 'name',
        'subsets': 'subsets',
        'geometry': 'geometry'
    }

    def __init__(self, url=None, name=None, subsets=None, geometry=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """CustomizedResultArea - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._name = None
        self._subsets = None
        self._geometry = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.name = name
        self.subsets = subsets
        self.geometry = geometry

    @property
    def url(self):
        """Gets the url of this CustomizedResultArea.  # noqa: E501


        :return: The url of this CustomizedResultArea.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CustomizedResultArea.


        :param url: The url of this CustomizedResultArea.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this CustomizedResultArea.  # noqa: E501

        Name of the customized results area.  # noqa: E501

        :return: The name of this CustomizedResultArea.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomizedResultArea.

        Name of the customized results area.  # noqa: E501

        :param name: The name of this CustomizedResultArea.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            self.__handle_validation_error("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            self.__handle_validation_error("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def subsets(self):
        """Gets the subsets of this CustomizedResultArea.  # noqa: E501

        The subsets for which the customized results area is defined.  # noqa: E501

        :return: The subsets of this CustomizedResultArea.  # noqa: E501
        :rtype: list[str]
        """
        return self._subsets

    @subsets.setter
    def subsets(self, subsets):
        """Sets the subsets of this CustomizedResultArea.

        The subsets for which the customized results area is defined.  # noqa: E501

        :param subsets: The subsets of this CustomizedResultArea.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and subsets is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `subsets`, must not be `None`")  # noqa: E501
        allowed_values = ["1D", "2D", "1D2D", "GW"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(subsets).issubset(set(allowed_values))):  # noqa: E501
            self.__handle_validation_error(
                "Invalid values for `subsets` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(subsets) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._subsets = subsets

    @property
    def geometry(self):
        """Gets the geometry of this CustomizedResultArea.  # noqa: E501

        The geometry of the customized results area.  # noqa: E501

        :return: The geometry of this CustomizedResultArea.  # noqa: E501
        :rtype: str
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this CustomizedResultArea.

        The geometry of the customized results area.  # noqa: E501

        :param geometry: The geometry of this CustomizedResultArea.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and geometry is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `geometry`, must not be `None`")  # noqa: E501

        self._geometry = geometry

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
        if not isinstance(other, CustomizedResultArea):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomizedResultArea):
            return True

        return self.to_dict() != other.to_dict()
