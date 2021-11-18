# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.0.5   3Di core release: 2.1.7  deployed on:  09:40AM (UTC) on November 18, 2021  # noqa: E501

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

class Simulation(object):
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
        'slug': 'str',
        'uuid': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'created': 'str',
        'threedimodel': 'str',
        'organisation': 'str',
        'organisation_name': 'str',
        'user': 'str',
        'start_datetime': 'datetime',
        'end_datetime': 'datetime',
        'duration': 'int',
        'duration_humanized': 'str',
        'threedimodel_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'slug': 'slug',
        'uuid': 'uuid',
        'name': 'name',
        'tags': 'tags',
        'created': 'created',
        'threedimodel': 'threedimodel',
        'organisation': 'organisation',
        'organisation_name': 'organisation_name',
        'user': 'user',
        'start_datetime': 'start_datetime',
        'end_datetime': 'end_datetime',
        'duration': 'duration',
        'duration_humanized': 'duration_humanized',
        'threedimodel_id': 'threedimodel_id',
        'id': 'id'
    }

    def __init__(self, url=None, slug=None, uuid=None, name=None, tags=None, created=None, threedimodel=None, organisation=None, organisation_name=None, user=None, start_datetime=None, end_datetime=None, duration=None, duration_humanized=None, threedimodel_id=None, id=None, local_vars_configuration=None):  # noqa: E501
        """Simulation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._slug = None
        self._uuid = None
        self._name = None
        self._tags = None
        self._created = None
        self._threedimodel = None
        self._organisation = None
        self._organisation_name = None
        self._user = None
        self._start_datetime = None
        self._end_datetime = None
        self._duration = None
        self._duration_humanized = None
        self._threedimodel_id = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if slug is not None:
            self.slug = slug
        if uuid is not None:
            self.uuid = uuid
        self.name = name
        if tags is not None:
            self.tags = tags
        if created is not None:
            self.created = created
        self.threedimodel = threedimodel
        self.organisation = organisation
        if organisation_name is not None:
            self.organisation_name = organisation_name
        if user is not None:
            self.user = user
        self.start_datetime = start_datetime
        if end_datetime is not None:
            self.end_datetime = end_datetime
        if duration is not None:
            self.duration = duration
        if duration_humanized is not None:
            self.duration_humanized = duration_humanized
        if threedimodel_id is not None:
            self.threedimodel_id = threedimodel_id
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this Simulation.  # noqa: E501


        :return: The url of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Simulation.


        :param url: The url of this Simulation.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def slug(self):
        """Gets the slug of this Simulation.  # noqa: E501


        :return: The slug of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Simulation.


        :param slug: The slug of this Simulation.  # noqa: E501
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
    def uuid(self):
        """Gets the uuid of this Simulation.  # noqa: E501


        :return: The uuid of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Simulation.


        :param uuid: The uuid of this Simulation.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this Simulation.  # noqa: E501


        :return: The name of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Simulation.


        :param name: The name of this Simulation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this Simulation.  # noqa: E501

        tags provided as a list of strings  # noqa: E501

        :return: The tags of this Simulation.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Simulation.

        tags provided as a list of strings  # noqa: E501

        :param tags: The tags of this Simulation.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def created(self):
        """Gets the created of this Simulation.  # noqa: E501


        :return: The created of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Simulation.


        :param created: The created of this Simulation.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def threedimodel(self):
        """Gets the threedimodel of this Simulation.  # noqa: E501

        The id of a threedimodel  # noqa: E501

        :return: The threedimodel of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._threedimodel

    @threedimodel.setter
    def threedimodel(self, threedimodel):
        """Sets the threedimodel of this Simulation.

        The id of a threedimodel  # noqa: E501

        :param threedimodel: The threedimodel of this Simulation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and threedimodel is None:  # noqa: E501
            raise ValueError("Invalid value for `threedimodel`, must not be `None`")  # noqa: E501

        self._threedimodel = threedimodel

    @property
    def organisation(self):
        """Gets the organisation of this Simulation.  # noqa: E501

        The unique_id of an organisation  # noqa: E501

        :return: The organisation of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this Simulation.

        The unique_id of an organisation  # noqa: E501

        :param organisation: The organisation of this Simulation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organisation is None:  # noqa: E501
            raise ValueError("Invalid value for `organisation`, must not be `None`")  # noqa: E501

        self._organisation = organisation

    @property
    def organisation_name(self):
        """Gets the organisation_name of this Simulation.  # noqa: E501


        :return: The organisation_name of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._organisation_name

    @organisation_name.setter
    def organisation_name(self, organisation_name):
        """Sets the organisation_name of this Simulation.


        :param organisation_name: The organisation_name of this Simulation.  # noqa: E501
        :type: str
        """

        self._organisation_name = organisation_name

    @property
    def user(self):
        """Gets the user of this Simulation.  # noqa: E501

        The username of a user  # noqa: E501

        :return: The user of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Simulation.

        The username of a user  # noqa: E501

        :param user: The user of this Simulation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                user is not None and not re.search(r'^[\w.@+-]+$', user)):  # noqa: E501
            raise ValueError(r"Invalid value for `user`, must be a follow pattern or equal to `/^[\w.@+-]+$/`")  # noqa: E501

        self._user = user

    @property
    def start_datetime(self):
        """Gets the start_datetime of this Simulation.  # noqa: E501


        :return: The start_datetime of this Simulation.  # noqa: E501
        :rtype: datetime
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        """Sets the start_datetime of this Simulation.


        :param start_datetime: The start_datetime of this Simulation.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_datetime is None:  # noqa: E501
            raise ValueError("Invalid value for `start_datetime`, must not be `None`")  # noqa: E501

        self._start_datetime = start_datetime

    @property
    def end_datetime(self):
        """Gets the end_datetime of this Simulation.  # noqa: E501


        :return: The end_datetime of this Simulation.  # noqa: E501
        :rtype: datetime
        """
        return self._end_datetime

    @end_datetime.setter
    def end_datetime(self, end_datetime):
        """Sets the end_datetime of this Simulation.


        :param end_datetime: The end_datetime of this Simulation.  # noqa: E501
        :type: datetime
        """

        self._end_datetime = end_datetime

    @property
    def duration(self):
        """Gets the duration of this Simulation.  # noqa: E501


        :return: The duration of this Simulation.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Simulation.


        :param duration: The duration of this Simulation.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def duration_humanized(self):
        """Gets the duration_humanized of this Simulation.  # noqa: E501


        :return: The duration_humanized of this Simulation.  # noqa: E501
        :rtype: str
        """
        return self._duration_humanized

    @duration_humanized.setter
    def duration_humanized(self, duration_humanized):
        """Sets the duration_humanized of this Simulation.


        :param duration_humanized: The duration_humanized of this Simulation.  # noqa: E501
        :type: str
        """

        self._duration_humanized = duration_humanized

    @property
    def threedimodel_id(self):
        """Gets the threedimodel_id of this Simulation.  # noqa: E501


        :return: The threedimodel_id of this Simulation.  # noqa: E501
        :rtype: int
        """
        return self._threedimodel_id

    @threedimodel_id.setter
    def threedimodel_id(self, threedimodel_id):
        """Sets the threedimodel_id of this Simulation.


        :param threedimodel_id: The threedimodel_id of this Simulation.  # noqa: E501
        :type: int
        """

        self._threedimodel_id = threedimodel_id

    @property
    def id(self):
        """Gets the id of this Simulation.  # noqa: E501


        :return: The id of this Simulation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Simulation.


        :param id: The id of this Simulation.  # noqa: E501
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
        if not isinstance(other, Simulation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Simulation):
            return True

        return self.to_dict() != other.to_dict()
