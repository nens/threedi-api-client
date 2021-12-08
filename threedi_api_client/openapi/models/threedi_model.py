# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.1.1   3Di core release: 2.1.9  deployed on:  02:45PM (UTC) on December 08, 2021  # noqa: E501

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

class ThreediModel(object):
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
        'user': 'str',
        'inpy_version': 'str',
        'revision': 'str',
        'revision_id': 'int',
        'revision_hash': 'str',
        'revision_number': 'str',
        'revision_commit_date': 'str',
        'schematisation_id': 'int',
        'schematisation_name': 'str',
        'repository_slug': 'str',
        'name': 'str',
        'slug': 'str',
        'disabled': 'bool',
        'epsg': 'int',
        'inp_success': 'bool',
        'description': 'str',
        'storage_space': 'int',
        'storage_space_humanized': 'str',
        'model_ini': 'str',
        'breach_count': 'str',
        'extent_two_d': 'Extent',
        'extent_one_d': 'Extent',
        'extent_zero_d': 'Extent',
        'nodes_count': 'int',
        'lines_count': 'int'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'user': 'user',
        'inpy_version': 'inpy_version',
        'revision': 'revision',
        'revision_id': 'revision_id',
        'revision_hash': 'revision_hash',
        'revision_number': 'revision_number',
        'revision_commit_date': 'revision_commit_date',
        'schematisation_id': 'schematisation_id',
        'schematisation_name': 'schematisation_name',
        'repository_slug': 'repository_slug',
        'name': 'name',
        'slug': 'slug',
        'disabled': 'disabled',
        'epsg': 'epsg',
        'inp_success': 'inp_success',
        'description': 'description',
        'storage_space': 'storage_space',
        'storage_space_humanized': 'storage_space_humanized',
        'model_ini': 'model_ini',
        'breach_count': 'breach_count',
        'extent_two_d': 'extent_two_d',
        'extent_one_d': 'extent_one_d',
        'extent_zero_d': 'extent_zero_d',
        'nodes_count': 'nodes_count',
        'lines_count': 'lines_count'
    }

    def __init__(self, url=None, id=None, user=None, inpy_version=None, revision=None, revision_id=None, revision_hash=None, revision_number=None, revision_commit_date=None, schematisation_id=None, schematisation_name=None, repository_slug=None, name=None, slug=None, disabled=None, epsg=None, inp_success=None, description=None, storage_space=None, storage_space_humanized=None, model_ini=None, breach_count=None, extent_two_d=None, extent_one_d=None, extent_zero_d=None, nodes_count=None, lines_count=None, local_vars_configuration=None):  # noqa: E501
        """ThreediModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._id = None
        self._user = None
        self._inpy_version = None
        self._revision = None
        self._revision_id = None
        self._revision_hash = None
        self._revision_number = None
        self._revision_commit_date = None
        self._schematisation_id = None
        self._schematisation_name = None
        self._repository_slug = None
        self._name = None
        self._slug = None
        self._disabled = None
        self._epsg = None
        self._inp_success = None
        self._description = None
        self._storage_space = None
        self._storage_space_humanized = None
        self._model_ini = None
        self._breach_count = None
        self._extent_two_d = None
        self._extent_one_d = None
        self._extent_zero_d = None
        self._nodes_count = None
        self._lines_count = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        self.inpy_version = inpy_version
        self.revision = revision
        if revision_id is not None:
            self.revision_id = revision_id
        if revision_hash is not None:
            self.revision_hash = revision_hash
        if revision_number is not None:
            self.revision_number = revision_number
        if revision_commit_date is not None:
            self.revision_commit_date = revision_commit_date
        if schematisation_id is not None:
            self.schematisation_id = schematisation_id
        if schematisation_name is not None:
            self.schematisation_name = schematisation_name
        if repository_slug is not None:
            self.repository_slug = repository_slug
        if name is not None:
            self.name = name
        self.slug = slug
        if disabled is not None:
            self.disabled = disabled
        self.epsg = epsg
        self.inp_success = inp_success
        self.description = description
        if storage_space is not None:
            self.storage_space = storage_space
        if storage_space_humanized is not None:
            self.storage_space_humanized = storage_space_humanized
        self.model_ini = model_ini
        if breach_count is not None:
            self.breach_count = breach_count
        if extent_two_d is not None:
            self.extent_two_d = extent_two_d
        if extent_one_d is not None:
            self.extent_one_d = extent_one_d
        if extent_zero_d is not None:
            self.extent_zero_d = extent_zero_d
        self.nodes_count = nodes_count
        self.lines_count = lines_count

    @property
    def url(self):
        """Gets the url of this ThreediModel.  # noqa: E501


        :return: The url of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ThreediModel.


        :param url: The url of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this ThreediModel.  # noqa: E501


        :return: The id of this ThreediModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThreediModel.


        :param id: The id of this ThreediModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this ThreediModel.  # noqa: E501

        The username of a user  # noqa: E501

        :return: The user of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ThreediModel.

        The username of a user  # noqa: E501

        :param user: The user of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def inpy_version(self):
        """Gets the inpy_version of this ThreediModel.  # noqa: E501


        :return: The inpy_version of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._inpy_version

    @inpy_version.setter
    def inpy_version(self, inpy_version):
        """Sets the inpy_version of this ThreediModel.


        :param inpy_version: The inpy_version of this ThreediModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inpy_version is None:  # noqa: E501
            raise ValueError("Invalid value for `inpy_version`, must not be `None`")  # noqa: E501

        self._inpy_version = inpy_version

    @property
    def revision(self):
        """Gets the revision of this ThreediModel.  # noqa: E501


        :return: The revision of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this ThreediModel.


        :param revision: The revision of this ThreediModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def revision_id(self):
        """Gets the revision_id of this ThreediModel.  # noqa: E501


        :return: The revision_id of this ThreediModel.  # noqa: E501
        :rtype: int
        """
        return self._revision_id

    @revision_id.setter
    def revision_id(self, revision_id):
        """Sets the revision_id of this ThreediModel.


        :param revision_id: The revision_id of this ThreediModel.  # noqa: E501
        :type: int
        """

        self._revision_id = revision_id

    @property
    def revision_hash(self):
        """Gets the revision_hash of this ThreediModel.  # noqa: E501


        :return: The revision_hash of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._revision_hash

    @revision_hash.setter
    def revision_hash(self, revision_hash):
        """Sets the revision_hash of this ThreediModel.


        :param revision_hash: The revision_hash of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._revision_hash = revision_hash

    @property
    def revision_number(self):
        """Gets the revision_number of this ThreediModel.  # noqa: E501


        :return: The revision_number of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """Sets the revision_number of this ThreediModel.


        :param revision_number: The revision_number of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._revision_number = revision_number

    @property
    def revision_commit_date(self):
        """Gets the revision_commit_date of this ThreediModel.  # noqa: E501


        :return: The revision_commit_date of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._revision_commit_date

    @revision_commit_date.setter
    def revision_commit_date(self, revision_commit_date):
        """Sets the revision_commit_date of this ThreediModel.


        :param revision_commit_date: The revision_commit_date of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._revision_commit_date = revision_commit_date

    @property
    def schematisation_id(self):
        """Gets the schematisation_id of this ThreediModel.  # noqa: E501


        :return: The schematisation_id of this ThreediModel.  # noqa: E501
        :rtype: int
        """
        return self._schematisation_id

    @schematisation_id.setter
    def schematisation_id(self, schematisation_id):
        """Sets the schematisation_id of this ThreediModel.


        :param schematisation_id: The schematisation_id of this ThreediModel.  # noqa: E501
        :type: int
        """

        self._schematisation_id = schematisation_id

    @property
    def schematisation_name(self):
        """Gets the schematisation_name of this ThreediModel.  # noqa: E501


        :return: The schematisation_name of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._schematisation_name

    @schematisation_name.setter
    def schematisation_name(self, schematisation_name):
        """Sets the schematisation_name of this ThreediModel.


        :param schematisation_name: The schematisation_name of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._schematisation_name = schematisation_name

    @property
    def repository_slug(self):
        """Gets the repository_slug of this ThreediModel.  # noqa: E501


        :return: The repository_slug of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._repository_slug

    @repository_slug.setter
    def repository_slug(self, repository_slug):
        """Sets the repository_slug of this ThreediModel.


        :param repository_slug: The repository_slug of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._repository_slug = repository_slug

    @property
    def name(self):
        """Gets the name of this ThreediModel.  # noqa: E501


        :return: The name of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThreediModel.


        :param name: The name of this ThreediModel.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this ThreediModel.  # noqa: E501


        :return: The slug of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this ThreediModel.


        :param slug: The slug of this ThreediModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and slug is None:  # noqa: E501
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and len(slug) > 255):
            raise ValueError("Invalid value for `slug`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and len(slug) < 1):
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug)):  # noqa: E501
            raise ValueError(r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def disabled(self):
        """Gets the disabled of this ThreediModel.  # noqa: E501

        Disable the model.  # noqa: E501

        :return: The disabled of this ThreediModel.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ThreediModel.

        Disable the model.  # noqa: E501

        :param disabled: The disabled of this ThreediModel.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def epsg(self):
        """Gets the epsg of this ThreediModel.  # noqa: E501


        :return: The epsg of this ThreediModel.  # noqa: E501
        :rtype: int
        """
        return self._epsg

    @epsg.setter
    def epsg(self, epsg):
        """Sets the epsg of this ThreediModel.


        :param epsg: The epsg of this ThreediModel.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                epsg is not None and epsg > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `epsg`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                epsg is not None and epsg < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `epsg`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._epsg = epsg

    @property
    def inp_success(self):
        """Gets the inp_success of this ThreediModel.  # noqa: E501

        signals success of generate inp/sewerage_inp/...  # noqa: E501

        :return: The inp_success of this ThreediModel.  # noqa: E501
        :rtype: bool
        """
        return self._inp_success

    @inp_success.setter
    def inp_success(self, inp_success):
        """Sets the inp_success of this ThreediModel.

        signals success of generate inp/sewerage_inp/...  # noqa: E501

        :param inp_success: The inp_success of this ThreediModel.  # noqa: E501
        :type: bool
        """

        self._inp_success = inp_success

    @property
    def description(self):
        """Gets the description of this ThreediModel.  # noqa: E501

        Please describe the model here...  # noqa: E501

        :return: The description of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ThreediModel.

        Please describe the model here...  # noqa: E501

        :param description: The description of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def storage_space(self):
        """Gets the storage_space of this ThreediModel.  # noqa: E501

        Automatically filled after inp generation.  # noqa: E501

        :return: The storage_space of this ThreediModel.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this ThreediModel.

        Automatically filled after inp generation.  # noqa: E501

        :param storage_space: The storage_space of this ThreediModel.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                storage_space is not None and storage_space > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `storage_space`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                storage_space is not None and storage_space < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `storage_space`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._storage_space = storage_space

    @property
    def storage_space_humanized(self):
        """Gets the storage_space_humanized of this ThreediModel.  # noqa: E501


        :return: The storage_space_humanized of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._storage_space_humanized

    @storage_space_humanized.setter
    def storage_space_humanized(self, storage_space_humanized):
        """Sets the storage_space_humanized of this ThreediModel.


        :param storage_space_humanized: The storage_space_humanized of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._storage_space_humanized = storage_space_humanized

    @property
    def model_ini(self):
        """Gets the model_ini of this ThreediModel.  # noqa: E501


        :return: The model_ini of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._model_ini

    @model_ini.setter
    def model_ini(self, model_ini):
        """Sets the model_ini of this ThreediModel.


        :param model_ini: The model_ini of this ThreediModel.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model_ini is not None and len(model_ini) > 512):
            raise ValueError("Invalid value for `model_ini`, length must be less than or equal to `512`")  # noqa: E501

        self._model_ini = model_ini

    @property
    def breach_count(self):
        """Gets the breach_count of this ThreediModel.  # noqa: E501


        :return: The breach_count of this ThreediModel.  # noqa: E501
        :rtype: str
        """
        return self._breach_count

    @breach_count.setter
    def breach_count(self, breach_count):
        """Sets the breach_count of this ThreediModel.


        :param breach_count: The breach_count of this ThreediModel.  # noqa: E501
        :type: str
        """

        self._breach_count = breach_count

    @property
    def extent_two_d(self):
        """Gets the extent_two_d of this ThreediModel.  # noqa: E501


        :return: The extent_two_d of this ThreediModel.  # noqa: E501
        :rtype: Extent
        """
        return self._extent_two_d

    @extent_two_d.setter
    def extent_two_d(self, extent_two_d):
        """Sets the extent_two_d of this ThreediModel.


        :param extent_two_d: The extent_two_d of this ThreediModel.  # noqa: E501
        :type: Extent
        """

        self._extent_two_d = extent_two_d

    @property
    def extent_one_d(self):
        """Gets the extent_one_d of this ThreediModel.  # noqa: E501


        :return: The extent_one_d of this ThreediModel.  # noqa: E501
        :rtype: Extent
        """
        return self._extent_one_d

    @extent_one_d.setter
    def extent_one_d(self, extent_one_d):
        """Sets the extent_one_d of this ThreediModel.


        :param extent_one_d: The extent_one_d of this ThreediModel.  # noqa: E501
        :type: Extent
        """

        self._extent_one_d = extent_one_d

    @property
    def extent_zero_d(self):
        """Gets the extent_zero_d of this ThreediModel.  # noqa: E501


        :return: The extent_zero_d of this ThreediModel.  # noqa: E501
        :rtype: Extent
        """
        return self._extent_zero_d

    @extent_zero_d.setter
    def extent_zero_d(self, extent_zero_d):
        """Sets the extent_zero_d of this ThreediModel.


        :param extent_zero_d: The extent_zero_d of this ThreediModel.  # noqa: E501
        :type: Extent
        """

        self._extent_zero_d = extent_zero_d

    @property
    def nodes_count(self):
        """Gets the nodes_count of this ThreediModel.  # noqa: E501


        :return: The nodes_count of this ThreediModel.  # noqa: E501
        :rtype: int
        """
        return self._nodes_count

    @nodes_count.setter
    def nodes_count(self, nodes_count):
        """Sets the nodes_count of this ThreediModel.


        :param nodes_count: The nodes_count of this ThreediModel.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                nodes_count is not None and nodes_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `nodes_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                nodes_count is not None and nodes_count < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `nodes_count`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._nodes_count = nodes_count

    @property
    def lines_count(self):
        """Gets the lines_count of this ThreediModel.  # noqa: E501


        :return: The lines_count of this ThreediModel.  # noqa: E501
        :rtype: int
        """
        return self._lines_count

    @lines_count.setter
    def lines_count(self, lines_count):
        """Sets the lines_count of this ThreediModel.


        :param lines_count: The lines_count of this ThreediModel.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                lines_count is not None and lines_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `lines_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lines_count is not None and lines_count < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `lines_count`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._lines_count = lines_count

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
        if not isinstance(other, ThreediModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThreediModel):
            return True

        return self.to_dict() != other.to_dict()
