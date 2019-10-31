# coding: utf-8

"""
    3Di API

    3Di simulation API   Framework release: 0.0.17   3Di core release: 2.0.2  deployed on:  10:18AM (UTC) on October 30, 2019  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PotentialBreach(object):
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
        'connected_pnt_id': 'int',
        'threedimodel': 'str'
    }

    attribute_map = {
        'url': 'url',
        'connected_pnt_id': 'connected_pnt_id',
        'threedimodel': 'threedimodel'
    }

    def __init__(self, url=None, connected_pnt_id=None, threedimodel=None):  # noqa: E501
        """PotentialBreach - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._connected_pnt_id = None
        self._threedimodel = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.connected_pnt_id = connected_pnt_id
        if threedimodel is not None:
            self.threedimodel = threedimodel

    @property
    def url(self):
        """Gets the url of this PotentialBreach.  # noqa: E501


        :return: The url of this PotentialBreach.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PotentialBreach.


        :param url: The url of this PotentialBreach.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def connected_pnt_id(self):
        """Gets the connected_pnt_id of this PotentialBreach.  # noqa: E501


        :return: The connected_pnt_id of this PotentialBreach.  # noqa: E501
        :rtype: int
        """
        return self._connected_pnt_id

    @connected_pnt_id.setter
    def connected_pnt_id(self, connected_pnt_id):
        """Sets the connected_pnt_id of this PotentialBreach.


        :param connected_pnt_id: The connected_pnt_id of this PotentialBreach.  # noqa: E501
        :type: int
        """
        if connected_pnt_id is None:
            raise ValueError("Invalid value for `connected_pnt_id`, must not be `None`")  # noqa: E501
        if connected_pnt_id is not None and connected_pnt_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `connected_pnt_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if connected_pnt_id is not None and connected_pnt_id < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `connected_pnt_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._connected_pnt_id = connected_pnt_id

    @property
    def threedimodel(self):
        """Gets the threedimodel of this PotentialBreach.  # noqa: E501


        :return: The threedimodel of this PotentialBreach.  # noqa: E501
        :rtype: str
        """
        return self._threedimodel

    @threedimodel.setter
    def threedimodel(self, threedimodel):
        """Sets the threedimodel of this PotentialBreach.


        :param threedimodel: The threedimodel of this PotentialBreach.  # noqa: E501
        :type: str
        """

        self._threedimodel = threedimodel

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
        if not isinstance(other, PotentialBreach):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
