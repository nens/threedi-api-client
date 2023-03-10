# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.2.6   3Di core release: 2.3.6  deployed on:  07:54AM (UTC) on March 10, 2023  # noqa: E501

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

class RasterOptions(object):
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
        'dem_file': 'str',
        'dem_raw_file': 'str',
        'equilibrium_infiltration_rate_file': 'str',
        'frict_coef_file': 'str',
        'initial_groundwater_level_file': 'str',
        'initial_waterlevel_file': 'str',
        'groundwater_hydro_connectivity_file': 'str',
        'groundwater_impervious_layer_level_file': 'str',
        'infiltration_decay_period_file': 'str',
        'initial_infiltration_rate_file': 'str',
        'leakage_file': 'str',
        'phreatic_storage_capacity_file': 'str',
        'hydraulic_conductivity_file': 'str',
        'porosity_file': 'str',
        'infiltration_rate_file': 'str',
        'max_infiltration_capacity_file': 'str',
        'interception_file': 'str'
    }

    attribute_map = {
        'dem_file': 'dem_file',
        'dem_raw_file': 'dem_raw_file',
        'equilibrium_infiltration_rate_file': 'equilibrium_infiltration_rate_file',
        'frict_coef_file': 'frict_coef_file',
        'initial_groundwater_level_file': 'initial_groundwater_level_file',
        'initial_waterlevel_file': 'initial_waterlevel_file',
        'groundwater_hydro_connectivity_file': 'groundwater_hydro_connectivity_file',
        'groundwater_impervious_layer_level_file': 'groundwater_impervious_layer_level_file',
        'infiltration_decay_period_file': 'infiltration_decay_period_file',
        'initial_infiltration_rate_file': 'initial_infiltration_rate_file',
        'leakage_file': 'leakage_file',
        'phreatic_storage_capacity_file': 'phreatic_storage_capacity_file',
        'hydraulic_conductivity_file': 'hydraulic_conductivity_file',
        'porosity_file': 'porosity_file',
        'infiltration_rate_file': 'infiltration_rate_file',
        'max_infiltration_capacity_file': 'max_infiltration_capacity_file',
        'interception_file': 'interception_file'
    }

    def __init__(self, dem_file=None, dem_raw_file=None, equilibrium_infiltration_rate_file=None, frict_coef_file=None, initial_groundwater_level_file=None, initial_waterlevel_file=None, groundwater_hydro_connectivity_file=None, groundwater_impervious_layer_level_file=None, infiltration_decay_period_file=None, initial_infiltration_rate_file=None, leakage_file=None, phreatic_storage_capacity_file=None, hydraulic_conductivity_file=None, porosity_file=None, infiltration_rate_file=None, max_infiltration_capacity_file=None, interception_file=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """RasterOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._dem_file = None
        self._dem_raw_file = None
        self._equilibrium_infiltration_rate_file = None
        self._frict_coef_file = None
        self._initial_groundwater_level_file = None
        self._initial_waterlevel_file = None
        self._groundwater_hydro_connectivity_file = None
        self._groundwater_impervious_layer_level_file = None
        self._infiltration_decay_period_file = None
        self._initial_infiltration_rate_file = None
        self._leakage_file = None
        self._phreatic_storage_capacity_file = None
        self._hydraulic_conductivity_file = None
        self._porosity_file = None
        self._infiltration_rate_file = None
        self._max_infiltration_capacity_file = None
        self._interception_file = None
        self.discriminator = None

        if dem_file is not None:
            self.dem_file = dem_file
        if dem_raw_file is not None:
            self.dem_raw_file = dem_raw_file
        if equilibrium_infiltration_rate_file is not None:
            self.equilibrium_infiltration_rate_file = equilibrium_infiltration_rate_file
        if frict_coef_file is not None:
            self.frict_coef_file = frict_coef_file
        if initial_groundwater_level_file is not None:
            self.initial_groundwater_level_file = initial_groundwater_level_file
        if initial_waterlevel_file is not None:
            self.initial_waterlevel_file = initial_waterlevel_file
        if groundwater_hydro_connectivity_file is not None:
            self.groundwater_hydro_connectivity_file = groundwater_hydro_connectivity_file
        if groundwater_impervious_layer_level_file is not None:
            self.groundwater_impervious_layer_level_file = groundwater_impervious_layer_level_file
        if infiltration_decay_period_file is not None:
            self.infiltration_decay_period_file = infiltration_decay_period_file
        if initial_infiltration_rate_file is not None:
            self.initial_infiltration_rate_file = initial_infiltration_rate_file
        if leakage_file is not None:
            self.leakage_file = leakage_file
        if phreatic_storage_capacity_file is not None:
            self.phreatic_storage_capacity_file = phreatic_storage_capacity_file
        if hydraulic_conductivity_file is not None:
            self.hydraulic_conductivity_file = hydraulic_conductivity_file
        if porosity_file is not None:
            self.porosity_file = porosity_file
        if infiltration_rate_file is not None:
            self.infiltration_rate_file = infiltration_rate_file
        if max_infiltration_capacity_file is not None:
            self.max_infiltration_capacity_file = max_infiltration_capacity_file
        if interception_file is not None:
            self.interception_file = interception_file

    @property
    def dem_file(self):
        """Gets the dem_file of this RasterOptions.  # noqa: E501


        :return: The dem_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._dem_file

    @dem_file.setter
    def dem_file(self, dem_file):
        """Sets the dem_file of this RasterOptions.


        :param dem_file: The dem_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                dem_file is not None and len(dem_file) > 80):
            self.__handle_validation_error("Invalid value for `dem_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dem_file is not None and len(dem_file) < 1):
            self.__handle_validation_error("Invalid value for `dem_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._dem_file = dem_file

    @property
    def dem_raw_file(self):
        """Gets the dem_raw_file of this RasterOptions.  # noqa: E501


        :return: The dem_raw_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._dem_raw_file

    @dem_raw_file.setter
    def dem_raw_file(self, dem_raw_file):
        """Sets the dem_raw_file of this RasterOptions.


        :param dem_raw_file: The dem_raw_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                dem_raw_file is not None and len(dem_raw_file) > 80):
            self.__handle_validation_error("Invalid value for `dem_raw_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dem_raw_file is not None and len(dem_raw_file) < 1):
            self.__handle_validation_error("Invalid value for `dem_raw_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._dem_raw_file = dem_raw_file

    @property
    def equilibrium_infiltration_rate_file(self):
        """Gets the equilibrium_infiltration_rate_file of this RasterOptions.  # noqa: E501


        :return: The equilibrium_infiltration_rate_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._equilibrium_infiltration_rate_file

    @equilibrium_infiltration_rate_file.setter
    def equilibrium_infiltration_rate_file(self, equilibrium_infiltration_rate_file):
        """Sets the equilibrium_infiltration_rate_file of this RasterOptions.


        :param equilibrium_infiltration_rate_file: The equilibrium_infiltration_rate_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                equilibrium_infiltration_rate_file is not None and len(equilibrium_infiltration_rate_file) > 80):
            self.__handle_validation_error("Invalid value for `equilibrium_infiltration_rate_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                equilibrium_infiltration_rate_file is not None and len(equilibrium_infiltration_rate_file) < 1):
            self.__handle_validation_error("Invalid value for `equilibrium_infiltration_rate_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._equilibrium_infiltration_rate_file = equilibrium_infiltration_rate_file

    @property
    def frict_coef_file(self):
        """Gets the frict_coef_file of this RasterOptions.  # noqa: E501


        :return: The frict_coef_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._frict_coef_file

    @frict_coef_file.setter
    def frict_coef_file(self, frict_coef_file):
        """Sets the frict_coef_file of this RasterOptions.


        :param frict_coef_file: The frict_coef_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                frict_coef_file is not None and len(frict_coef_file) > 80):
            self.__handle_validation_error("Invalid value for `frict_coef_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                frict_coef_file is not None and len(frict_coef_file) < 1):
            self.__handle_validation_error("Invalid value for `frict_coef_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._frict_coef_file = frict_coef_file

    @property
    def initial_groundwater_level_file(self):
        """Gets the initial_groundwater_level_file of this RasterOptions.  # noqa: E501


        :return: The initial_groundwater_level_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._initial_groundwater_level_file

    @initial_groundwater_level_file.setter
    def initial_groundwater_level_file(self, initial_groundwater_level_file):
        """Sets the initial_groundwater_level_file of this RasterOptions.


        :param initial_groundwater_level_file: The initial_groundwater_level_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                initial_groundwater_level_file is not None and len(initial_groundwater_level_file) > 80):
            self.__handle_validation_error("Invalid value for `initial_groundwater_level_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                initial_groundwater_level_file is not None and len(initial_groundwater_level_file) < 1):
            self.__handle_validation_error("Invalid value for `initial_groundwater_level_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._initial_groundwater_level_file = initial_groundwater_level_file

    @property
    def initial_waterlevel_file(self):
        """Gets the initial_waterlevel_file of this RasterOptions.  # noqa: E501


        :return: The initial_waterlevel_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._initial_waterlevel_file

    @initial_waterlevel_file.setter
    def initial_waterlevel_file(self, initial_waterlevel_file):
        """Sets the initial_waterlevel_file of this RasterOptions.


        :param initial_waterlevel_file: The initial_waterlevel_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                initial_waterlevel_file is not None and len(initial_waterlevel_file) > 80):
            self.__handle_validation_error("Invalid value for `initial_waterlevel_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                initial_waterlevel_file is not None and len(initial_waterlevel_file) < 1):
            self.__handle_validation_error("Invalid value for `initial_waterlevel_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._initial_waterlevel_file = initial_waterlevel_file

    @property
    def groundwater_hydro_connectivity_file(self):
        """Gets the groundwater_hydro_connectivity_file of this RasterOptions.  # noqa: E501


        :return: The groundwater_hydro_connectivity_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._groundwater_hydro_connectivity_file

    @groundwater_hydro_connectivity_file.setter
    def groundwater_hydro_connectivity_file(self, groundwater_hydro_connectivity_file):
        """Sets the groundwater_hydro_connectivity_file of this RasterOptions.


        :param groundwater_hydro_connectivity_file: The groundwater_hydro_connectivity_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                groundwater_hydro_connectivity_file is not None and len(groundwater_hydro_connectivity_file) > 80):
            self.__handle_validation_error("Invalid value for `groundwater_hydro_connectivity_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                groundwater_hydro_connectivity_file is not None and len(groundwater_hydro_connectivity_file) < 1):
            self.__handle_validation_error("Invalid value for `groundwater_hydro_connectivity_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._groundwater_hydro_connectivity_file = groundwater_hydro_connectivity_file

    @property
    def groundwater_impervious_layer_level_file(self):
        """Gets the groundwater_impervious_layer_level_file of this RasterOptions.  # noqa: E501


        :return: The groundwater_impervious_layer_level_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._groundwater_impervious_layer_level_file

    @groundwater_impervious_layer_level_file.setter
    def groundwater_impervious_layer_level_file(self, groundwater_impervious_layer_level_file):
        """Sets the groundwater_impervious_layer_level_file of this RasterOptions.


        :param groundwater_impervious_layer_level_file: The groundwater_impervious_layer_level_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                groundwater_impervious_layer_level_file is not None and len(groundwater_impervious_layer_level_file) > 80):
            self.__handle_validation_error("Invalid value for `groundwater_impervious_layer_level_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                groundwater_impervious_layer_level_file is not None and len(groundwater_impervious_layer_level_file) < 1):
            self.__handle_validation_error("Invalid value for `groundwater_impervious_layer_level_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._groundwater_impervious_layer_level_file = groundwater_impervious_layer_level_file

    @property
    def infiltration_decay_period_file(self):
        """Gets the infiltration_decay_period_file of this RasterOptions.  # noqa: E501


        :return: The infiltration_decay_period_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._infiltration_decay_period_file

    @infiltration_decay_period_file.setter
    def infiltration_decay_period_file(self, infiltration_decay_period_file):
        """Sets the infiltration_decay_period_file of this RasterOptions.


        :param infiltration_decay_period_file: The infiltration_decay_period_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                infiltration_decay_period_file is not None and len(infiltration_decay_period_file) > 80):
            self.__handle_validation_error("Invalid value for `infiltration_decay_period_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                infiltration_decay_period_file is not None and len(infiltration_decay_period_file) < 1):
            self.__handle_validation_error("Invalid value for `infiltration_decay_period_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._infiltration_decay_period_file = infiltration_decay_period_file

    @property
    def initial_infiltration_rate_file(self):
        """Gets the initial_infiltration_rate_file of this RasterOptions.  # noqa: E501


        :return: The initial_infiltration_rate_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._initial_infiltration_rate_file

    @initial_infiltration_rate_file.setter
    def initial_infiltration_rate_file(self, initial_infiltration_rate_file):
        """Sets the initial_infiltration_rate_file of this RasterOptions.


        :param initial_infiltration_rate_file: The initial_infiltration_rate_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                initial_infiltration_rate_file is not None and len(initial_infiltration_rate_file) > 80):
            self.__handle_validation_error("Invalid value for `initial_infiltration_rate_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                initial_infiltration_rate_file is not None and len(initial_infiltration_rate_file) < 1):
            self.__handle_validation_error("Invalid value for `initial_infiltration_rate_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._initial_infiltration_rate_file = initial_infiltration_rate_file

    @property
    def leakage_file(self):
        """Gets the leakage_file of this RasterOptions.  # noqa: E501


        :return: The leakage_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._leakage_file

    @leakage_file.setter
    def leakage_file(self, leakage_file):
        """Sets the leakage_file of this RasterOptions.


        :param leakage_file: The leakage_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                leakage_file is not None and len(leakage_file) > 80):
            self.__handle_validation_error("Invalid value for `leakage_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                leakage_file is not None and len(leakage_file) < 1):
            self.__handle_validation_error("Invalid value for `leakage_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._leakage_file = leakage_file

    @property
    def phreatic_storage_capacity_file(self):
        """Gets the phreatic_storage_capacity_file of this RasterOptions.  # noqa: E501


        :return: The phreatic_storage_capacity_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._phreatic_storage_capacity_file

    @phreatic_storage_capacity_file.setter
    def phreatic_storage_capacity_file(self, phreatic_storage_capacity_file):
        """Sets the phreatic_storage_capacity_file of this RasterOptions.


        :param phreatic_storage_capacity_file: The phreatic_storage_capacity_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phreatic_storage_capacity_file is not None and len(phreatic_storage_capacity_file) > 80):
            self.__handle_validation_error("Invalid value for `phreatic_storage_capacity_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                phreatic_storage_capacity_file is not None and len(phreatic_storage_capacity_file) < 1):
            self.__handle_validation_error("Invalid value for `phreatic_storage_capacity_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._phreatic_storage_capacity_file = phreatic_storage_capacity_file

    @property
    def hydraulic_conductivity_file(self):
        """Gets the hydraulic_conductivity_file of this RasterOptions.  # noqa: E501


        :return: The hydraulic_conductivity_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._hydraulic_conductivity_file

    @hydraulic_conductivity_file.setter
    def hydraulic_conductivity_file(self, hydraulic_conductivity_file):
        """Sets the hydraulic_conductivity_file of this RasterOptions.


        :param hydraulic_conductivity_file: The hydraulic_conductivity_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hydraulic_conductivity_file is not None and len(hydraulic_conductivity_file) > 80):
            self.__handle_validation_error("Invalid value for `hydraulic_conductivity_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hydraulic_conductivity_file is not None and len(hydraulic_conductivity_file) < 1):
            self.__handle_validation_error("Invalid value for `hydraulic_conductivity_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._hydraulic_conductivity_file = hydraulic_conductivity_file

    @property
    def porosity_file(self):
        """Gets the porosity_file of this RasterOptions.  # noqa: E501


        :return: The porosity_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._porosity_file

    @porosity_file.setter
    def porosity_file(self, porosity_file):
        """Sets the porosity_file of this RasterOptions.


        :param porosity_file: The porosity_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                porosity_file is not None and len(porosity_file) > 80):
            self.__handle_validation_error("Invalid value for `porosity_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                porosity_file is not None and len(porosity_file) < 1):
            self.__handle_validation_error("Invalid value for `porosity_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._porosity_file = porosity_file

    @property
    def infiltration_rate_file(self):
        """Gets the infiltration_rate_file of this RasterOptions.  # noqa: E501


        :return: The infiltration_rate_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._infiltration_rate_file

    @infiltration_rate_file.setter
    def infiltration_rate_file(self, infiltration_rate_file):
        """Sets the infiltration_rate_file of this RasterOptions.


        :param infiltration_rate_file: The infiltration_rate_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                infiltration_rate_file is not None and len(infiltration_rate_file) > 80):
            self.__handle_validation_error("Invalid value for `infiltration_rate_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                infiltration_rate_file is not None and len(infiltration_rate_file) < 1):
            self.__handle_validation_error("Invalid value for `infiltration_rate_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._infiltration_rate_file = infiltration_rate_file

    @property
    def max_infiltration_capacity_file(self):
        """Gets the max_infiltration_capacity_file of this RasterOptions.  # noqa: E501


        :return: The max_infiltration_capacity_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._max_infiltration_capacity_file

    @max_infiltration_capacity_file.setter
    def max_infiltration_capacity_file(self, max_infiltration_capacity_file):
        """Sets the max_infiltration_capacity_file of this RasterOptions.


        :param max_infiltration_capacity_file: The max_infiltration_capacity_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                max_infiltration_capacity_file is not None and len(max_infiltration_capacity_file) > 80):
            self.__handle_validation_error("Invalid value for `max_infiltration_capacity_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_infiltration_capacity_file is not None and len(max_infiltration_capacity_file) < 1):
            self.__handle_validation_error("Invalid value for `max_infiltration_capacity_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._max_infiltration_capacity_file = max_infiltration_capacity_file

    @property
    def interception_file(self):
        """Gets the interception_file of this RasterOptions.  # noqa: E501


        :return: The interception_file of this RasterOptions.  # noqa: E501
        :rtype: str
        """
        return self._interception_file

    @interception_file.setter
    def interception_file(self, interception_file):
        """Sets the interception_file of this RasterOptions.


        :param interception_file: The interception_file of this RasterOptions.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                interception_file is not None and len(interception_file) > 80):
            self.__handle_validation_error("Invalid value for `interception_file`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                interception_file is not None and len(interception_file) < 1):
            self.__handle_validation_error("Invalid value for `interception_file`, length must be greater than or equal to `1`")  # noqa: E501

        self._interception_file = interception_file

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
        if not isinstance(other, RasterOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RasterOptions):
            return True

        return self.to_dict() != other.to_dict()
