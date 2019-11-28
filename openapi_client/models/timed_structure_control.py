# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 0.0.22   3Di core release: 2.0.2  deployed on:  09:48AM (UTC) on November 25, 2019  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TimedStructureControl(object):
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
        'id': 'int',
        'url': 'str',
        'simulation': 'str',
        'offset': 'int',
        'duration': 'int',
        'value': 'list[float]',
        'type': 'str',
        'structure_id': 'int',
        'structure_type': 'str',
        'state': 'str',
        'state_detail': 'object',
        'grid_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'simulation': 'simulation',
        'offset': 'offset',
        'duration': 'duration',
        'value': 'value',
        'type': 'type',
        'structure_id': 'structure_id',
        'structure_type': 'structure_type',
        'state': 'state',
        'state_detail': 'state_detail',
        'grid_id': 'grid_id'
    }

    def __init__(self, id=None, url=None, simulation=None, offset=None, duration=None, value=None, type=None, structure_id=None, structure_type=None, state=None, state_detail=None, grid_id=None):  # noqa: E501
        """TimedStructureControl - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._url = None
        self._simulation = None
        self._offset = None
        self._duration = None
        self._value = None
        self._type = None
        self._structure_id = None
        self._structure_type = None
        self._state = None
        self._state_detail = None
        self._grid_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        self.duration = duration
        self.value = value
        self.type = type
        self.structure_id = structure_id
        self.structure_type = structure_type
        if state is not None:
            self.state = state
        if state_detail is not None:
            self.state_detail = state_detail
        self.grid_id = grid_id

    @property
    def id(self):
        """Gets the id of this TimedStructureControl.  # noqa: E501


        :return: The id of this TimedStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimedStructureControl.


        :param id: The id of this TimedStructureControl.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this TimedStructureControl.  # noqa: E501


        :return: The url of this TimedStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TimedStructureControl.


        :param url: The url of this TimedStructureControl.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this TimedStructureControl.  # noqa: E501


        :return: The simulation of this TimedStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this TimedStructureControl.


        :param simulation: The simulation of this TimedStructureControl.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this TimedStructureControl.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this TimedStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TimedStructureControl.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this TimedStructureControl.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if offset is not None and offset > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if offset is not None and offset < 0:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def duration(self):
        """Gets the duration of this TimedStructureControl.  # noqa: E501


        :return: The duration of this TimedStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TimedStructureControl.


        :param duration: The duration of this TimedStructureControl.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501
        if duration is not None and duration < 1:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `1`")  # noqa: E501

        self._duration = duration

    @property
    def value(self):
        """Gets the value of this TimedStructureControl.  # noqa: E501


        :return: The value of this TimedStructureControl.  # noqa: E501
        :rtype: list[float]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TimedStructureControl.


        :param value: The value of this TimedStructureControl.  # noqa: E501
        :type: list[float]
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def type(self):
        """Gets the type of this TimedStructureControl.  # noqa: E501


        :return: The type of this TimedStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimedStructureControl.


        :param type: The type of this TimedStructureControl.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["set_discharge_coefficients", "set_crest_level", "set_pump_discharge"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def structure_id(self):
        """Gets the structure_id of this TimedStructureControl.  # noqa: E501


        :return: The structure_id of this TimedStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._structure_id

    @structure_id.setter
    def structure_id(self, structure_id):
        """Sets the structure_id of this TimedStructureControl.


        :param structure_id: The structure_id of this TimedStructureControl.  # noqa: E501
        :type: int
        """
        if structure_id is not None and structure_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `structure_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if structure_id is not None and structure_id < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `structure_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._structure_id = structure_id

    @property
    def structure_type(self):
        """Gets the structure_type of this TimedStructureControl.  # noqa: E501


        :return: The structure_type of this TimedStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._structure_type

    @structure_type.setter
    def structure_type(self, structure_type):
        """Sets the structure_type of this TimedStructureControl.


        :param structure_type: The structure_type of this TimedStructureControl.  # noqa: E501
        :type: str
        """
        if structure_type is None:
            raise ValueError("Invalid value for `structure_type`, must not be `None`")  # noqa: E501
        allowed_values = ["v2_pumpstation", "v2_pipe", "v2_orifice", "v2_culvert", "v2_weir", "v2_channel"]  # noqa: E501
        if structure_type not in allowed_values:
            raise ValueError(
                "Invalid value for `structure_type` ({0}), must be one of {1}"  # noqa: E501
                .format(structure_type, allowed_values)
            )

        self._structure_type = structure_type

    @property
    def state(self):
        """Gets the state of this TimedStructureControl.  # noqa: E501


        :return: The state of this TimedStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TimedStructureControl.


        :param state: The state of this TimedStructureControl.  # noqa: E501
        :type: str
        """
        allowed_values = ["processing", "valid", "invalid"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_detail(self):
        """Gets the state_detail of this TimedStructureControl.  # noqa: E501


        :return: The state_detail of this TimedStructureControl.  # noqa: E501
        :rtype: object
        """
        return self._state_detail

    @state_detail.setter
    def state_detail(self, state_detail):
        """Sets the state_detail of this TimedStructureControl.


        :param state_detail: The state_detail of this TimedStructureControl.  # noqa: E501
        :type: object
        """

        self._state_detail = state_detail

    @property
    def grid_id(self):
        """Gets the grid_id of this TimedStructureControl.  # noqa: E501


        :return: The grid_id of this TimedStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._grid_id

    @grid_id.setter
    def grid_id(self, grid_id):
        """Sets the grid_id of this TimedStructureControl.


        :param grid_id: The grid_id of this TimedStructureControl.  # noqa: E501
        :type: int
        """
        if grid_id is not None and grid_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `grid_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if grid_id is not None and grid_id < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `grid_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._grid_id = grid_id

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
        if not isinstance(other, TimedStructureControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
