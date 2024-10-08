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

class UploadEventFile(object):
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
        'put_url': 'str',
        'filename': 'str',
        'status': 'str',
        'offset': 'int',
        'periodic': 'str'
    }

    required_fields = [
       'filename',
       'offset',
    ]

    attribute_map = {
        'put_url': 'put_url',
        'filename': 'filename',
        'status': 'status',
        'offset': 'offset',
        'periodic': 'periodic'
    }

    def __init__(self, put_url=None, filename=None, status=None, offset=None, periodic=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """UploadEventFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._put_url = None
        self._filename = None
        self._status = None
        self._offset = None
        self._periodic = None
        self.discriminator = None

        if put_url is not None:
            self.put_url = put_url
        self.filename = filename
        if status is not None:
            self.status = status
        self.offset = offset
        if periodic is not None:
            self.periodic = periodic

    @property
    def put_url(self):
        """Gets the put_url of this UploadEventFile.  # noqa: E501


        :return: The put_url of this UploadEventFile.  # noqa: E501
        :rtype: str
        """
        return self._put_url

    @put_url.setter
    def put_url(self, put_url):
        """Sets the put_url of this UploadEventFile.


        :param put_url: The put_url of this UploadEventFile.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                put_url is not None and len(put_url) < 1):
            self.__handle_validation_error("Invalid value for `put_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._put_url = put_url

    @property
    def filename(self):
        """Gets the filename of this UploadEventFile.  # noqa: E501


        :return: The filename of this UploadEventFile.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this UploadEventFile.


        :param filename: The filename of this UploadEventFile.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and filename is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `filename`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filename is not None and len(filename) > 255):
            self.__handle_validation_error("Invalid value for `filename`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filename is not None and len(filename) < 1):
            self.__handle_validation_error("Invalid value for `filename`, length must be greater than or equal to `1`")  # noqa: E501

        self._filename = filename

    @property
    def status(self):
        """Gets the status of this UploadEventFile.  # noqa: E501


        :return: The status of this UploadEventFile.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UploadEventFile.


        :param status: The status of this UploadEventFile.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            self.__handle_validation_error("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def offset(self):
        """Gets the offset of this UploadEventFile.  # noqa: E501


        :return: The offset of this UploadEventFile.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this UploadEventFile.


        :param offset: The offset of this UploadEventFile.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def periodic(self):
        """Gets the periodic of this UploadEventFile.  # noqa: E501


        :return: The periodic of this UploadEventFile.  # noqa: E501
        :rtype: str
        """
        return self._periodic

    @periodic.setter
    def periodic(self, periodic):
        """Sets the periodic of this UploadEventFile.


        :param periodic: The periodic of this UploadEventFile.  # noqa: E501
        :type: str
        """
        allowed_values = ["daily"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and periodic not in allowed_values:  # noqa: E501
            self.__handle_validation_error(
                "Invalid value for `periodic` ({0}), must be one of {1}"  # noqa: E501
                .format(periodic, allowed_values)
            )

        self._periodic = periodic

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
        if not isinstance(other, UploadEventFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadEventFile):
            return True

        return self.to_dict() != other.to_dict()
