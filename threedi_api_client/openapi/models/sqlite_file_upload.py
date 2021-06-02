# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 1.0.16   3Di core release: 2.0.11  deployed on:  07:33AM (UTC) on September 04, 2020  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from threedi_api_client.openapi.configuration import Configuration


class SqliteFileUpload(object):
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
        'uncompressed_md5sum': 'str'
    }

    attribute_map = {
        'put_url': 'put_url',
        'filename': 'filename',
        'status': 'status',
        'uncompressed_md5sum': 'uncompressed_md5sum'
    }

    def __init__(self, put_url=None, filename=None, status=None, uncompressed_md5sum=None, local_vars_configuration=None):  # noqa: E501
        """SqliteFileUpload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._put_url = None
        self._filename = None
        self._status = None
        self._uncompressed_md5sum = None
        self.discriminator = None

        if put_url is not None:
            self.put_url = put_url
        self.filename = filename
        if status is not None:
            self.status = status
        if uncompressed_md5sum is not None:
            self.uncompressed_md5sum = uncompressed_md5sum

    @property
    def put_url(self):
        """Gets the put_url of this SqliteFileUpload.  # noqa: E501


        :return: The put_url of this SqliteFileUpload.  # noqa: E501
        :rtype: str
        """
        return self._put_url

    @put_url.setter
    def put_url(self, put_url):
        """Sets the put_url of this SqliteFileUpload.


        :param put_url: The put_url of this SqliteFileUpload.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                put_url is not None and len(put_url) < 1):
            raise ValueError("Invalid value for `put_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._put_url = put_url

    @property
    def filename(self):
        """Gets the filename of this SqliteFileUpload.  # noqa: E501


        :return: The filename of this SqliteFileUpload.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this SqliteFileUpload.


        :param filename: The filename of this SqliteFileUpload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and filename is None:  # noqa: E501
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filename is not None and len(filename) > 255):
            raise ValueError("Invalid value for `filename`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filename is not None and len(filename) < 1):
            raise ValueError("Invalid value for `filename`, length must be greater than or equal to `1`")  # noqa: E501

        self._filename = filename

    @property
    def status(self):
        """Gets the status of this SqliteFileUpload.  # noqa: E501


        :return: The status of this SqliteFileUpload.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SqliteFileUpload.


        :param status: The status of this SqliteFileUpload.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def uncompressed_md5sum(self):
        """Gets the uncompressed_md5sum of this SqliteFileUpload.  # noqa: E501


        :return: The uncompressed_md5sum of this SqliteFileUpload.  # noqa: E501
        :rtype: str
        """
        return self._uncompressed_md5sum

    @uncompressed_md5sum.setter
    def uncompressed_md5sum(self, uncompressed_md5sum):
        """Sets the uncompressed_md5sum of this SqliteFileUpload.


        :param uncompressed_md5sum: The uncompressed_md5sum of this SqliteFileUpload.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                uncompressed_md5sum is not None and len(uncompressed_md5sum) > 256):
            raise ValueError("Invalid value for `uncompressed_md5sum`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                uncompressed_md5sum is not None and len(uncompressed_md5sum) < 1):
            raise ValueError("Invalid value for `uncompressed_md5sum`, length must be greater than or equal to `1`")  # noqa: E501

        self._uncompressed_md5sum = uncompressed_md5sum

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
        if not isinstance(other, SqliteFileUpload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SqliteFileUpload):
            return True

        return self.to_dict() != other.to_dict()
