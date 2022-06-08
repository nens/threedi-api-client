# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.19.3   3Di core release: 2.2.11  deployed on:  10:31AM (UTC) on June 01, 2022  # noqa: E501

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

class SimulationStatus(object):
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
        'simulation': 'str',
        'simulation_id': 'int',
        'simulation_name': 'str',
        'simulation_tags': 'list[str]',
        'threedimodel_slug': 'str',
        'threedimodel_id': 'int',
        'has_results': 'bool',
        'created': 'datetime',
        'expiry': 'datetime',
        'time': 'int',
        'paused': 'bool',
        'detail': 'object',
        'exit_code': 'int',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'name': 'name',
        'simulation': 'simulation',
        'simulation_id': 'simulation_id',
        'simulation_name': 'simulation_name',
        'simulation_tags': 'simulation_tags',
        'threedimodel_slug': 'threedimodel_slug',
        'threedimodel_id': 'threedimodel_id',
        'has_results': 'has_results',
        'created': 'created',
        'expiry': 'expiry',
        'time': 'time',
        'paused': 'paused',
        'detail': 'detail',
        'exit_code': 'exit_code',
        'id': 'id'
    }

    def __init__(self, url=None, name=None, simulation=None, simulation_id=None, simulation_name=None, simulation_tags=None, threedimodel_slug=None, threedimodel_id=None, has_results=None, created=None, expiry=None, time=None, paused=None, detail=None, exit_code=None, id=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """SimulationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._name = None
        self._simulation = None
        self._simulation_id = None
        self._simulation_name = None
        self._simulation_tags = None
        self._threedimodel_slug = None
        self._threedimodel_id = None
        self._has_results = None
        self._created = None
        self._expiry = None
        self._time = None
        self._paused = None
        self._detail = None
        self._exit_code = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.name = name
        if simulation is not None:
            self.simulation = simulation
        if simulation_id is not None:
            self.simulation_id = simulation_id
        if simulation_name is not None:
            self.simulation_name = simulation_name
        if simulation_tags is not None:
            self.simulation_tags = simulation_tags
        if threedimodel_slug is not None:
            self.threedimodel_slug = threedimodel_slug
        if threedimodel_id is not None:
            self.threedimodel_id = threedimodel_id
        self.has_results = has_results
        if created is not None:
            self.created = created
        self.expiry = expiry
        self.time = time
        self.paused = paused
        self.detail = detail
        self.exit_code = exit_code
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this SimulationStatus.  # noqa: E501


        :return: The url of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SimulationStatus.


        :param url: The url of this SimulationStatus.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this SimulationStatus.  # noqa: E501


        :return: The name of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimulationStatus.


        :param name: The name of this SimulationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `name`, must not be `None`")  # noqa: E501
        allowed_values = ["created", "starting", "initialized", "queued", "ended", "postprocessing", "finished", "crashed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and name not in allowed_values:  # noqa: E501
            self.__handle_validation_error(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def simulation(self):
        """Gets the simulation of this SimulationStatus.  # noqa: E501


        :return: The simulation of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this SimulationStatus.


        :param simulation: The simulation of this SimulationStatus.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def simulation_id(self):
        """Gets the simulation_id of this SimulationStatus.  # noqa: E501


        :return: The simulation_id of this SimulationStatus.  # noqa: E501
        :rtype: int
        """
        return self._simulation_id

    @simulation_id.setter
    def simulation_id(self, simulation_id):
        """Sets the simulation_id of this SimulationStatus.


        :param simulation_id: The simulation_id of this SimulationStatus.  # noqa: E501
        :type: int
        """

        self._simulation_id = simulation_id

    @property
    def simulation_name(self):
        """Gets the simulation_name of this SimulationStatus.  # noqa: E501


        :return: The simulation_name of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._simulation_name

    @simulation_name.setter
    def simulation_name(self, simulation_name):
        """Sets the simulation_name of this SimulationStatus.


        :param simulation_name: The simulation_name of this SimulationStatus.  # noqa: E501
        :type: str
        """

        self._simulation_name = simulation_name

    @property
    def simulation_tags(self):
        """Gets the simulation_tags of this SimulationStatus.  # noqa: E501


        :return: The simulation_tags of this SimulationStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._simulation_tags

    @simulation_tags.setter
    def simulation_tags(self, simulation_tags):
        """Sets the simulation_tags of this SimulationStatus.


        :param simulation_tags: The simulation_tags of this SimulationStatus.  # noqa: E501
        :type: list[str]
        """

        self._simulation_tags = simulation_tags

    @property
    def threedimodel_slug(self):
        """Gets the threedimodel_slug of this SimulationStatus.  # noqa: E501


        :return: The threedimodel_slug of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._threedimodel_slug

    @threedimodel_slug.setter
    def threedimodel_slug(self, threedimodel_slug):
        """Sets the threedimodel_slug of this SimulationStatus.


        :param threedimodel_slug: The threedimodel_slug of this SimulationStatus.  # noqa: E501
        :type: str
        """

        self._threedimodel_slug = threedimodel_slug

    @property
    def threedimodel_id(self):
        """Gets the threedimodel_id of this SimulationStatus.  # noqa: E501


        :return: The threedimodel_id of this SimulationStatus.  # noqa: E501
        :rtype: int
        """
        return self._threedimodel_id

    @threedimodel_id.setter
    def threedimodel_id(self, threedimodel_id):
        """Sets the threedimodel_id of this SimulationStatus.


        :param threedimodel_id: The threedimodel_id of this SimulationStatus.  # noqa: E501
        :type: int
        """

        self._threedimodel_id = threedimodel_id

    @property
    def has_results(self):
        """Gets the has_results of this SimulationStatus.  # noqa: E501


        :return: The has_results of this SimulationStatus.  # noqa: E501
        :rtype: bool
        """
        return self._has_results

    @has_results.setter
    def has_results(self, has_results):
        """Sets the has_results of this SimulationStatus.


        :param has_results: The has_results of this SimulationStatus.  # noqa: E501
        :type: bool
        """

        self._has_results = has_results

    @property
    def created(self):
        """Gets the created of this SimulationStatus.  # noqa: E501


        :return: The created of this SimulationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SimulationStatus.


        :param created: The created of this SimulationStatus.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def expiry(self):
        """Gets the expiry of this SimulationStatus.  # noqa: E501


        :return: The expiry of this SimulationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this SimulationStatus.


        :param expiry: The expiry of this SimulationStatus.  # noqa: E501
        :type: datetime
        """

        self._expiry = expiry

    @property
    def time(self):
        """Gets the time of this SimulationStatus.  # noqa: E501

        simulation time in seconds  # noqa: E501

        :return: The time of this SimulationStatus.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SimulationStatus.

        simulation time in seconds  # noqa: E501

        :param time: The time of this SimulationStatus.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                time is not None and time > 2147483647):  # noqa: E501
            self.__handle_validation_error("Invalid value for `time`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time is not None and time < 0):  # noqa: E501
            self.__handle_validation_error("Invalid value for `time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._time = time

    @property
    def paused(self):
        """Gets the paused of this SimulationStatus.  # noqa: E501


        :return: The paused of this SimulationStatus.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this SimulationStatus.


        :param paused: The paused of this SimulationStatus.  # noqa: E501
        :type: bool
        """

        self._paused = paused

    @property
    def detail(self):
        """Gets the detail of this SimulationStatus.  # noqa: E501


        :return: The detail of this SimulationStatus.  # noqa: E501
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this SimulationStatus.


        :param detail: The detail of this SimulationStatus.  # noqa: E501
        :type: object
        """

        self._detail = detail

    @property
    def exit_code(self):
        """Gets the exit_code of this SimulationStatus.  # noqa: E501

        only available for final statuses like 'finished' or 'crashed'. Gives detailed insight to the application state when the simulation finished  # noqa: E501

        :return: The exit_code of this SimulationStatus.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this SimulationStatus.

        only available for final statuses like 'finished' or 'crashed'. Gives detailed insight to the application state when the simulation finished  # noqa: E501

        :param exit_code: The exit_code of this SimulationStatus.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def id(self):
        """Gets the id of this SimulationStatus.  # noqa: E501


        :return: The id of this SimulationStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimulationStatus.


        :param id: The id of this SimulationStatus.  # noqa: E501
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
        if not isinstance(other, SimulationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationStatus):
            return True

        return self.to_dict() != other.to_dict()
