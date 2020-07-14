# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.10   3Di core release: 2.0.10  deployed on:  09:44AM (UTC) on July 02, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.aio.configuration import Configuration


class Breach(object):
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
        'potential_breach': 'str',
        'line_id': 'int',
        'duration_till_max_depth': 'int',
        'maximum_breach_depth': 'float',
        'levee_material': 'str',
        'initial_width': 'float',
        'discharge_coefficient_positive': 'float',
        'discharge_coefficient_negative': 'float',
        'simulation': 'str',
        'offset': 'int',
        'id': 'int',
        'uid': 'str'
    }

    attribute_map = {
        'url': 'url',
        'potential_breach': 'potential_breach',
        'line_id': 'line_id',
        'duration_till_max_depth': 'duration_till_max_depth',
        'maximum_breach_depth': 'maximum_breach_depth',
        'levee_material': 'levee_material',
        'initial_width': 'initial_width',
        'discharge_coefficient_positive': 'discharge_coefficient_positive',
        'discharge_coefficient_negative': 'discharge_coefficient_negative',
        'simulation': 'simulation',
        'offset': 'offset',
        'id': 'id',
        'uid': 'uid'
    }

    def __init__(self, url=None, potential_breach=None, line_id=None, duration_till_max_depth=None, maximum_breach_depth=None, levee_material=None, initial_width=None, discharge_coefficient_positive=None, discharge_coefficient_negative=None, simulation=None, offset=None, id=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """Breach - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._potential_breach = None
        self._line_id = None
        self._duration_till_max_depth = None
        self._maximum_breach_depth = None
        self._levee_material = None
        self._initial_width = None
        self._discharge_coefficient_positive = None
        self._discharge_coefficient_negative = None
        self._simulation = None
        self._offset = None
        self._id = None
        self._uid = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.potential_breach = potential_breach
        if line_id is not None:
            self.line_id = line_id
        self.duration_till_max_depth = duration_till_max_depth
        self.maximum_breach_depth = maximum_breach_depth
        self.levee_material = levee_material
        self.initial_width = initial_width
        self.discharge_coefficient_positive = discharge_coefficient_positive
        self.discharge_coefficient_negative = discharge_coefficient_negative
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        if id is not None:
            self.id = id
        if uid is not None:
            self.uid = uid

    @property
    def url(self):
        """Gets the url of this Breach.  # noqa: E501


        :return: The url of this Breach.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Breach.


        :param url: The url of this Breach.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def potential_breach(self):
        """Gets the potential_breach of this Breach.  # noqa: E501


        :return: The potential_breach of this Breach.  # noqa: E501
        :rtype: str
        """
        return self._potential_breach

    @potential_breach.setter
    def potential_breach(self, potential_breach):
        """Sets the potential_breach of this Breach.


        :param potential_breach: The potential_breach of this Breach.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and potential_breach is None:  # noqa: E501
            raise ValueError("Invalid value for `potential_breach`, must not be `None`")  # noqa: E501

        self._potential_breach = potential_breach

    @property
    def line_id(self):
        """Gets the line_id of this Breach.  # noqa: E501


        :return: The line_id of this Breach.  # noqa: E501
        :rtype: int
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this Breach.


        :param line_id: The line_id of this Breach.  # noqa: E501
        :type: int
        """

        self._line_id = line_id

    @property
    def duration_till_max_depth(self):
        """Gets the duration_till_max_depth of this Breach.  # noqa: E501

        duration till maximum depth in seconds  # noqa: E501

        :return: The duration_till_max_depth of this Breach.  # noqa: E501
        :rtype: int
        """
        return self._duration_till_max_depth

    @duration_till_max_depth.setter
    def duration_till_max_depth(self, duration_till_max_depth):
        """Sets the duration_till_max_depth of this Breach.

        duration till maximum depth in seconds  # noqa: E501

        :param duration_till_max_depth: The duration_till_max_depth of this Breach.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and duration_till_max_depth is None:  # noqa: E501
            raise ValueError("Invalid value for `duration_till_max_depth`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration_till_max_depth is not None and duration_till_max_depth > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `duration_till_max_depth`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration_till_max_depth is not None and duration_till_max_depth < 0):  # noqa: E501
            raise ValueError("Invalid value for `duration_till_max_depth`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration_till_max_depth = duration_till_max_depth

    @property
    def maximum_breach_depth(self):
        """Gets the maximum_breach_depth of this Breach.  # noqa: E501

        Override the maximum_breach_depth of the potential breach  # noqa: E501

        :return: The maximum_breach_depth of this Breach.  # noqa: E501
        :rtype: float
        """
        return self._maximum_breach_depth

    @maximum_breach_depth.setter
    def maximum_breach_depth(self, maximum_breach_depth):
        """Sets the maximum_breach_depth of this Breach.

        Override the maximum_breach_depth of the potential breach  # noqa: E501

        :param maximum_breach_depth: The maximum_breach_depth of this Breach.  # noqa: E501
        :type: float
        """

        self._maximum_breach_depth = maximum_breach_depth

    @property
    def levee_material(self):
        """Gets the levee_material of this Breach.  # noqa: E501

        Override the levee_material of the potential breach  # noqa: E501

        :return: The levee_material of this Breach.  # noqa: E501
        :rtype: str
        """
        return self._levee_material

    @levee_material.setter
    def levee_material(self, levee_material):
        """Sets the levee_material of this Breach.

        Override the levee_material of the potential breach  # noqa: E501

        :param levee_material: The levee_material of this Breach.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"sand", "clay"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and levee_material not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `levee_material` ({0}), must be one of {1}"  # noqa: E501
                .format(levee_material, allowed_values)
            )

        self._levee_material = levee_material

    @property
    def initial_width(self):
        """Gets the initial_width of this Breach.  # noqa: E501

        initial width in meters  # noqa: E501

        :return: The initial_width of this Breach.  # noqa: E501
        :rtype: float
        """
        return self._initial_width

    @initial_width.setter
    def initial_width(self, initial_width):
        """Sets the initial_width of this Breach.

        initial width in meters  # noqa: E501

        :param initial_width: The initial_width of this Breach.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and initial_width is None:  # noqa: E501
            raise ValueError("Invalid value for `initial_width`, must not be `None`")  # noqa: E501

        self._initial_width = initial_width

    @property
    def discharge_coefficient_positive(self):
        """Gets the discharge_coefficient_positive of this Breach.  # noqa: E501


        :return: The discharge_coefficient_positive of this Breach.  # noqa: E501
        :rtype: float
        """
        return self._discharge_coefficient_positive

    @discharge_coefficient_positive.setter
    def discharge_coefficient_positive(self, discharge_coefficient_positive):
        """Sets the discharge_coefficient_positive of this Breach.


        :param discharge_coefficient_positive: The discharge_coefficient_positive of this Breach.  # noqa: E501
        :type: float
        """

        self._discharge_coefficient_positive = discharge_coefficient_positive

    @property
    def discharge_coefficient_negative(self):
        """Gets the discharge_coefficient_negative of this Breach.  # noqa: E501


        :return: The discharge_coefficient_negative of this Breach.  # noqa: E501
        :rtype: float
        """
        return self._discharge_coefficient_negative

    @discharge_coefficient_negative.setter
    def discharge_coefficient_negative(self, discharge_coefficient_negative):
        """Sets the discharge_coefficient_negative of this Breach.


        :param discharge_coefficient_negative: The discharge_coefficient_negative of this Breach.  # noqa: E501
        :type: float
        """

        self._discharge_coefficient_negative = discharge_coefficient_negative

    @property
    def simulation(self):
        """Gets the simulation of this Breach.  # noqa: E501


        :return: The simulation of this Breach.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this Breach.


        :param simulation: The simulation of this Breach.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this Breach.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this Breach.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Breach.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this Breach.  # noqa: E501
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
    def id(self):
        """Gets the id of this Breach.  # noqa: E501


        :return: The id of this Breach.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Breach.


        :param id: The id of this Breach.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uid(self):
        """Gets the uid of this Breach.  # noqa: E501


        :return: The uid of this Breach.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Breach.


        :param uid: The uid of this Breach.  # noqa: E501
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
        if not isinstance(other, Breach):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Breach):
            return True

        return self.to_dict() != other.to_dict()