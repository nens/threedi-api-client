# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.16   3Di core release: 2.0.11  deployed on:  07:33AM (UTC) on September 04, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class OrganisationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def organisations_list(self, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name:
        :param str name__contains:
        :param str name__icontains:
        :param str name__in: Multiple values may be separated by commas.
        :param str name__startswith:
        :param str name__istartswith:
        :param str name__endswith:
        :param str name__regex:
        :param str unique_id:
        :param str unique_id__contains:
        :param str unique_id__icontains:
        :param str unique_id__in: Multiple values may be separated by commas.
        :param str unique_id__startswith:
        :param str unique_id__istartswith:
        :param str unique_id__endswith:
        :param str unique_id__regex:
        :param str valid_contracts_only:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.organisations_list_with_http_info(**kwargs)  # noqa: E501

    def organisations_list_with_http_info(self, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name:
        :param str name__contains:
        :param str name__icontains:
        :param str name__in: Multiple values may be separated by commas.
        :param str name__startswith:
        :param str name__istartswith:
        :param str name__endswith:
        :param str name__regex:
        :param str unique_id:
        :param str unique_id__contains:
        :param str unique_id__icontains:
        :param str unique_id__in: Multiple values may be separated by commas.
        :param str unique_id__startswith:
        :param str unique_id__istartswith:
        :param str unique_id__endswith:
        :param str unique_id__regex:
        :param str valid_contracts_only:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2004, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "name",
            "name__contains",
            "name__icontains",
            "name__in",
            "name__startswith",
            "name__istartswith",
            "name__endswith",
            "name__regex",
            "unique_id",
            "unique_id__contains",
            "unique_id__icontains",
            "unique_id__in",
            "unique_id__startswith",
            "unique_id__istartswith",
            "unique_id__endswith",
            "unique_id__regex",
            "valid_contracts_only",
            "limit",
            "offset",
        ]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organisations_list" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if (
            "name" in local_var_params and local_var_params["name"] is not None
        ):  # noqa: E501
            query_params.append(("name", local_var_params["name"]))  # noqa: E501
        if (
            "name__contains" in local_var_params
            and local_var_params["name__contains"] is not None
        ):  # noqa: E501
            query_params.append(
                ("name__contains", local_var_params["name__contains"])
            )  # noqa: E501
        if (
            "name__icontains" in local_var_params
            and local_var_params["name__icontains"] is not None
        ):  # noqa: E501
            query_params.append(
                ("name__icontains", local_var_params["name__icontains"])
            )  # noqa: E501
        if (
            "name__in" in local_var_params and local_var_params["name__in"] is not None
        ):  # noqa: E501
            query_params.append(
                ("name__in", local_var_params["name__in"])
            )  # noqa: E501
        if (
            "name__startswith" in local_var_params
            and local_var_params["name__startswith"] is not None
        ):  # noqa: E501
            query_params.append(
                ("name__startswith", local_var_params["name__startswith"])
            )  # noqa: E501
        if (
            "name__istartswith" in local_var_params
            and local_var_params["name__istartswith"] is not None
        ):  # noqa: E501
            query_params.append(
                ("name__istartswith", local_var_params["name__istartswith"])
            )  # noqa: E501
        if (
            "name__endswith" in local_var_params
            and local_var_params["name__endswith"] is not None
        ):  # noqa: E501
            query_params.append(
                ("name__endswith", local_var_params["name__endswith"])
            )  # noqa: E501
        if (
            "name__regex" in local_var_params
            and local_var_params["name__regex"] is not None
        ):  # noqa: E501
            query_params.append(
                ("name__regex", local_var_params["name__regex"])
            )  # noqa: E501
        if (
            "unique_id" in local_var_params
            and local_var_params["unique_id"] is not None
        ):  # noqa: E501
            query_params.append(
                ("unique_id", local_var_params["unique_id"])
            )  # noqa: E501
        if (
            "unique_id__contains" in local_var_params
            and local_var_params["unique_id__contains"] is not None
        ):  # noqa: E501
            query_params.append(
                ("unique_id__contains", local_var_params["unique_id__contains"])
            )  # noqa: E501
        if (
            "unique_id__icontains" in local_var_params
            and local_var_params["unique_id__icontains"] is not None
        ):  # noqa: E501
            query_params.append(
                ("unique_id__icontains", local_var_params["unique_id__icontains"])
            )  # noqa: E501
        if (
            "unique_id__in" in local_var_params
            and local_var_params["unique_id__in"] is not None
        ):  # noqa: E501
            query_params.append(
                ("unique_id__in", local_var_params["unique_id__in"])
            )  # noqa: E501
        if (
            "unique_id__startswith" in local_var_params
            and local_var_params["unique_id__startswith"] is not None
        ):  # noqa: E501
            query_params.append(
                ("unique_id__startswith", local_var_params["unique_id__startswith"])
            )  # noqa: E501
        if (
            "unique_id__istartswith" in local_var_params
            and local_var_params["unique_id__istartswith"] is not None
        ):  # noqa: E501
            query_params.append(
                ("unique_id__istartswith", local_var_params["unique_id__istartswith"])
            )  # noqa: E501
        if (
            "unique_id__endswith" in local_var_params
            and local_var_params["unique_id__endswith"] is not None
        ):  # noqa: E501
            query_params.append(
                ("unique_id__endswith", local_var_params["unique_id__endswith"])
            )  # noqa: E501
        if (
            "unique_id__regex" in local_var_params
            and local_var_params["unique_id__regex"] is not None
        ):  # noqa: E501
            query_params.append(
                ("unique_id__regex", local_var_params["unique_id__regex"])
            )  # noqa: E501
        if (
            "valid_contracts_only" in local_var_params
            and local_var_params["valid_contracts_only"] is not None
        ):  # noqa: E501
            query_params.append(
                ("valid_contracts_only", local_var_params["valid_contracts_only"])
            )  # noqa: E501
        if (
            "limit" in local_var_params and local_var_params["limit"] is not None
        ):  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if (
            "offset" in local_var_params and local_var_params["offset"] is not None
        ):  # noqa: E501
            query_params.append(("offset", local_var_params["offset"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/organisations/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2004",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def organisations_permissions(self, unique_id, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_permissions(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str unique_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[OrganisationRole]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.organisations_permissions_with_http_info(
            unique_id, **kwargs
        )  # noqa: E501

    def organisations_permissions_with_http_info(
        self, unique_id, **kwargs
    ):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_permissions_with_http_info(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str unique_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[OrganisationRole], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["unique_id"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organisations_permissions" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'unique_id' is set
        if self.api_client.client_side_validation and (
            "unique_id" not in local_var_params
            or local_var_params["unique_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `unique_id` when calling `organisations_permissions`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "unique_id" in local_var_params:
            path_params["unique_id"] = local_var_params["unique_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/organisations/{unique_id}/permissions/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[OrganisationRole]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def organisations_read(self, unique_id, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_read(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str unique_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Organisation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.organisations_read_with_http_info(unique_id, **kwargs)  # noqa: E501

    def organisations_read_with_http_info(self, unique_id, **kwargs):  # noqa: E501
        """Read-only API endpoint for interacting with organisations.  # noqa: E501

        ##Authorization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.organisations_read_with_http_info(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str unique_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Organisation, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["unique_id"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organisations_read" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'unique_id' is set
        if self.api_client.client_side_validation and (
            "unique_id" not in local_var_params
            or local_var_params["unique_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `unique_id` when calling `organisations_read`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "unique_id" in local_var_params:
            path_params["unique_id"] = local_var_params["unique_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/organisations/{unique_id}/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Organisation",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
