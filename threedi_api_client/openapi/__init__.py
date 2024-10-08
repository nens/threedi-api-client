# coding: utf-8

# flake8: noqa

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.4.3   3Di core release: 3.5.0  deployed on:  03:07PM (UTC) on October 02, 2024  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from threedi_api_client.openapi.api.v3_api import V3Api
from threedi_api_client.openapi.api.v3_beta_api import V3BetaApi

# import ApiClient
from threedi_api_client.openapi.api_client import ApiClient
from threedi_api_client.openapi.configuration import Configuration
from threedi_api_client.openapi.exceptions import OpenApiException
from threedi_api_client.openapi.exceptions import ApiTypeError
from threedi_api_client.openapi.exceptions import ApiValueError
from threedi_api_client.openapi.exceptions import ApiKeyError
from threedi_api_client.openapi.exceptions import ApiException
# import models into sdk package
from threedi_api_client.openapi.models.action import Action
from threedi_api_client.openapi.models.aggregation_settings import AggregationSettings
from threedi_api_client.openapi.models.arrival_time_post_processing import ArrivalTimePostProcessing
from threedi_api_client.openapi.models.authenticate import Authenticate
from threedi_api_client.openapi.models.base_event_state import BaseEventState
from threedi_api_client.openapi.models.basic_post_processing import BasicPostProcessing
from threedi_api_client.openapi.models.boundary_condition import BoundaryCondition
from threedi_api_client.openapi.models.breach import Breach
from threedi_api_client.openapi.models.breach_graph import BreachGraph
from threedi_api_client.openapi.models.breach_graph_request import BreachGraphRequest
from threedi_api_client.openapi.models.commit import Commit
from threedi_api_client.openapi.models.constant_lateral import ConstantLateral
from threedi_api_client.openapi.models.constant_leakage import ConstantLeakage
from threedi_api_client.openapi.models.constant_local_rain import ConstantLocalRain
from threedi_api_client.openapi.models.constant_rain import ConstantRain
from threedi_api_client.openapi.models.constant_sources_sinks import ConstantSourcesSinks
from threedi_api_client.openapi.models.constant_wind import ConstantWind
from threedi_api_client.openapi.models.contract import Contract
from threedi_api_client.openapi.models.create_revision import CreateRevision
from threedi_api_client.openapi.models.create_template import CreateTemplate
from threedi_api_client.openapi.models.create_threedimodel import CreateThreedimodel
from threedi_api_client.openapi.models.current_status import CurrentStatus
from threedi_api_client.openapi.models.current_version import CurrentVersion
from threedi_api_client.openapi.models.customized_result_area import CustomizedResultArea
from threedi_api_client.openapi.models.damage_estimation import DamageEstimation
from threedi_api_client.openapi.models.damage_post_processing import DamagePostProcessing
from threedi_api_client.openapi.models.destroy_revision import DestroyRevision
from threedi_api_client.openapi.models.download import Download
from threedi_api_client.openapi.models.event import Event
from threedi_api_client.openapi.models.extent import Extent
from threedi_api_client.openapi.models.file import File
from threedi_api_client.openapi.models.file_boundary_condition import FileBoundaryCondition
from threedi_api_client.openapi.models.file_lateral import FileLateral
from threedi_api_client.openapi.models.file_meta import FileMeta
from threedi_api_client.openapi.models.file_raster_leakage import FileRasterLeakage
from threedi_api_client.openapi.models.file_raster_rain import FileRasterRain
from threedi_api_client.openapi.models.file_raster_sources_sinks import FileRasterSourcesSinks
from threedi_api_client.openapi.models.file_read_only import FileReadOnly
from threedi_api_client.openapi.models.file_structure_control import FileStructureControl
from threedi_api_client.openapi.models.file_timeseries_leakage import FileTimeseriesLeakage
from threedi_api_client.openapi.models.file_timeseries_rain import FileTimeseriesRain
from threedi_api_client.openapi.models.file_timeseries_sources_sinks import FileTimeseriesSourcesSinks
from threedi_api_client.openapi.models.forcing_substance import ForcingSubstance
from threedi_api_client.openapi.models.from_template import FromTemplate
from threedi_api_client.openapi.models.grid_event_state import GridEventState
from threedi_api_client.openapi.models.ground_water_level import GroundWaterLevel
from threedi_api_client.openapi.models.ground_water_raster import GroundWaterRaster
from threedi_api_client.openapi.models.ground_water_substance_concentration import GroundWaterSubstanceConcentration
from threedi_api_client.openapi.models.initial_concentration import InitialConcentration
from threedi_api_client.openapi.models.initial_saved_state import InitialSavedState
from threedi_api_client.openapi.models.initial_saved_state_overview import InitialSavedStateOverview
from threedi_api_client.openapi.models.initial_waterlevel import InitialWaterlevel
from threedi_api_client.openapi.models.inline_response200 import InlineResponse200
from threedi_api_client.openapi.models.inline_response2001 import InlineResponse2001
from threedi_api_client.openapi.models.inline_response20010 import InlineResponse20010
from threedi_api_client.openapi.models.inline_response20011 import InlineResponse20011
from threedi_api_client.openapi.models.inline_response20012 import InlineResponse20012
from threedi_api_client.openapi.models.inline_response20013 import InlineResponse20013
from threedi_api_client.openapi.models.inline_response20014 import InlineResponse20014
from threedi_api_client.openapi.models.inline_response20015 import InlineResponse20015
from threedi_api_client.openapi.models.inline_response20016 import InlineResponse20016
from threedi_api_client.openapi.models.inline_response20017 import InlineResponse20017
from threedi_api_client.openapi.models.inline_response20018 import InlineResponse20018
from threedi_api_client.openapi.models.inline_response20019 import InlineResponse20019
from threedi_api_client.openapi.models.inline_response2002 import InlineResponse2002
from threedi_api_client.openapi.models.inline_response20020 import InlineResponse20020
from threedi_api_client.openapi.models.inline_response20021 import InlineResponse20021
from threedi_api_client.openapi.models.inline_response20022 import InlineResponse20022
from threedi_api_client.openapi.models.inline_response20023 import InlineResponse20023
from threedi_api_client.openapi.models.inline_response20024 import InlineResponse20024
from threedi_api_client.openapi.models.inline_response20025 import InlineResponse20025
from threedi_api_client.openapi.models.inline_response20026 import InlineResponse20026
from threedi_api_client.openapi.models.inline_response20027 import InlineResponse20027
from threedi_api_client.openapi.models.inline_response20028 import InlineResponse20028
from threedi_api_client.openapi.models.inline_response20029 import InlineResponse20029
from threedi_api_client.openapi.models.inline_response2003 import InlineResponse2003
from threedi_api_client.openapi.models.inline_response20030 import InlineResponse20030
from threedi_api_client.openapi.models.inline_response20031 import InlineResponse20031
from threedi_api_client.openapi.models.inline_response20032 import InlineResponse20032
from threedi_api_client.openapi.models.inline_response20033 import InlineResponse20033
from threedi_api_client.openapi.models.inline_response20034 import InlineResponse20034
from threedi_api_client.openapi.models.inline_response20035 import InlineResponse20035
from threedi_api_client.openapi.models.inline_response20036 import InlineResponse20036
from threedi_api_client.openapi.models.inline_response20037 import InlineResponse20037
from threedi_api_client.openapi.models.inline_response20038 import InlineResponse20038
from threedi_api_client.openapi.models.inline_response20039 import InlineResponse20039
from threedi_api_client.openapi.models.inline_response2004 import InlineResponse2004
from threedi_api_client.openapi.models.inline_response20040 import InlineResponse20040
from threedi_api_client.openapi.models.inline_response20041 import InlineResponse20041
from threedi_api_client.openapi.models.inline_response20042 import InlineResponse20042
from threedi_api_client.openapi.models.inline_response20043 import InlineResponse20043
from threedi_api_client.openapi.models.inline_response20044 import InlineResponse20044
from threedi_api_client.openapi.models.inline_response20045 import InlineResponse20045
from threedi_api_client.openapi.models.inline_response20046 import InlineResponse20046
from threedi_api_client.openapi.models.inline_response20047 import InlineResponse20047
from threedi_api_client.openapi.models.inline_response20048 import InlineResponse20048
from threedi_api_client.openapi.models.inline_response20049 import InlineResponse20049
from threedi_api_client.openapi.models.inline_response2005 import InlineResponse2005
from threedi_api_client.openapi.models.inline_response20050 import InlineResponse20050
from threedi_api_client.openapi.models.inline_response20051 import InlineResponse20051
from threedi_api_client.openapi.models.inline_response20052 import InlineResponse20052
from threedi_api_client.openapi.models.inline_response20053 import InlineResponse20053
from threedi_api_client.openapi.models.inline_response20054 import InlineResponse20054
from threedi_api_client.openapi.models.inline_response20055 import InlineResponse20055
from threedi_api_client.openapi.models.inline_response20056 import InlineResponse20056
from threedi_api_client.openapi.models.inline_response20057 import InlineResponse20057
from threedi_api_client.openapi.models.inline_response20058 import InlineResponse20058
from threedi_api_client.openapi.models.inline_response20059 import InlineResponse20059
from threedi_api_client.openapi.models.inline_response2006 import InlineResponse2006
from threedi_api_client.openapi.models.inline_response20060 import InlineResponse20060
from threedi_api_client.openapi.models.inline_response20061 import InlineResponse20061
from threedi_api_client.openapi.models.inline_response20062 import InlineResponse20062
from threedi_api_client.openapi.models.inline_response20063 import InlineResponse20063
from threedi_api_client.openapi.models.inline_response20064 import InlineResponse20064
from threedi_api_client.openapi.models.inline_response20065 import InlineResponse20065
from threedi_api_client.openapi.models.inline_response20066 import InlineResponse20066
from threedi_api_client.openapi.models.inline_response20067 import InlineResponse20067
from threedi_api_client.openapi.models.inline_response20068 import InlineResponse20068
from threedi_api_client.openapi.models.inline_response20069 import InlineResponse20069
from threedi_api_client.openapi.models.inline_response2007 import InlineResponse2007
from threedi_api_client.openapi.models.inline_response20070 import InlineResponse20070
from threedi_api_client.openapi.models.inline_response20071 import InlineResponse20071
from threedi_api_client.openapi.models.inline_response20072 import InlineResponse20072
from threedi_api_client.openapi.models.inline_response20073 import InlineResponse20073
from threedi_api_client.openapi.models.inline_response20074 import InlineResponse20074
from threedi_api_client.openapi.models.inline_response20075 import InlineResponse20075
from threedi_api_client.openapi.models.inline_response20076 import InlineResponse20076
from threedi_api_client.openapi.models.inline_response20077 import InlineResponse20077
from threedi_api_client.openapi.models.inline_response20078 import InlineResponse20078
from threedi_api_client.openapi.models.inline_response20079 import InlineResponse20079
from threedi_api_client.openapi.models.inline_response2008 import InlineResponse2008
from threedi_api_client.openapi.models.inline_response20080 import InlineResponse20080
from threedi_api_client.openapi.models.inline_response2009 import InlineResponse2009
from threedi_api_client.openapi.models.inpy_version import InpyVersion
from threedi_api_client.openapi.models.lateral import Lateral
from threedi_api_client.openapi.models.linestring import Linestring
from threedi_api_client.openapi.models.lizard_raster_rain import LizardRasterRain
from threedi_api_client.openapi.models.lizard_raster_sources_sinks import LizardRasterSourcesSinks
from threedi_api_client.openapi.models.lizard_timeseries_rain import LizardTimeseriesRain
from threedi_api_client.openapi.models.lizard_timeseries_sources_sinks import LizardTimeseriesSourcesSinks
from threedi_api_client.openapi.models.local_rain import LocalRain
from threedi_api_client.openapi.models.measure_location import MeasureLocation
from threedi_api_client.openapi.models.measure_location_grid_event_state import MeasureLocationGridEventState
from threedi_api_client.openapi.models.measure_specification import MeasureSpecification
from threedi_api_client.openapi.models.memory_structure_control import MemoryStructureControl
from threedi_api_client.openapi.models.net_cdf_raster_leakage import NetCDFRasterLeakage
from threedi_api_client.openapi.models.net_cdf_raster_rain import NetCDFRasterRain
from threedi_api_client.openapi.models.net_cdf_raster_sources_sinks import NetCDFRasterSourcesSinks
from threedi_api_client.openapi.models.net_cdf_timeseries_leakage import NetCDFTimeseriesLeakage
from threedi_api_client.openapi.models.net_cdf_timeseries_rain import NetCDFTimeseriesRain
from threedi_api_client.openapi.models.net_cdf_timeseries_sources_sinks import NetCDFTimeseriesSourcesSinks
from threedi_api_client.openapi.models.numerical_settings import NumericalSettings
from threedi_api_client.openapi.models.obstacle_edit import ObstacleEdit
from threedi_api_client.openapi.models.one_d_substance_concentration import OneDSubstanceConcentration
from threedi_api_client.openapi.models.one_d_water_level import OneDWaterLevel
from threedi_api_client.openapi.models.one_d_water_level_file import OneDWaterLevelFile
from threedi_api_client.openapi.models.one_d_water_level_predefined import OneDWaterLevelPredefined
from threedi_api_client.openapi.models.organisation import Organisation
from threedi_api_client.openapi.models.organisation_role import OrganisationRole
from threedi_api_client.openapi.models.organisation_settings import OrganisationSettings
from threedi_api_client.openapi.models.organisation_user import OrganisationUser
from threedi_api_client.openapi.models.organisation_user_role_patch import OrganisationUserRolePatch
from threedi_api_client.openapi.models.output_settings import OutputSettings
from threedi_api_client.openapi.models.personal_api_key import PersonalAPIKey
from threedi_api_client.openapi.models.personal_api_key_with_secret import PersonalAPIKeyWithSecret
from threedi_api_client.openapi.models.physical_settings import PhysicalSettings
from threedi_api_client.openapi.models.point import Point
from threedi_api_client.openapi.models.polygon import Polygon
from threedi_api_client.openapi.models.post_processing_overview import PostProcessingOverview
from threedi_api_client.openapi.models.post_processing_queue import PostProcessingQueue
from threedi_api_client.openapi.models.post_processing_status import PostProcessingStatus
from threedi_api_client.openapi.models.potential_breach import PotentialBreach
from threedi_api_client.openapi.models.profile import Profile
from threedi_api_client.openapi.models.progress import Progress
from threedi_api_client.openapi.models.pump_discharge_graph import PumpDischargeGraph
from threedi_api_client.openapi.models.pump_discharge_graph_request import PumpDischargeGraphRequest
from threedi_api_client.openapi.models.rain_graph import RainGraph
from threedi_api_client.openapi.models.rain_graph_request import RainGraphRequest
from threedi_api_client.openapi.models.raster import Raster
from threedi_api_client.openapi.models.raster_create import RasterCreate
from threedi_api_client.openapi.models.raster_edit import RasterEdit
from threedi_api_client.openapi.models.raster_edit_urls import RasterEditUrls
from threedi_api_client.openapi.models.raster_options import RasterOptions
from threedi_api_client.openapi.models.refresh import Refresh
from threedi_api_client.openapi.models.repository import Repository
from threedi_api_client.openapi.models.result import Result
from threedi_api_client.openapi.models.result_file import ResultFile
from threedi_api_client.openapi.models.revision import Revision
from threedi_api_client.openapi.models.revision_raster import RevisionRaster
from threedi_api_client.openapi.models.revision_task import RevisionTask
from threedi_api_client.openapi.models.role import Role
from threedi_api_client.openapi.models.saved_state_overview import SavedStateOverview
from threedi_api_client.openapi.models.schematisation import Schematisation
from threedi_api_client.openapi.models.schematisation_revision import SchematisationRevision
from threedi_api_client.openapi.models.settings import Settings
from threedi_api_client.openapi.models.simulation import Simulation
from threedi_api_client.openapi.models.simulation_channel import SimulationChannel
from threedi_api_client.openapi.models.simulation_settings_overview import SimulationSettingsOverview
from threedi_api_client.openapi.models.simulation_status import SimulationStatus
from threedi_api_client.openapi.models.simulation_status_statistics import SimulationStatusStatistics
from threedi_api_client.openapi.models.simulation_update import SimulationUpdate
from threedi_api_client.openapi.models.sqlite import Sqlite
from threedi_api_client.openapi.models.sqlite_file_upload import SqliteFileUpload
from threedi_api_client.openapi.models.stable_threshold_saved_state import StableThresholdSavedState
from threedi_api_client.openapi.models.status import Status
from threedi_api_client.openapi.models.substance import Substance
from threedi_api_client.openapi.models.tms import TMS
from threedi_api_client.openapi.models.table_structure_control import TableStructureControl
from threedi_api_client.openapi.models.template import Template
from threedi_api_client.openapi.models.threedi_model import ThreediModel
from threedi_api_client.openapi.models.threedi_model_saved_state import ThreediModelSavedState
from threedi_api_client.openapi.models.threedi_model_task import ThreediModelTask
from threedi_api_client.openapi.models.threshold import Threshold
from threedi_api_client.openapi.models.time_step_settings import TimeStepSettings
from threedi_api_client.openapi.models.timed_saved_state_update import TimedSavedStateUpdate
from threedi_api_client.openapi.models.timed_structure_control import TimedStructureControl
from threedi_api_client.openapi.models.timeout import Timeout
from threedi_api_client.openapi.models.timeseries_lateral import TimeseriesLateral
from threedi_api_client.openapi.models.timeseries_leakage import TimeseriesLeakage
from threedi_api_client.openapi.models.timeseries_leakage_overview import TimeseriesLeakageOverview
from threedi_api_client.openapi.models.timeseries_local_rain import TimeseriesLocalRain
from threedi_api_client.openapi.models.timeseries_rain import TimeseriesRain
from threedi_api_client.openapi.models.timeseries_rain_overview import TimeseriesRainOverview
from threedi_api_client.openapi.models.timeseries_sources_sinks import TimeseriesSourcesSinks
from threedi_api_client.openapi.models.timeseries_sources_sinks_overview import TimeseriesSourcesSinksOverview
from threedi_api_client.openapi.models.timeseries_wind import TimeseriesWind
from threedi_api_client.openapi.models.tokens import Tokens
from threedi_api_client.openapi.models.two_d_substance_concentration import TwoDSubstanceConcentration
from threedi_api_client.openapi.models.two_d_water_level import TwoDWaterLevel
from threedi_api_client.openapi.models.two_d_water_raster import TwoDWaterRaster
from threedi_api_client.openapi.models.update_revision import UpdateRevision
from threedi_api_client.openapi.models.update_template import UpdateTemplate
from threedi_api_client.openapi.models.upload import Upload
from threedi_api_client.openapi.models.upload_event_file import UploadEventFile
from threedi_api_client.openapi.models.upload_with_substances import UploadWithSubstances
from threedi_api_client.openapi.models.usage import Usage
from threedi_api_client.openapi.models.usage_statistics import UsageStatistics
from threedi_api_client.openapi.models.user import User
from threedi_api_client.openapi.models.user_tokens import UserTokens
from threedi_api_client.openapi.models.water_flow_graph_request import WaterFlowGraphRequest
from threedi_api_client.openapi.models.water_graph import WaterGraph
from threedi_api_client.openapi.models.water_level_graph_request import WaterLevelGraphRequest
from threedi_api_client.openapi.models.water_level_profile import WaterLevelProfile
from threedi_api_client.openapi.models.water_level_profile_request import WaterLevelProfileRequest
from threedi_api_client.openapi.models.water_quality_customized_result_area import WaterQualityCustomizedResultArea
from threedi_api_client.openapi.models.water_quality_output_settings import WaterQualityOutputSettings
from threedi_api_client.openapi.models.water_quality_settings import WaterQualitySettings
from threedi_api_client.openapi.models.waterdepth import Waterdepth
from threedi_api_client.openapi.models.wind import Wind
from threedi_api_client.openapi.models.wind_drag_coefficient import WindDragCoefficient

