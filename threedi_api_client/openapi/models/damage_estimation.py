# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.4.3   3Di core release: 3.5.0  deployed on:  03:07PM (UTC) on October 02, 2024  # noqa: E501

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

class DamageEstimation(object):
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
        'damage_table': 'str',
        'elevation_raster_uuid': 'str',
        'landcover_raster_uuid': 'str',
        'road_rail_raster_uuid': 'str',
        'cost_type': 'int',
        'flood_month': 'int',
        'inundation_period': 'int',
        'repair_time_infrastructure': 'int',
        'repair_time_buildings': 'int'
    }

    required_fields = [
    ]

    attribute_map = {
        'damage_table': 'damage_table',
        'elevation_raster_uuid': 'elevation_raster_uuid',
        'landcover_raster_uuid': 'landcover_raster_uuid',
        'road_rail_raster_uuid': 'road_rail_raster_uuid',
        'cost_type': 'cost_type',
        'flood_month': 'flood_month',
        'inundation_period': 'inundation_period',
        'repair_time_infrastructure': 'repair_time_infrastructure',
        'repair_time_buildings': 'repair_time_buildings'
    }

    def __init__(self, damage_table='3Di-V1', elevation_raster_uuid='36588275-f3e3-4120-8c1e-602f7ae85386', landcover_raster_uuid='717478ef-099d-41d8-971d-8b4309e59d92', road_rail_raster_uuid='e40c1b96-e71f-462c-8acb-59a3a8b7db89', cost_type=None, flood_month=None, inundation_period=None, repair_time_infrastructure=None, repair_time_buildings=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """DamageEstimation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._damage_table = None
        self._elevation_raster_uuid = None
        self._landcover_raster_uuid = None
        self._road_rail_raster_uuid = None
        self._cost_type = None
        self._flood_month = None
        self._inundation_period = None
        self._repair_time_infrastructure = None
        self._repair_time_buildings = None
        self.discriminator = None

        if damage_table is not None:
            self.damage_table = damage_table
        if elevation_raster_uuid is not None:
            self.elevation_raster_uuid = elevation_raster_uuid
        if landcover_raster_uuid is not None:
            self.landcover_raster_uuid = landcover_raster_uuid
        if road_rail_raster_uuid is not None:
            self.road_rail_raster_uuid = road_rail_raster_uuid
        if cost_type is not None:
            self.cost_type = cost_type
        if flood_month is not None:
            self.flood_month = flood_month
        if inundation_period is not None:
            self.inundation_period = inundation_period
        if repair_time_infrastructure is not None:
            self.repair_time_infrastructure = repair_time_infrastructure
        if repair_time_buildings is not None:
            self.repair_time_buildings = repair_time_buildings

    @property
    def damage_table(self):
        """Gets the damage_table of this DamageEstimation.  # noqa: E501


        :return: The damage_table of this DamageEstimation.  # noqa: E501
        :rtype: str
        """
        return self._damage_table

    @damage_table.setter
    def damage_table(self, damage_table):
        """Sets the damage_table of this DamageEstimation.


        :param damage_table: The damage_table of this DamageEstimation.  # noqa: E501
        :type: str
        """

        self._damage_table = damage_table

    @property
    def elevation_raster_uuid(self):
        """Gets the elevation_raster_uuid of this DamageEstimation.  # noqa: E501


        :return: The elevation_raster_uuid of this DamageEstimation.  # noqa: E501
        :rtype: str
        """
        return self._elevation_raster_uuid

    @elevation_raster_uuid.setter
    def elevation_raster_uuid(self, elevation_raster_uuid):
        """Sets the elevation_raster_uuid of this DamageEstimation.


        :param elevation_raster_uuid: The elevation_raster_uuid of this DamageEstimation.  # noqa: E501
        :type: str
        """

        self._elevation_raster_uuid = elevation_raster_uuid

    @property
    def landcover_raster_uuid(self):
        """Gets the landcover_raster_uuid of this DamageEstimation.  # noqa: E501


        :return: The landcover_raster_uuid of this DamageEstimation.  # noqa: E501
        :rtype: str
        """
        return self._landcover_raster_uuid

    @landcover_raster_uuid.setter
    def landcover_raster_uuid(self, landcover_raster_uuid):
        """Sets the landcover_raster_uuid of this DamageEstimation.


        :param landcover_raster_uuid: The landcover_raster_uuid of this DamageEstimation.  # noqa: E501
        :type: str
        """

        self._landcover_raster_uuid = landcover_raster_uuid

    @property
    def road_rail_raster_uuid(self):
        """Gets the road_rail_raster_uuid of this DamageEstimation.  # noqa: E501


        :return: The road_rail_raster_uuid of this DamageEstimation.  # noqa: E501
        :rtype: str
        """
        return self._road_rail_raster_uuid

    @road_rail_raster_uuid.setter
    def road_rail_raster_uuid(self, road_rail_raster_uuid):
        """Sets the road_rail_raster_uuid of this DamageEstimation.


        :param road_rail_raster_uuid: The road_rail_raster_uuid of this DamageEstimation.  # noqa: E501
        :type: str
        """

        self._road_rail_raster_uuid = road_rail_raster_uuid

    @property
    def cost_type(self):
        """Gets the cost_type of this DamageEstimation.  # noqa: E501


        :return: The cost_type of this DamageEstimation.  # noqa: E501
        :rtype: int
        """
        return self._cost_type

    @cost_type.setter
    def cost_type(self, cost_type):
        """Sets the cost_type of this DamageEstimation.


        :param cost_type: The cost_type of this DamageEstimation.  # noqa: E501
        :type: int
        """

        self._cost_type = cost_type

    @property
    def flood_month(self):
        """Gets the flood_month of this DamageEstimation.  # noqa: E501


        :return: The flood_month of this DamageEstimation.  # noqa: E501
        :rtype: int
        """
        return self._flood_month

    @flood_month.setter
    def flood_month(self, flood_month):
        """Sets the flood_month of this DamageEstimation.


        :param flood_month: The flood_month of this DamageEstimation.  # noqa: E501
        :type: int
        """

        self._flood_month = flood_month

    @property
    def inundation_period(self):
        """Gets the inundation_period of this DamageEstimation.  # noqa: E501


        :return: The inundation_period of this DamageEstimation.  # noqa: E501
        :rtype: int
        """
        return self._inundation_period

    @inundation_period.setter
    def inundation_period(self, inundation_period):
        """Sets the inundation_period of this DamageEstimation.


        :param inundation_period: The inundation_period of this DamageEstimation.  # noqa: E501
        :type: int
        """

        self._inundation_period = inundation_period

    @property
    def repair_time_infrastructure(self):
        """Gets the repair_time_infrastructure of this DamageEstimation.  # noqa: E501


        :return: The repair_time_infrastructure of this DamageEstimation.  # noqa: E501
        :rtype: int
        """
        return self._repair_time_infrastructure

    @repair_time_infrastructure.setter
    def repair_time_infrastructure(self, repair_time_infrastructure):
        """Sets the repair_time_infrastructure of this DamageEstimation.


        :param repair_time_infrastructure: The repair_time_infrastructure of this DamageEstimation.  # noqa: E501
        :type: int
        """

        self._repair_time_infrastructure = repair_time_infrastructure

    @property
    def repair_time_buildings(self):
        """Gets the repair_time_buildings of this DamageEstimation.  # noqa: E501


        :return: The repair_time_buildings of this DamageEstimation.  # noqa: E501
        :rtype: int
        """
        return self._repair_time_buildings

    @repair_time_buildings.setter
    def repair_time_buildings(self, repair_time_buildings):
        """Sets the repair_time_buildings of this DamageEstimation.


        :param repair_time_buildings: The repair_time_buildings of this DamageEstimation.  # noqa: E501
        :type: int
        """

        self._repair_time_buildings = repair_time_buildings

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
        if not isinstance(other, DamageEstimation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DamageEstimation):
            return True

        return self.to_dict() != other.to_dict()
