# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 1.0.65   3Di core release: 2.1.3  deployed on:  09:52AM (UTC) on November 01, 2021  # noqa: E501

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

class MeasureLocation(object):
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
        'weight': 'str',
        'content_type': 'str',
        'content_pk': 'int',
        'grid_id': 'int',
        'state': 'str',
        'state_detail': 'object'
    }

    attribute_map = {
        'id': 'id',
        'weight': 'weight',
        'content_type': 'content_type',
        'content_pk': 'content_pk',
        'grid_id': 'grid_id',
        'state': 'state',
        'state_detail': 'state_detail'
    }

    def __init__(self, id=None, weight=None, content_type=None, content_pk=None, grid_id=None, state=None, state_detail=None, local_vars_configuration=None):  # noqa: E501
        """MeasureLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._weight = None
        self._content_type = None
        self._content_pk = None
        self._grid_id = None
        self._state = None
        self._state_detail = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.weight = weight
        self.content_type = content_type
        self.content_pk = content_pk
        self.grid_id = grid_id
        if state is not None:
            self.state = state
        if state_detail is not None:
            self.state_detail = state_detail

    @property
    def id(self):
        """Gets the id of this MeasureLocation.  # noqa: E501


        :return: The id of this MeasureLocation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MeasureLocation.


        :param id: The id of this MeasureLocation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def weight(self):
        """Gets the weight of this MeasureLocation.  # noqa: E501


        :return: The weight of this MeasureLocation.  # noqa: E501
        :rtype: str
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this MeasureLocation.


        :param weight: The weight of this MeasureLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and weight is None:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

    @property
    def content_type(self):
        """Gets the content_type of this MeasureLocation.  # noqa: E501

        e.g.   # noqa: E501

        :return: The content_type of this MeasureLocation.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this MeasureLocation.

        e.g.   # noqa: E501

        :param content_type: The content_type of this MeasureLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and content_type is None:  # noqa: E501
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501
        allowed_values = ["v2_connection_node", "v2_pipe", "v2_orifice", "v2_culvert", "v2_channel", "v2_weir"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and content_type not in allowed_values:  # noqa: E501
            logger.warning(
                "Warning: Unknown value for `content_type` ({0}), must be one of {1}. Either your threedi-api-client version is out of date or this value is invalid."  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def content_pk(self):
        """Gets the content_pk of this MeasureLocation.  # noqa: E501


        :return: The content_pk of this MeasureLocation.  # noqa: E501
        :rtype: int
        """
        return self._content_pk

    @content_pk.setter
    def content_pk(self, content_pk):
        """Sets the content_pk of this MeasureLocation.


        :param content_pk: The content_pk of this MeasureLocation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and content_pk is None:  # noqa: E501
            raise ValueError("Invalid value for `content_pk`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                content_pk is not None and content_pk > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `content_pk`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                content_pk is not None and content_pk < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `content_pk`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._content_pk = content_pk

    @property
    def grid_id(self):
        """Gets the grid_id of this MeasureLocation.  # noqa: E501


        :return: The grid_id of this MeasureLocation.  # noqa: E501
        :rtype: int
        """
        return self._grid_id

    @grid_id.setter
    def grid_id(self, grid_id):
        """Sets the grid_id of this MeasureLocation.


        :param grid_id: The grid_id of this MeasureLocation.  # noqa: E501
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
    def state(self):
        """Gets the state of this MeasureLocation.  # noqa: E501


        :return: The state of this MeasureLocation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MeasureLocation.


        :param state: The state of this MeasureLocation.  # noqa: E501
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
        """Gets the state_detail of this MeasureLocation.  # noqa: E501


        :return: The state_detail of this MeasureLocation.  # noqa: E501
        :rtype: object
        """
        return self._state_detail

    @state_detail.setter
    def state_detail(self, state_detail):
        """Sets the state_detail of this MeasureLocation.


        :param state_detail: The state_detail of this MeasureLocation.  # noqa: E501
        :type: object
        """

        self._state_detail = state_detail

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
        if not isinstance(other, MeasureLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeasureLocation):
            return True

        return self.to_dict() != other.to_dict()
