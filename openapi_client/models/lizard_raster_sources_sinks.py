# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.16   3Di core release: 2.0.11  deployed on:  07:33AM (UTC) on September 04, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class LizardRasterSourcesSinks(object):
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
        "url": "str",
        "offset": "int",
        "duration": "int",
        "reference_uuid": "str",
        "start_datetime": "datetime",
        "simulation": "str",
        "interval": "int",
        "origin_offset": "int",
        "store_path": "str",
        "id": "int",
        "uid": "str",
        "user": "str",
    }

    attribute_map = {
        "url": "url",
        "offset": "offset",
        "duration": "duration",
        "reference_uuid": "reference_uuid",
        "start_datetime": "start_datetime",
        "simulation": "simulation",
        "interval": "interval",
        "origin_offset": "origin_offset",
        "store_path": "store_path",
        "id": "id",
        "uid": "uid",
        "user": "user",
    }

    def __init__(
        self,
        url=None,
        offset=None,
        duration=None,
        reference_uuid=None,
        start_datetime=None,
        simulation=None,
        interval=None,
        origin_offset=None,
        store_path=None,
        id=None,
        uid=None,
        user=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """LizardRasterSourcesSinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._offset = None
        self._duration = None
        self._reference_uuid = None
        self._start_datetime = None
        self._simulation = None
        self._interval = None
        self._origin_offset = None
        self._store_path = None
        self._id = None
        self._uid = None
        self._user = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.offset = offset
        self.duration = duration
        self.reference_uuid = reference_uuid
        self.start_datetime = start_datetime
        if simulation is not None:
            self.simulation = simulation
        if interval is not None:
            self.interval = interval
        if origin_offset is not None:
            self.origin_offset = origin_offset
        if store_path is not None:
            self.store_path = store_path
        if id is not None:
            self.id = id
        if uid is not None:
            self.uid = uid
        if user is not None:
            self.user = user

    @property
    def url(self):
        """Gets the url of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The url of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LizardRasterSourcesSinks.


        :param url: The url of this LizardRasterSourcesSinks.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def offset(self):
        """Gets the offset of this LizardRasterSourcesSinks.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this LizardRasterSourcesSinks.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this LizardRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and offset is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `offset`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and offset is not None
            and offset > 2147483647
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `offset`, must be a value less than or equal to `2147483647`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and offset is not None
            and offset < 0
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `offset`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._offset = offset

    @property
    def duration(self):
        """Gets the duration of this LizardRasterSourcesSinks.  # noqa: E501

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :return: The duration of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this LizardRasterSourcesSinks.

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :param duration: The duration of this LizardRasterSourcesSinks.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and duration is not None
            and duration > 9223372036854775807
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `duration`, must be a value less than or equal to `9223372036854775807`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and duration is not None
            and duration < -9223372036854775808
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `duration`, must be a value greater than or equal to `-9223372036854775808`"
            )  # noqa: E501

        self._duration = duration

    @property
    def reference_uuid(self):
        """Gets the reference_uuid of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The reference_uuid of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._reference_uuid

    @reference_uuid.setter
    def reference_uuid(self, reference_uuid):
        """Sets the reference_uuid of this LizardRasterSourcesSinks.


        :param reference_uuid: The reference_uuid of this LizardRasterSourcesSinks.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and reference_uuid is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `reference_uuid`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and reference_uuid is not None
            and len(reference_uuid) > 40
        ):
            raise ValueError(
                "Invalid value for `reference_uuid`, length must be less than or equal to `40`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and reference_uuid is not None
            and len(reference_uuid) < 1
        ):
            raise ValueError(
                "Invalid value for `reference_uuid`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._reference_uuid = reference_uuid

    @property
    def start_datetime(self):
        """Gets the start_datetime of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The start_datetime of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: datetime
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        """Sets the start_datetime of this LizardRasterSourcesSinks.


        :param start_datetime: The start_datetime of this LizardRasterSourcesSinks.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation
            and start_datetime is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `start_datetime`, must not be `None`"
            )  # noqa: E501

        self._start_datetime = start_datetime

    @property
    def simulation(self):
        """Gets the simulation of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The simulation of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this LizardRasterSourcesSinks.


        :param simulation: The simulation of this LizardRasterSourcesSinks.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def interval(self):
        """Gets the interval of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The interval of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this LizardRasterSourcesSinks.


        :param interval: The interval of this LizardRasterSourcesSinks.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def origin_offset(self):
        """Gets the origin_offset of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The origin_offset of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._origin_offset

    @origin_offset.setter
    def origin_offset(self, origin_offset):
        """Sets the origin_offset of this LizardRasterSourcesSinks.


        :param origin_offset: The origin_offset of this LizardRasterSourcesSinks.  # noqa: E501
        :type: int
        """

        self._origin_offset = origin_offset

    @property
    def store_path(self):
        """Gets the store_path of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The store_path of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._store_path

    @store_path.setter
    def store_path(self, store_path):
        """Sets the store_path of this LizardRasterSourcesSinks.


        :param store_path: The store_path of this LizardRasterSourcesSinks.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and store_path is not None
            and len(store_path) < 1
        ):
            raise ValueError(
                "Invalid value for `store_path`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._store_path = store_path

    @property
    def id(self):
        """Gets the id of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The id of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LizardRasterSourcesSinks.


        :param id: The id of this LizardRasterSourcesSinks.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uid(self):
        """Gets the uid of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The uid of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this LizardRasterSourcesSinks.


        :param uid: The uid of this LizardRasterSourcesSinks.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def user(self):
        """Gets the user of this LizardRasterSourcesSinks.  # noqa: E501


        :return: The user of this LizardRasterSourcesSinks.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LizardRasterSourcesSinks.


        :param user: The user of this LizardRasterSourcesSinks.  # noqa: E501
        :type: str
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, LizardRasterSourcesSinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LizardRasterSourcesSinks):
            return True

        return self.to_dict() != other.to_dict()
