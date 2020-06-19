# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.7   3Di core release: 2.0.9  deployed on:  02:04PM (UTC) on June 16, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class File(object):
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
        'storage_name': 'str',
        'filename': 'str',
        'bucket': 'str',
        'prefix': 'str',
        'etag': 'str',
        'size': 'int',
        'expiry_date': 'date',
        'related_object': 'str',
        'type': 'str',
        'state': 'str',
        'state_description': 'str',
        'meta': 'object',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'storage_name': 'storage_name',
        'filename': 'filename',
        'bucket': 'bucket',
        'prefix': 'prefix',
        'etag': 'etag',
        'size': 'size',
        'expiry_date': 'expiry_date',
        'related_object': 'related_object',
        'type': 'type',
        'state': 'state',
        'state_description': 'state_description',
        'meta': 'meta',
        'id': 'id'
    }

    def __init__(self, url=None, storage_name=None, filename=None, bucket=None, prefix=None, etag=None, size=None, expiry_date=None, related_object=None, type=None, state=None, state_description=None, meta=None, id=None):  # noqa: E501
        """File - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._storage_name = None
        self._filename = None
        self._bucket = None
        self._prefix = None
        self._etag = None
        self._size = None
        self._expiry_date = None
        self._related_object = None
        self._type = None
        self._state = None
        self._state_description = None
        self._meta = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if storage_name is not None:
            self.storage_name = storage_name
        self.filename = filename
        self.bucket = bucket
        self.prefix = prefix
        self.etag = etag
        self.size = size
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if related_object is not None:
            self.related_object = related_object
        self.type = type
        self.state = state
        self.state_description = state_description
        self.meta = meta
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this File.  # noqa: E501


        :return: The url of this File.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this File.


        :param url: The url of this File.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def storage_name(self):
        """Gets the storage_name of this File.  # noqa: E501


        :return: The storage_name of this File.  # noqa: E501
        :rtype: str
        """
        return self._storage_name

    @storage_name.setter
    def storage_name(self, storage_name):
        """Sets the storage_name of this File.


        :param storage_name: The storage_name of this File.  # noqa: E501
        :type: str
        """
        if storage_name is not None and len(storage_name) < 1:
            raise ValueError("Invalid value for `storage_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._storage_name = storage_name

    @property
    def filename(self):
        """Gets the filename of this File.  # noqa: E501


        :return: The filename of this File.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this File.


        :param filename: The filename of this File.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501
        if filename is not None and len(filename) > 256:
            raise ValueError("Invalid value for `filename`, length must be less than or equal to `256`")  # noqa: E501
        if filename is not None and len(filename) < 1:
            raise ValueError("Invalid value for `filename`, length must be greater than or equal to `1`")  # noqa: E501

        self._filename = filename

    @property
    def bucket(self):
        """Gets the bucket of this File.  # noqa: E501


        :return: The bucket of this File.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this File.


        :param bucket: The bucket of this File.  # noqa: E501
        :type: str
        """
        if bucket is None:
            raise ValueError("Invalid value for `bucket`, must not be `None`")  # noqa: E501
        if bucket is not None and len(bucket) > 256:
            raise ValueError("Invalid value for `bucket`, length must be less than or equal to `256`")  # noqa: E501
        if bucket is not None and len(bucket) < 1:
            raise ValueError("Invalid value for `bucket`, length must be greater than or equal to `1`")  # noqa: E501

        self._bucket = bucket

    @property
    def prefix(self):
        """Gets the prefix of this File.  # noqa: E501


        :return: The prefix of this File.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this File.


        :param prefix: The prefix of this File.  # noqa: E501
        :type: str
        """
        if prefix is not None and len(prefix) > 256:
            raise ValueError("Invalid value for `prefix`, length must be less than or equal to `256`")  # noqa: E501

        self._prefix = prefix

    @property
    def etag(self):
        """Gets the etag of this File.  # noqa: E501

        Optional eTag (md5sum)  # noqa: E501

        :return: The etag of this File.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this File.

        Optional eTag (md5sum)  # noqa: E501

        :param etag: The etag of this File.  # noqa: E501
        :type: str
        """
        if etag is not None and len(etag) > 256:
            raise ValueError("Invalid value for `etag`, length must be less than or equal to `256`")  # noqa: E501

        self._etag = etag

    @property
    def size(self):
        """Gets the size of this File.  # noqa: E501

        Filesize in bytes  # noqa: E501

        :return: The size of this File.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this File.

        Filesize in bytes  # noqa: E501

        :param size: The size of this File.  # noqa: E501
        :type: int
        """
        if size is not None and size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if size is not None and size < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._size = size

    @property
    def expiry_date(self):
        """Gets the expiry_date of this File.  # noqa: E501


        :return: The expiry_date of this File.  # noqa: E501
        :rtype: date
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this File.


        :param expiry_date: The expiry_date of this File.  # noqa: E501
        :type: date
        """

        self._expiry_date = expiry_date

    @property
    def related_object(self):
        """Gets the related_object of this File.  # noqa: E501


        :return: The related_object of this File.  # noqa: E501
        :rtype: str
        """
        return self._related_object

    @related_object.setter
    def related_object(self, related_object):
        """Sets the related_object of this File.


        :param related_object: The related_object of this File.  # noqa: E501
        :type: str
        """

        self._related_object = related_object

    @property
    def type(self):
        """Gets the type of this File.  # noqa: E501


        :return: The type of this File.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this File.


        :param type: The type of this File.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["timeseries", "rastertimeseries", "savedstate", "results", "rasters", "gridadmin", "geojson", "initialwaterlevel"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def state(self):
        """Gets the state of this File.  # noqa: E501


        :return: The state of this File.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this File.


        :param state: The state of this File.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["created", "uploaded", "processed", "error", "removed"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_description(self):
        """Gets the state_description of this File.  # noqa: E501


        :return: The state_description of this File.  # noqa: E501
        :rtype: str
        """
        return self._state_description

    @state_description.setter
    def state_description(self, state_description):
        """Sets the state_description of this File.


        :param state_description: The state_description of this File.  # noqa: E501
        :type: str
        """
        if state_description is not None and len(state_description) > 512:
            raise ValueError("Invalid value for `state_description`, length must be less than or equal to `512`")  # noqa: E501

        self._state_description = state_description

    @property
    def meta(self):
        """Gets the meta of this File.  # noqa: E501


        :return: The meta of this File.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this File.


        :param meta: The meta of this File.  # noqa: E501
        :type: object
        """

        self._meta = meta

    @property
    def id(self):
        """Gets the id of this File.  # noqa: E501


        :return: The id of this File.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this File.


        :param id: The id of this File.  # noqa: E501
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
        if not isinstance(other, File):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
