# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.1.1   3Di core release: 2.1.9  deployed on:  10:36AM (UTC) on December 09, 2021  # noqa: E501

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

class TableStructureControl(object):
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
        'offset': 'int',
        'duration': 'int',
        'measure_specification': 'MeasureSpecification',
        'structure_id': 'int',
        'structure_type': 'str',
        'type': 'str',
        'values': 'list[list[float]]',
        'state': 'str',
        'state_detail': 'object',
        'grid_id': 'int',
        'uid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'offset': 'offset',
        'duration': 'duration',
        'measure_specification': 'measure_specification',
        'structure_id': 'structure_id',
        'structure_type': 'structure_type',
        'type': 'type',
        'values': 'values',
        'state': 'state',
        'state_detail': 'state_detail',
        'grid_id': 'grid_id',
        'uid': 'uid'
    }

    def __init__(self, id=None, url=None, offset=None, duration=None, measure_specification=None, structure_id=None, structure_type=None, type=None, values=None, state=None, state_detail=None, grid_id=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """TableStructureControl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._url = None
        self._offset = None
        self._duration = None
        self._measure_specification = None
        self._structure_id = None
        self._structure_type = None
        self._type = None
        self._values = None
        self._state = None
        self._state_detail = None
        self._grid_id = None
        self._uid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        self.offset = offset
        self.duration = duration
        self.measure_specification = measure_specification
        self.structure_id = structure_id
        self.structure_type = structure_type
        self.type = type
        self.values = values
        if state is not None:
            self.state = state
        if state_detail is not None:
            self.state_detail = state_detail
        self.grid_id = grid_id
        if uid is not None:
            self.uid = uid

    @property
    def id(self):
        """Gets the id of this TableStructureControl.  # noqa: E501


        :return: The id of this TableStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableStructureControl.


        :param id: The id of this TableStructureControl.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this TableStructureControl.  # noqa: E501


        :return: The url of this TableStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TableStructureControl.


        :param url: The url of this TableStructureControl.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def offset(self):
        """Gets the offset of this TableStructureControl.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this TableStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TableStructureControl.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this TableStructureControl.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def duration(self):
        """Gets the duration of this TableStructureControl.  # noqa: E501

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :return: The duration of this TableStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TableStructureControl.

        event duration in seconds. -9999 is the 'infinite duration' value (only allowed in conjunction with infinite simulations  # noqa: E501

        :param duration: The duration of this TableStructureControl.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._duration = duration

    @property
    def measure_specification(self):
        """Gets the measure_specification of this TableStructureControl.  # noqa: E501


        :return: The measure_specification of this TableStructureControl.  # noqa: E501
        :rtype: MeasureSpecification
        """
        return self._measure_specification

    @measure_specification.setter
    def measure_specification(self, measure_specification):
        """Sets the measure_specification of this TableStructureControl.


        :param measure_specification: The measure_specification of this TableStructureControl.  # noqa: E501
        :type: MeasureSpecification
        """
        if self.local_vars_configuration.client_side_validation and measure_specification is None:  # noqa: E501
            raise ValueError("Invalid value for `measure_specification`, must not be `None`")  # noqa: E501

        self._measure_specification = measure_specification

    @property
    def structure_id(self):
        """Gets the structure_id of this TableStructureControl.  # noqa: E501


        :return: The structure_id of this TableStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._structure_id

    @structure_id.setter
    def structure_id(self, structure_id):
        """Sets the structure_id of this TableStructureControl.


        :param structure_id: The structure_id of this TableStructureControl.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                structure_id is not None and structure_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `structure_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                structure_id is not None and structure_id < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `structure_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._structure_id = structure_id

    @property
    def structure_type(self):
        """Gets the structure_type of this TableStructureControl.  # noqa: E501


        :return: The structure_type of this TableStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._structure_type

    @structure_type.setter
    def structure_type(self, structure_type):
        """Sets the structure_type of this TableStructureControl.


        :param structure_type: The structure_type of this TableStructureControl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and structure_type is None:  # noqa: E501
            raise ValueError("Invalid value for `structure_type`, must not be `None`")  # noqa: E501
        allowed_values = ["v2_pumpstation", "v2_pipe", "v2_orifice", "v2_culvert", "v2_weir", "v2_channel"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and structure_type not in allowed_values:  # noqa: E501
            logger.warning(
                "Warning: Unknown value for `structure_type` ({0}), must be one of {1}. Either your threedi-api-client version is out of date or this value is invalid."  # noqa: E501
                .format(structure_type, allowed_values)
            )

        self._structure_type = structure_type

    @property
    def type(self):
        """Gets the type of this TableStructureControl.  # noqa: E501


        :return: The type of this TableStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TableStructureControl.


        :param type: The type of this TableStructureControl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["set_discharge_coefficients", "set_crest_level", "set_pump_capacity"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            logger.warning(
                "Warning: Unknown value for `type` ({0}), must be one of {1}. Either your threedi-api-client version is out of date or this value is invalid."  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def values(self):
        """Gets the values of this TableStructureControl.  # noqa: E501


        :return: The values of this TableStructureControl.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TableStructureControl.


        :param values: The values of this TableStructureControl.  # noqa: E501
        :type: list[list[float]]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def state(self):
        """Gets the state of this TableStructureControl.  # noqa: E501


        :return: The state of this TableStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TableStructureControl.


        :param state: The state of this TableStructureControl.  # noqa: E501
        :type: str
        """
        allowed_values = ["processing", "valid", "invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            logger.warning(
                "Warning: Unknown value for `state` ({0}), must be one of {1}. Either your threedi-api-client version is out of date or this value is invalid."  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_detail(self):
        """Gets the state_detail of this TableStructureControl.  # noqa: E501


        :return: The state_detail of this TableStructureControl.  # noqa: E501
        :rtype: object
        """
        return self._state_detail

    @state_detail.setter
    def state_detail(self, state_detail):
        """Sets the state_detail of this TableStructureControl.


        :param state_detail: The state_detail of this TableStructureControl.  # noqa: E501
        :type: object
        """

        self._state_detail = state_detail

    @property
    def grid_id(self):
        """Gets the grid_id of this TableStructureControl.  # noqa: E501


        :return: The grid_id of this TableStructureControl.  # noqa: E501
        :rtype: int
        """
        return self._grid_id

    @grid_id.setter
    def grid_id(self, grid_id):
        """Sets the grid_id of this TableStructureControl.


        :param grid_id: The grid_id of this TableStructureControl.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                grid_id is not None and grid_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `grid_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                grid_id is not None and grid_id < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `grid_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._grid_id = grid_id

    @property
    def uid(self):
        """Gets the uid of this TableStructureControl.  # noqa: E501


        :return: The uid of this TableStructureControl.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this TableStructureControl.


        :param uid: The uid of this TableStructureControl.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if not isinstance(other, TableStructureControl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TableStructureControl):
            return True

        return self.to_dict() != other.to_dict()
