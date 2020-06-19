# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.6   3Di core release: 2.0.9  deployed on:  03:53PM (UTC) on June 12, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Raster(object):
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
        'type': 'str',
        'name': 'str',
        'threedimodel': 'str',
        'file': 'FileReadOnly',
        'id': 'int',
        'epsg_code': 'int',
        'extent': 'str',
        'geotransform': 'list[float]',
        'unit': 'str'
    }

    attribute_map = {
        'url': 'url',
        'type': 'type',
        'name': 'name',
        'threedimodel': 'threedimodel',
        'file': 'file',
        'id': 'id',
        'epsg_code': 'epsg_code',
        'extent': 'extent',
        'geotransform': 'geotransform',
        'unit': 'unit'
    }

    def __init__(self, url=None, type=None, name=None, threedimodel=None, file=None, id=None, epsg_code=None, extent=None, geotransform=None, unit=None):  # noqa: E501
        """Raster - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._type = None
        self._name = None
        self._threedimodel = None
        self._file = None
        self._id = None
        self._epsg_code = None
        self._extent = None
        self._geotransform = None
        self._unit = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.type = type
        self.name = name
        if threedimodel is not None:
            self.threedimodel = threedimodel
        if file is not None:
            self.file = file
        if id is not None:
            self.id = id
        self.epsg_code = epsg_code
        self.extent = extent
        self.geotransform = geotransform
        self.unit = unit

    @property
    def url(self):
        """Gets the url of this Raster.  # noqa: E501


        :return: The url of this Raster.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Raster.


        :param url: The url of this Raster.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def type(self):
        """Gets the type of this Raster.  # noqa: E501


        :return: The type of this Raster.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Raster.


        :param type: The type of this Raster.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["dem_file", "dem_raw_file", "equilibrium_infiltration_rate_file", "frict_coef_file", "initial_groundwater_level_file", "initial_waterlevel_file", "groundwater_hydro_connectivity_file", "groundwater_impervious_layer_level_file", "infiltration_decay_period_file", "initial_infiltration_rate_file", "leakage_file", "phreatic_storage_capacity_file", "hydraulic_conductivity_file", "porosity_file", "infiltration_rate_file", "max_infiltration_capacity_file", "interception_file"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this Raster.  # noqa: E501


        :return: The name of this Raster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Raster.


        :param name: The name of this Raster.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 60:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `60`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def threedimodel(self):
        """Gets the threedimodel of this Raster.  # noqa: E501


        :return: The threedimodel of this Raster.  # noqa: E501
        :rtype: str
        """
        return self._threedimodel

    @threedimodel.setter
    def threedimodel(self, threedimodel):
        """Sets the threedimodel of this Raster.


        :param threedimodel: The threedimodel of this Raster.  # noqa: E501
        :type: str
        """

        self._threedimodel = threedimodel

    @property
    def file(self):
        """Gets the file of this Raster.  # noqa: E501


        :return: The file of this Raster.  # noqa: E501
        :rtype: FileReadOnly
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Raster.


        :param file: The file of this Raster.  # noqa: E501
        :type: FileReadOnly
        """

        self._file = file

    @property
    def id(self):
        """Gets the id of this Raster.  # noqa: E501


        :return: The id of this Raster.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Raster.


        :param id: The id of this Raster.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def epsg_code(self):
        """Gets the epsg_code of this Raster.  # noqa: E501


        :return: The epsg_code of this Raster.  # noqa: E501
        :rtype: int
        """
        return self._epsg_code

    @epsg_code.setter
    def epsg_code(self, epsg_code):
        """Sets the epsg_code of this Raster.


        :param epsg_code: The epsg_code of this Raster.  # noqa: E501
        :type: int
        """
        if epsg_code is not None and epsg_code > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `epsg_code`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if epsg_code is not None and epsg_code < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `epsg_code`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._epsg_code = epsg_code

    @property
    def extent(self):
        """Gets the extent of this Raster.  # noqa: E501


        :return: The extent of this Raster.  # noqa: E501
        :rtype: str
        """
        return self._extent

    @extent.setter
    def extent(self, extent):
        """Sets the extent of this Raster.


        :param extent: The extent of this Raster.  # noqa: E501
        :type: str
        """

        self._extent = extent

    @property
    def geotransform(self):
        """Gets the geotransform of this Raster.  # noqa: E501


        :return: The geotransform of this Raster.  # noqa: E501
        :rtype: list[float]
        """
        return self._geotransform

    @geotransform.setter
    def geotransform(self, geotransform):
        """Sets the geotransform of this Raster.


        :param geotransform: The geotransform of this Raster.  # noqa: E501
        :type: list[float]
        """

        self._geotransform = geotransform

    @property
    def unit(self):
        """Gets the unit of this Raster.  # noqa: E501


        :return: The unit of this Raster.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Raster.


        :param unit: The unit of this Raster.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"meters"]  # noqa: E501
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

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
        if not isinstance(other, Raster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
