# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.15.1   3Di core release: 2.2.4  deployed on:  01:07PM (UTC) on January 26, 2022  # noqa: E501

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

class FromTemplate(object):
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
        'template': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'organisation': 'str',
        'start_datetime': 'datetime',
        'end_datetime': 'datetime',
        'duration': 'int',
        'clone_events': 'bool',
        'clone_initials': 'bool',
        'clone_settings': 'bool'
    }

    attribute_map = {
        'template': 'template',
        'name': 'name',
        'tags': 'tags',
        'organisation': 'organisation',
        'start_datetime': 'start_datetime',
        'end_datetime': 'end_datetime',
        'duration': 'duration',
        'clone_events': 'clone_events',
        'clone_initials': 'clone_initials',
        'clone_settings': 'clone_settings'
    }

    def __init__(self, template=None, name=None, tags=None, organisation=None, start_datetime=None, end_datetime=None, duration=None, clone_events=True, clone_initials=True, clone_settings=True, local_vars_configuration=None):  # noqa: E501
        """FromTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._template = None
        self._name = None
        self._tags = None
        self._organisation = None
        self._start_datetime = None
        self._end_datetime = None
        self._duration = None
        self._clone_events = None
        self._clone_initials = None
        self._clone_settings = None
        self.discriminator = None

        self.template = template
        self.name = name
        if tags is not None:
            self.tags = tags
        self.organisation = organisation
        self.start_datetime = start_datetime
        if end_datetime is not None:
            self.end_datetime = end_datetime
        if duration is not None:
            self.duration = duration
        if clone_events is not None:
            self.clone_events = clone_events
        if clone_initials is not None:
            self.clone_initials = clone_initials
        if clone_settings is not None:
            self.clone_settings = clone_settings

    @property
    def template(self):
        """Gets the template of this FromTemplate.  # noqa: E501

        source simulation template id  # noqa: E501

        :return: The template of this FromTemplate.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this FromTemplate.

        source simulation template id  # noqa: E501

        :param template: The template of this FromTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and template is None:  # noqa: E501
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def name(self):
        """Gets the name of this FromTemplate.  # noqa: E501


        :return: The name of this FromTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FromTemplate.


        :param name: The name of this FromTemplate.  # noqa: E501
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
        """Gets the tags of this FromTemplate.  # noqa: E501


        :return: The tags of this FromTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FromTemplate.


        :param tags: The tags of this FromTemplate.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def organisation(self):
        """Gets the organisation of this FromTemplate.  # noqa: E501


        :return: The organisation of this FromTemplate.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this FromTemplate.


        :param organisation: The organisation of this FromTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organisation is None:  # noqa: E501
            raise ValueError("Invalid value for `organisation`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                organisation is not None and len(organisation) < 1):
            raise ValueError("Invalid value for `organisation`, length must be greater than or equal to `1`")  # noqa: E501

        self._organisation = organisation

    @property
    def start_datetime(self):
        """Gets the start_datetime of this FromTemplate.  # noqa: E501


        :return: The start_datetime of this FromTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        """Sets the start_datetime of this FromTemplate.


        :param start_datetime: The start_datetime of this FromTemplate.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_datetime is None:  # noqa: E501
            raise ValueError("Invalid value for `start_datetime`, must not be `None`")  # noqa: E501

        self._start_datetime = start_datetime

    @property
    def end_datetime(self):
        """Gets the end_datetime of this FromTemplate.  # noqa: E501


        :return: The end_datetime of this FromTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._end_datetime

    @end_datetime.setter
    def end_datetime(self, end_datetime):
        """Sets the end_datetime of this FromTemplate.


        :param end_datetime: The end_datetime of this FromTemplate.  # noqa: E501
        :type: datetime
        """

        self._end_datetime = end_datetime

    @property
    def duration(self):
        """Gets the duration of this FromTemplate.  # noqa: E501


        :return: The duration of this FromTemplate.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this FromTemplate.


        :param duration: The duration of this FromTemplate.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def clone_events(self):
        """Gets the clone_events of this FromTemplate.  # noqa: E501


        :return: The clone_events of this FromTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._clone_events

    @clone_events.setter
    def clone_events(self, clone_events):
        """Sets the clone_events of this FromTemplate.


        :param clone_events: The clone_events of this FromTemplate.  # noqa: E501
        :type: bool
        """

        self._clone_events = clone_events

    @property
    def clone_initials(self):
        """Gets the clone_initials of this FromTemplate.  # noqa: E501


        :return: The clone_initials of this FromTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._clone_initials

    @clone_initials.setter
    def clone_initials(self, clone_initials):
        """Sets the clone_initials of this FromTemplate.


        :param clone_initials: The clone_initials of this FromTemplate.  # noqa: E501
        :type: bool
        """

        self._clone_initials = clone_initials

    @property
    def clone_settings(self):
        """Gets the clone_settings of this FromTemplate.  # noqa: E501


        :return: The clone_settings of this FromTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._clone_settings

    @clone_settings.setter
    def clone_settings(self, clone_settings):
        """Sets the clone_settings of this FromTemplate.


        :param clone_settings: The clone_settings of this FromTemplate.  # noqa: E501
        :type: bool
        """

        self._clone_settings = clone_settings

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
        if not isinstance(other, FromTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FromTemplate):
            return True

        return self.to_dict() != other.to_dict()
