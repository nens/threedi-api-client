# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.1.1   3Di core release: 2.1.9  deployed on:  02:45PM (UTC) on December 08, 2021  # noqa: E501

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

class RevisionTask(object):
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
        'params': 'object',
        'created': 'datetime',
        'last_updated': 'datetime',
        'status': 'str',
        'detail': 'object',
        'revision': 'str',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'name': 'name',
        'params': 'params',
        'created': 'created',
        'last_updated': 'last_updated',
        'status': 'status',
        'detail': 'detail',
        'revision': 'revision',
        'id': 'id'
    }

    def __init__(self, url=None, name=None, params=None, created=None, last_updated=None, status=None, detail=None, revision=None, id=None, local_vars_configuration=None):  # noqa: E501
        """RevisionTask - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._name = None
        self._params = None
        self._created = None
        self._last_updated = None
        self._status = None
        self._detail = None
        self._revision = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.name = name
        self.params = params
        if created is not None:
            self.created = created
        if last_updated is not None:
            self.last_updated = last_updated
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
        if revision is not None:
            self.revision = revision
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this RevisionTask.  # noqa: E501


        :return: The url of this RevisionTask.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RevisionTask.


        :param url: The url of this RevisionTask.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this RevisionTask.  # noqa: E501


        :return: The name of this RevisionTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RevisionTask.


        :param name: The name of this RevisionTask.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        allowed_values = ["modelchecker"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and name not in allowed_values:  # noqa: E501
            logger.warning(
                "Warning: Unknown value for `name` ({0}), must be one of {1}. Either your threedi-api-client version is out of date or this value is invalid."  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def params(self):
        """Gets the params of this RevisionTask.  # noqa: E501


        :return: The params of this RevisionTask.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this RevisionTask.


        :param params: The params of this RevisionTask.  # noqa: E501
        :type: object
        """

        self._params = params

    @property
    def created(self):
        """Gets the created of this RevisionTask.  # noqa: E501


        :return: The created of this RevisionTask.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RevisionTask.


        :param created: The created of this RevisionTask.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this RevisionTask.  # noqa: E501


        :return: The last_updated of this RevisionTask.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this RevisionTask.


        :param last_updated: The last_updated of this RevisionTask.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def status(self):
        """Gets the status of this RevisionTask.  # noqa: E501


        :return: The status of this RevisionTask.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RevisionTask.


        :param status: The status of this RevisionTask.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "received", "started", "success", "failure", "revoked"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            logger.warning(
                "Warning: Unknown value for `status` ({0}), must be one of {1}. Either your threedi-api-client version is out of date or this value is invalid."  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this RevisionTask.  # noqa: E501


        :return: The detail of this RevisionTask.  # noqa: E501
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this RevisionTask.


        :param detail: The detail of this RevisionTask.  # noqa: E501
        :type: object
        """

        self._detail = detail

    @property
    def revision(self):
        """Gets the revision of this RevisionTask.  # noqa: E501


        :return: The revision of this RevisionTask.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this RevisionTask.


        :param revision: The revision of this RevisionTask.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def id(self):
        """Gets the id of this RevisionTask.  # noqa: E501


        :return: The id of this RevisionTask.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RevisionTask.


        :param id: The id of this RevisionTask.  # noqa: E501
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
        if not isinstance(other, RevisionTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RevisionTask):
            return True

        return self.to_dict() != other.to_dict()
