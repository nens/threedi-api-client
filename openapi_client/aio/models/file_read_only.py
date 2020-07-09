# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.10   3Di core release: 2.0.10  deployed on:  09:44AM (UTC) on July 02, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.aio.configuration import Configuration


class FileReadOnly(object):
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
        'filename': 'str',
        'state': 'str',
        'state_description': 'str',
        'type': 'str',
        'size': 'int',
        'etag': 'str',
        'expiry_date': 'date',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'filename': 'filename',
        'state': 'state',
        'state_description': 'state_description',
        'type': 'type',
        'size': 'size',
        'etag': 'etag',
        'expiry_date': 'expiry_date',
        'id': 'id'
    }

    def __init__(self, url=None, filename=None, state=None, state_description=None, type=None, size=None, etag=None, expiry_date=None, id=None, local_vars_configuration=None):  # noqa: E501
        """FileReadOnly - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._filename = None
        self._state = None
        self._state_description = None
        self._type = None
        self._size = None
        self._etag = None
        self._expiry_date = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if filename is not None:
            self.filename = filename
        if state is not None:
            self.state = state
        self.state_description = state_description
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        self.etag = etag
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this FileReadOnly.  # noqa: E501


        :return: The url of this FileReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FileReadOnly.


        :param url: The url of this FileReadOnly.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def filename(self):
        """Gets the filename of this FileReadOnly.  # noqa: E501


        :return: The filename of this FileReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this FileReadOnly.


        :param filename: The filename of this FileReadOnly.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                filename is not None and len(filename) < 1):
            raise ValueError("Invalid value for `filename`, length must be greater than or equal to `1`")  # noqa: E501

        self._filename = filename

    @property
    def state(self):
        """Gets the state of this FileReadOnly.  # noqa: E501


        :return: The state of this FileReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FileReadOnly.


        :param state: The state of this FileReadOnly.  # noqa: E501
        :type: str
        """
        allowed_values = ["created", "uploaded", "processed", "error", "removed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_description(self):
        """Gets the state_description of this FileReadOnly.  # noqa: E501


        :return: The state_description of this FileReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._state_description

    @state_description.setter
    def state_description(self, state_description):
        """Sets the state_description of this FileReadOnly.


        :param state_description: The state_description of this FileReadOnly.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                state_description is not None and len(state_description) > 512):
            raise ValueError("Invalid value for `state_description`, length must be less than or equal to `512`")  # noqa: E501

        self._state_description = state_description

    @property
    def type(self):
        """Gets the type of this FileReadOnly.  # noqa: E501


        :return: The type of this FileReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileReadOnly.


        :param type: The type of this FileReadOnly.  # noqa: E501
        :type: str
        """
        allowed_values = ["timeseries", "rastertimeseries", "savedstate", "results", "rasters", "gridadmin", "geojson", "initialwaterlevel"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def size(self):
        """Gets the size of this FileReadOnly.  # noqa: E501

        Filesize in bytes  # noqa: E501

        :return: The size of this FileReadOnly.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileReadOnly.

        Filesize in bytes  # noqa: E501

        :param size: The size of this FileReadOnly.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def etag(self):
        """Gets the etag of this FileReadOnly.  # noqa: E501

        Optional eTag (md5sum)  # noqa: E501

        :return: The etag of this FileReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this FileReadOnly.

        Optional eTag (md5sum)  # noqa: E501

        :param etag: The etag of this FileReadOnly.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                etag is not None and len(etag) > 256):
            raise ValueError("Invalid value for `etag`, length must be less than or equal to `256`")  # noqa: E501

        self._etag = etag

    @property
    def expiry_date(self):
        """Gets the expiry_date of this FileReadOnly.  # noqa: E501


        :return: The expiry_date of this FileReadOnly.  # noqa: E501
        :rtype: date
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this FileReadOnly.


        :param expiry_date: The expiry_date of this FileReadOnly.  # noqa: E501
        :type: date
        """

        self._expiry_date = expiry_date

    @property
    def id(self):
        """Gets the id of this FileReadOnly.  # noqa: E501


        :return: The id of this FileReadOnly.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileReadOnly.


        :param id: The id of this FileReadOnly.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, FileReadOnly):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileReadOnly):
            return True

        return self.to_dict() != other.to_dict()
