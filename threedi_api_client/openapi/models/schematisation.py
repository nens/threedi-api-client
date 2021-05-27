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


class Schematisation(object):
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
        'owner': 'str',
        'name': 'str',
        'slug': 'str',
        'tags': 'str',
        'meta': 'object',
        'created_by': 'str',
        'created': 'datetime',
        'storage_usage': 'int'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'owner': 'owner',
        'name': 'name',
        'slug': 'slug',
        'tags': 'tags',
        'meta': 'meta',
        'created_by': 'created_by',
        'created': 'created',
        'storage_usage': 'storage_usage'
    }

    def __init__(self, url=None, id=None, owner=None, name=None, slug=None, tags=None, meta=None, created_by=None, created=None, storage_usage=None, local_vars_configuration=None):  # noqa: E501
        """Schematisation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._id = None
        self._owner = None
        self._name = None
        self._slug = None
        self._tags = None
        self._meta = None
        self._created_by = None
        self._created = None
        self._storage_usage = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        self.name = name
        if slug is not None:
            self.slug = slug
        if tags is not None:
            self.tags = tags
        self.meta = meta
        if created_by is not None:
            self.created_by = created_by
        if created is not None:
            self.created = created
        if storage_usage is not None:
            self.storage_usage = storage_usage

    @property
    def url(self):
        """Gets the url of this Schematisation.  # noqa: E501


        :return: The url of this Schematisation.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Schematisation.


        :param url: The url of this Schematisation.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this Schematisation.  # noqa: E501


        :return: The id of this Schematisation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Schematisation.


        :param id: The id of this Schematisation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this Schematisation.  # noqa: E501

        The unique_id of an organisation  # noqa: E501

        :return: The owner of this Schematisation.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Schematisation.

        The unique_id of an organisation  # noqa: E501

        :param owner: The owner of this Schematisation.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def name(self):
        """Gets the name of this Schematisation.  # noqa: E501


        :return: The name of this Schematisation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Schematisation.


        :param name: The name of this Schematisation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Schematisation.  # noqa: E501

        do not change  # noqa: E501

        :return: The slug of this Schematisation.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Schematisation.

        do not change  # noqa: E501

        :param slug: The slug of this Schematisation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and len(slug) < 1):
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug)):  # noqa: E501
            raise ValueError(r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def tags(self):
        """Gets the tags of this Schematisation.  # noqa: E501


        :return: The tags of this Schematisation.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Schematisation.


        :param tags: The tags of this Schematisation.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def meta(self):
        """Gets the meta of this Schematisation.  # noqa: E501


        :return: The meta of this Schematisation.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Schematisation.


        :param meta: The meta of this Schematisation.  # noqa: E501
        :type: object
        """

        self._meta = meta

    @property
    def created_by(self):
        """Gets the created_by of this Schematisation.  # noqa: E501

        The username of a user  # noqa: E501

        :return: The created_by of this Schematisation.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Schematisation.

        The username of a user  # noqa: E501

        :param created_by: The created_by of this Schematisation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                created_by is not None and not re.search(r'^[\w.@+-]+$', created_by)):  # noqa: E501
            raise ValueError(r"Invalid value for `created_by`, must be a follow pattern or equal to `/^[\w.@+-]+$/`")  # noqa: E501

        self._created_by = created_by

    @property
    def created(self):
        """Gets the created of this Schematisation.  # noqa: E501


        :return: The created of this Schematisation.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Schematisation.


        :param created: The created of this Schematisation.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def storage_usage(self):
        """Gets the storage_usage of this Schematisation.  # noqa: E501

        Automatically calculated.  # noqa: E501

        :return: The storage_usage of this Schematisation.  # noqa: E501
        :rtype: int
        """
        return self._storage_usage

    @storage_usage.setter
    def storage_usage(self, storage_usage):
        """Sets the storage_usage of this Schematisation.

        Automatically calculated.  # noqa: E501

        :param storage_usage: The storage_usage of this Schematisation.  # noqa: E501
        :type: int
        """

        self._storage_usage = storage_usage

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
        if not isinstance(other, Schematisation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Schematisation):
            return True

        return self.to_dict() != other.to_dict()