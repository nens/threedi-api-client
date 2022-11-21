# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.0.8   3Di core release: 2.3.1  deployed on:  01:12PM (UTC) on November 15, 2022  # noqa: E501

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

class RasterEdit(object):
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
        'simulation': 'str',
        'raster': 'str',
        'offset': 'int',
        'value': 'float',
        'polygon': 'Polygon',
        'relative': 'bool',
        'uid': 'str',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'raster': 'raster',
        'offset': 'offset',
        'value': 'value',
        'polygon': 'polygon',
        'relative': 'relative',
        'uid': 'uid',
        'id': 'id'
    }

    def __init__(self, url=None, simulation=None, raster=None, offset=None, value=None, polygon=None, relative=None, uid=None, id=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """RasterEdit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._simulation = None
        self._raster = None
        self._offset = None
        self._value = None
        self._polygon = None
        self._relative = None
        self._uid = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.raster = raster
        self.offset = offset
        self.value = value
        self.polygon = polygon
        if relative is not None:
            self.relative = relative
        if uid is not None:
            self.uid = uid
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this RasterEdit.  # noqa: E501


        :return: The url of this RasterEdit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RasterEdit.


        :param url: The url of this RasterEdit.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this RasterEdit.  # noqa: E501


        :return: The simulation of this RasterEdit.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this RasterEdit.


        :param simulation: The simulation of this RasterEdit.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def raster(self):
        """Gets the raster of this RasterEdit.  # noqa: E501


        :return: The raster of this RasterEdit.  # noqa: E501
        :rtype: str
        """
        return self._raster

    @raster.setter
    def raster(self, raster):
        """Sets the raster of this RasterEdit.


        :param raster: The raster of this RasterEdit.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and raster is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `raster`, must not be `None`")  # noqa: E501

        self._raster = raster

    @property
    def offset(self):
        """Gets the offset of this RasterEdit.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this RasterEdit.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this RasterEdit.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this RasterEdit.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset > 2147483647):  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            self.__handle_validation_error("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def value(self):
        """Gets the value of this RasterEdit.  # noqa: E501

        Absolute or relative height (in meters)  to use for the polygon  # noqa: E501

        :return: The value of this RasterEdit.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RasterEdit.

        Absolute or relative height (in meters)  to use for the polygon  # noqa: E501

        :param value: The value of this RasterEdit.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def polygon(self):
        """Gets the polygon of this RasterEdit.  # noqa: E501


        :return: The polygon of this RasterEdit.  # noqa: E501
        :rtype: Polygon
        """
        return self._polygon

    @polygon.setter
    def polygon(self, polygon):
        """Sets the polygon of this RasterEdit.


        :param polygon: The polygon of this RasterEdit.  # noqa: E501
        :type: Polygon
        """
        if self.local_vars_configuration.client_side_validation and polygon is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `polygon`, must not be `None`")  # noqa: E501

        self._polygon = polygon

    @property
    def relative(self):
        """Gets the relative of this RasterEdit.  # noqa: E501

        Process the value as a relative height, default is absolute  # noqa: E501

        :return: The relative of this RasterEdit.  # noqa: E501
        :rtype: bool
        """
        return self._relative

    @relative.setter
    def relative(self, relative):
        """Sets the relative of this RasterEdit.

        Process the value as a relative height, default is absolute  # noqa: E501

        :param relative: The relative of this RasterEdit.  # noqa: E501
        :type: bool
        """

        self._relative = relative

    @property
    def uid(self):
        """Gets the uid of this RasterEdit.  # noqa: E501


        :return: The uid of this RasterEdit.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this RasterEdit.


        :param uid: The uid of this RasterEdit.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def id(self):
        """Gets the id of this RasterEdit.  # noqa: E501


        :return: The id of this RasterEdit.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RasterEdit.


        :param id: The id of this RasterEdit.  # noqa: E501
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
        if not isinstance(other, RasterEdit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RasterEdit):
            return True

        return self.to_dict() != other.to_dict()
