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


class ResultFile(object):
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
        'filename': 'str',
        'description': 'str',
        'created': 'datetime',
        'file': 'FileReadOnly',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'filename': 'filename',
        'description': 'description',
        'created': 'created',
        'file': 'file',
        'id': 'id'
    }

    def __init__(self, url=None, simulation=None, filename=None, description=None, created=None, file=None, id=None):  # noqa: E501
        """ResultFile - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._simulation = None
        self._filename = None
        self._description = None
        self._created = None
        self._file = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.filename = filename
        self.description = description
        self.created = created
        if file is not None:
            self.file = file
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this ResultFile.  # noqa: E501


        :return: The url of this ResultFile.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ResultFile.


        :param url: The url of this ResultFile.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this ResultFile.  # noqa: E501


        :return: The simulation of this ResultFile.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this ResultFile.


        :param simulation: The simulation of this ResultFile.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def filename(self):
        """Gets the filename of this ResultFile.  # noqa: E501


        :return: The filename of this ResultFile.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ResultFile.


        :param filename: The filename of this ResultFile.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501
        if filename is not None and len(filename) > 255:
            raise ValueError("Invalid value for `filename`, length must be less than or equal to `255`")  # noqa: E501
        if filename is not None and len(filename) < 1:
            raise ValueError("Invalid value for `filename`, length must be greater than or equal to `1`")  # noqa: E501

        self._filename = filename

    @property
    def description(self):
        """Gets the description of this ResultFile.  # noqa: E501


        :return: The description of this ResultFile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResultFile.


        :param description: The description of this ResultFile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created(self):
        """Gets the created of this ResultFile.  # noqa: E501


        :return: The created of this ResultFile.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ResultFile.


        :param created: The created of this ResultFile.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def file(self):
        """Gets the file of this ResultFile.  # noqa: E501


        :return: The file of this ResultFile.  # noqa: E501
        :rtype: FileReadOnly
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ResultFile.


        :param file: The file of this ResultFile.  # noqa: E501
        :type: FileReadOnly
        """

        self._file = file

    @property
    def id(self):
        """Gets the id of this ResultFile.  # noqa: E501


        :return: The id of this ResultFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResultFile.


        :param id: The id of this ResultFile.  # noqa: E501
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

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResultFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
