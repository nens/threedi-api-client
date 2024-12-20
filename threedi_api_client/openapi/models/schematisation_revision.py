# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 3.4.24   3Di core release: 3.5.4.1  deployed on:  08:40AM (UTC) on December 20, 2024  # noqa: E501

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

class SchematisationRevision(object):
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
        'id': 'int',
        'created': 'datetime',
        'schematisation': 'str',
        'schematisation_id': 'int',
        'number': 'int',
        'sqlite': 'Sqlite',
        'rasters': 'list[RevisionRaster]',
        'archived': 'datetime',
        'commit_date': 'datetime',
        'commit_user': 'str',
        'commit_first_name': 'str',
        'commit_last_name': 'str',
        'commit_message': 'str',
        'is_valid': 'bool',
        'has_threedimodel': 'bool',
        'tags': 'list[str]'
    }

    required_fields = [
    ]

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created': 'created',
        'schematisation': 'schematisation',
        'schematisation_id': 'schematisation_id',
        'number': 'number',
        'sqlite': 'sqlite',
        'rasters': 'rasters',
        'archived': 'archived',
        'commit_date': 'commit_date',
        'commit_user': 'commit_user',
        'commit_first_name': 'commit_first_name',
        'commit_last_name': 'commit_last_name',
        'commit_message': 'commit_message',
        'is_valid': 'is_valid',
        'has_threedimodel': 'has_threedimodel',
        'tags': 'tags'
    }

    def __init__(self, url=None, id=None, created=None, schematisation=None, schematisation_id=None, number=None, sqlite=None, rasters=None, archived=None, commit_date=None, commit_user=None, commit_first_name=None, commit_last_name=None, commit_message=None, is_valid=None, has_threedimodel=None, tags=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """SchematisationRevision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._id = None
        self._created = None
        self._schematisation = None
        self._schematisation_id = None
        self._number = None
        self._sqlite = None
        self._rasters = None
        self._archived = None
        self._commit_date = None
        self._commit_user = None
        self._commit_first_name = None
        self._commit_last_name = None
        self._commit_message = None
        self._is_valid = None
        self._has_threedimodel = None
        self._tags = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        self.created = created
        if schematisation is not None:
            self.schematisation = schematisation
        if schematisation_id is not None:
            self.schematisation_id = schematisation_id
        if number is not None:
            self.number = number
        if sqlite is not None:
            self.sqlite = sqlite
        if rasters is not None:
            self.rasters = rasters
        self.archived = archived
        self.commit_date = commit_date
        if commit_user is not None:
            self.commit_user = commit_user
        if commit_first_name is not None:
            self.commit_first_name = commit_first_name
        if commit_last_name is not None:
            self.commit_last_name = commit_last_name
        self.commit_message = commit_message
        self.is_valid = is_valid
        if has_threedimodel is not None:
            self.has_threedimodel = has_threedimodel
        if tags is not None:
            self.tags = tags

    @property
    def url(self):
        """Gets the url of this SchematisationRevision.  # noqa: E501


        :return: The url of this SchematisationRevision.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SchematisationRevision.


        :param url: The url of this SchematisationRevision.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this SchematisationRevision.  # noqa: E501


        :return: The id of this SchematisationRevision.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SchematisationRevision.


        :param id: The id of this SchematisationRevision.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this SchematisationRevision.  # noqa: E501


        :return: The created of this SchematisationRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SchematisationRevision.


        :param created: The created of this SchematisationRevision.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def schematisation(self):
        """Gets the schematisation of this SchematisationRevision.  # noqa: E501


        :return: The schematisation of this SchematisationRevision.  # noqa: E501
        :rtype: str
        """
        return self._schematisation

    @schematisation.setter
    def schematisation(self, schematisation):
        """Sets the schematisation of this SchematisationRevision.


        :param schematisation: The schematisation of this SchematisationRevision.  # noqa: E501
        :type: str
        """

        self._schematisation = schematisation

    @property
    def schematisation_id(self):
        """Gets the schematisation_id of this SchematisationRevision.  # noqa: E501


        :return: The schematisation_id of this SchematisationRevision.  # noqa: E501
        :rtype: int
        """
        return self._schematisation_id

    @schematisation_id.setter
    def schematisation_id(self, schematisation_id):
        """Sets the schematisation_id of this SchematisationRevision.


        :param schematisation_id: The schematisation_id of this SchematisationRevision.  # noqa: E501
        :type: int
        """

        self._schematisation_id = schematisation_id

    @property
    def number(self):
        """Gets the number of this SchematisationRevision.  # noqa: E501


        :return: The number of this SchematisationRevision.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SchematisationRevision.


        :param number: The number of this SchematisationRevision.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def sqlite(self):
        """Gets the sqlite of this SchematisationRevision.  # noqa: E501


        :return: The sqlite of this SchematisationRevision.  # noqa: E501
        :rtype: Sqlite
        """
        return self._sqlite

    @sqlite.setter
    def sqlite(self, sqlite):
        """Sets the sqlite of this SchematisationRevision.


        :param sqlite: The sqlite of this SchematisationRevision.  # noqa: E501
        :type: Sqlite
        """

        self._sqlite = sqlite

    @property
    def rasters(self):
        """Gets the rasters of this SchematisationRevision.  # noqa: E501


        :return: The rasters of this SchematisationRevision.  # noqa: E501
        :rtype: list[RevisionRaster]
        """
        return self._rasters

    @rasters.setter
    def rasters(self, rasters):
        """Sets the rasters of this SchematisationRevision.


        :param rasters: The rasters of this SchematisationRevision.  # noqa: E501
        :type: list[RevisionRaster]
        """

        self._rasters = rasters

    @property
    def archived(self):
        """Gets the archived of this SchematisationRevision.  # noqa: E501


        :return: The archived of this SchematisationRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this SchematisationRevision.


        :param archived: The archived of this SchematisationRevision.  # noqa: E501
        :type: datetime
        """

        self._archived = archived

    @property
    def commit_date(self):
        """Gets the commit_date of this SchematisationRevision.  # noqa: E501


        :return: The commit_date of this SchematisationRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._commit_date

    @commit_date.setter
    def commit_date(self, commit_date):
        """Sets the commit_date of this SchematisationRevision.


        :param commit_date: The commit_date of this SchematisationRevision.  # noqa: E501
        :type: datetime
        """

        self._commit_date = commit_date

    @property
    def commit_user(self):
        """Gets the commit_user of this SchematisationRevision.  # noqa: E501

        The username of a user  # noqa: E501

        :return: The commit_user of this SchematisationRevision.  # noqa: E501
        :rtype: str
        """
        return self._commit_user

    @commit_user.setter
    def commit_user(self, commit_user):
        """Sets the commit_user of this SchematisationRevision.

        The username of a user  # noqa: E501

        :param commit_user: The commit_user of this SchematisationRevision.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commit_user is not None and not re.search(r'^[\w.@+-]+$', commit_user)):  # noqa: E501
            self.__handle_validation_error(r"Invalid value for `commit_user`, must be a follow pattern or equal to `/^[\w.@+-]+$/`")  # noqa: E501

        self._commit_user = commit_user

    @property
    def commit_first_name(self):
        """Gets the commit_first_name of this SchematisationRevision.  # noqa: E501


        :return: The commit_first_name of this SchematisationRevision.  # noqa: E501
        :rtype: str
        """
        return self._commit_first_name

    @commit_first_name.setter
    def commit_first_name(self, commit_first_name):
        """Sets the commit_first_name of this SchematisationRevision.


        :param commit_first_name: The commit_first_name of this SchematisationRevision.  # noqa: E501
        :type: str
        """

        self._commit_first_name = commit_first_name

    @property
    def commit_last_name(self):
        """Gets the commit_last_name of this SchematisationRevision.  # noqa: E501


        :return: The commit_last_name of this SchematisationRevision.  # noqa: E501
        :rtype: str
        """
        return self._commit_last_name

    @commit_last_name.setter
    def commit_last_name(self, commit_last_name):
        """Sets the commit_last_name of this SchematisationRevision.


        :param commit_last_name: The commit_last_name of this SchematisationRevision.  # noqa: E501
        :type: str
        """

        self._commit_last_name = commit_last_name

    @property
    def commit_message(self):
        """Gets the commit_message of this SchematisationRevision.  # noqa: E501


        :return: The commit_message of this SchematisationRevision.  # noqa: E501
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this SchematisationRevision.


        :param commit_message: The commit_message of this SchematisationRevision.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commit_message is not None and len(commit_message) < 1):
            self.__handle_validation_error("Invalid value for `commit_message`, length must be greater than or equal to `1`")  # noqa: E501

        self._commit_message = commit_message

    @property
    def is_valid(self):
        """Gets the is_valid of this SchematisationRevision.  # noqa: E501


        :return: The is_valid of this SchematisationRevision.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this SchematisationRevision.


        :param is_valid: The is_valid of this SchematisationRevision.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def has_threedimodel(self):
        """Gets the has_threedimodel of this SchematisationRevision.  # noqa: E501


        :return: The has_threedimodel of this SchematisationRevision.  # noqa: E501
        :rtype: bool
        """
        return self._has_threedimodel

    @has_threedimodel.setter
    def has_threedimodel(self, has_threedimodel):
        """Sets the has_threedimodel of this SchematisationRevision.


        :param has_threedimodel: The has_threedimodel of this SchematisationRevision.  # noqa: E501
        :type: bool
        """

        self._has_threedimodel = has_threedimodel

    @property
    def tags(self):
        """Gets the tags of this SchematisationRevision.  # noqa: E501

        tags provided as a list of strings  # noqa: E501

        :return: The tags of this SchematisationRevision.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SchematisationRevision.

        tags provided as a list of strings  # noqa: E501

        :param tags: The tags of this SchematisationRevision.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, SchematisationRevision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SchematisationRevision):
            return True

        return self.to_dict() != other.to_dict()
