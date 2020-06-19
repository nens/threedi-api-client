# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.7   3Di core release: 2.0.9  deployed on:  02:04PM (UTC) on June 16, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class PermissionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def permissions_create(self, data, **kwargs):  # noqa: E501
        """create a role for an existing user in an existing organisation  # noqa: E501

        Example payload:      {       \"user\": \"chuck.norris\",  # user name       \"role\": \"follow_simulation\",  # role name       \"organisation\": \"48dac75bef8a42ebbb52e8f89bbdb9f2\"  # unique id     }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permissions_create(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param OrganisationRole data: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: OrganisationRole
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.permissions_create_with_http_info(data, **kwargs)  # noqa: E501

    def permissions_create_with_http_info(self, data, **kwargs):  # noqa: E501
        """create a role for an existing user in an existing organisation  # noqa: E501

        Example payload:      {       \"user\": \"chuck.norris\",  # user name       \"role\": \"follow_simulation\",  # role name       \"organisation\": \"48dac75bef8a42ebbb52e8f89bbdb9f2\"  # unique id     }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permissions_create_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param OrganisationRole data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(OrganisationRole, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method permissions_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in local_var_params or
                local_var_params['data'] is None):
            raise ApiValueError("Missing the required parameter `data` when calling `permissions_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/permissions/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrganisationRole',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def permissions_delete(self, id, **kwargs):  # noqa: E501
        """permissions_delete  # noqa: E501

        Permissions management endpoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permissions_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this user organisation role. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.permissions_delete_with_http_info(id, **kwargs)  # noqa: E501

    def permissions_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """permissions_delete  # noqa: E501

        Permissions management endpoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permissions_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this user organisation role. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method permissions_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `permissions_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/permissions/{id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def permissions_list(self, **kwargs):  # noqa: E501
        """permissions_list  # noqa: E501

        Permissions management endpoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permissions_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user__username:
        :param str user__username__contains:
        :param str user__username__icontains:
        :param str user__username__in: Multiple values may be separated by commas.
        :param str user__username__startswith:
        :param str user__username__istartswith:
        :param str user__username__endswith:
        :param str user__username__regex:
        :param str role__name:
        :param str role__name__contains:
        :param str role__name__icontains:
        :param str role__name__in: Multiple values may be separated by commas.
        :param str role__name__startswith:
        :param str role__name__istartswith:
        :param str role__name__endswith:
        :param str role__name__regex:
        :param str organisation__name:
        :param str organisation__name__contains:
        :param str organisation__name__icontains:
        :param str organisation__name__in: Multiple values may be separated by commas.
        :param str organisation__name__startswith:
        :param str organisation__name__istartswith:
        :param str organisation__name__endswith:
        :param str organisation__name__regex:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.permissions_list_with_http_info(**kwargs)  # noqa: E501

    def permissions_list_with_http_info(self, **kwargs):  # noqa: E501
        """permissions_list  # noqa: E501

        Permissions management endpoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permissions_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user__username:
        :param str user__username__contains:
        :param str user__username__icontains:
        :param str user__username__in: Multiple values may be separated by commas.
        :param str user__username__startswith:
        :param str user__username__istartswith:
        :param str user__username__endswith:
        :param str user__username__regex:
        :param str role__name:
        :param str role__name__contains:
        :param str role__name__icontains:
        :param str role__name__in: Multiple values may be separated by commas.
        :param str role__name__startswith:
        :param str role__name__istartswith:
        :param str role__name__endswith:
        :param str role__name__regex:
        :param str organisation__name:
        :param str organisation__name__contains:
        :param str organisation__name__icontains:
        :param str organisation__name__in: Multiple values may be separated by commas.
        :param str organisation__name__startswith:
        :param str organisation__name__istartswith:
        :param str organisation__name__endswith:
        :param str organisation__name__regex:
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
        :return: tuple(InlineResponse2005, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user__username', 'user__username__contains', 'user__username__icontains', 'user__username__in', 'user__username__startswith', 'user__username__istartswith', 'user__username__endswith', 'user__username__regex', 'role__name', 'role__name__contains', 'role__name__icontains', 'role__name__in', 'role__name__startswith', 'role__name__istartswith', 'role__name__endswith', 'role__name__regex', 'organisation__name', 'organisation__name__contains', 'organisation__name__icontains', 'organisation__name__in', 'organisation__name__startswith', 'organisation__name__istartswith', 'organisation__name__endswith', 'organisation__name__regex', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method permissions_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user__username' in local_var_params:
            query_params.append(('user__username', local_var_params['user__username']))  # noqa: E501
        if 'user__username__contains' in local_var_params:
            query_params.append(('user__username__contains', local_var_params['user__username__contains']))  # noqa: E501
        if 'user__username__icontains' in local_var_params:
            query_params.append(('user__username__icontains', local_var_params['user__username__icontains']))  # noqa: E501
        if 'user__username__in' in local_var_params:
            query_params.append(('user__username__in', local_var_params['user__username__in']))  # noqa: E501
        if 'user__username__startswith' in local_var_params:
            query_params.append(('user__username__startswith', local_var_params['user__username__startswith']))  # noqa: E501
        if 'user__username__istartswith' in local_var_params:
            query_params.append(('user__username__istartswith', local_var_params['user__username__istartswith']))  # noqa: E501
        if 'user__username__endswith' in local_var_params:
            query_params.append(('user__username__endswith', local_var_params['user__username__endswith']))  # noqa: E501
        if 'user__username__regex' in local_var_params:
            query_params.append(('user__username__regex', local_var_params['user__username__regex']))  # noqa: E501
        if 'role__name' in local_var_params:
            query_params.append(('role__name', local_var_params['role__name']))  # noqa: E501
        if 'role__name__contains' in local_var_params:
            query_params.append(('role__name__contains', local_var_params['role__name__contains']))  # noqa: E501
        if 'role__name__icontains' in local_var_params:
            query_params.append(('role__name__icontains', local_var_params['role__name__icontains']))  # noqa: E501
        if 'role__name__in' in local_var_params:
            query_params.append(('role__name__in', local_var_params['role__name__in']))  # noqa: E501
        if 'role__name__startswith' in local_var_params:
            query_params.append(('role__name__startswith', local_var_params['role__name__startswith']))  # noqa: E501
        if 'role__name__istartswith' in local_var_params:
            query_params.append(('role__name__istartswith', local_var_params['role__name__istartswith']))  # noqa: E501
        if 'role__name__endswith' in local_var_params:
            query_params.append(('role__name__endswith', local_var_params['role__name__endswith']))  # noqa: E501
        if 'role__name__regex' in local_var_params:
            query_params.append(('role__name__regex', local_var_params['role__name__regex']))  # noqa: E501
        if 'organisation__name' in local_var_params:
            query_params.append(('organisation__name', local_var_params['organisation__name']))  # noqa: E501
        if 'organisation__name__contains' in local_var_params:
            query_params.append(('organisation__name__contains', local_var_params['organisation__name__contains']))  # noqa: E501
        if 'organisation__name__icontains' in local_var_params:
            query_params.append(('organisation__name__icontains', local_var_params['organisation__name__icontains']))  # noqa: E501
        if 'organisation__name__in' in local_var_params:
            query_params.append(('organisation__name__in', local_var_params['organisation__name__in']))  # noqa: E501
        if 'organisation__name__startswith' in local_var_params:
            query_params.append(('organisation__name__startswith', local_var_params['organisation__name__startswith']))  # noqa: E501
        if 'organisation__name__istartswith' in local_var_params:
            query_params.append(('organisation__name__istartswith', local_var_params['organisation__name__istartswith']))  # noqa: E501
        if 'organisation__name__endswith' in local_var_params:
            query_params.append(('organisation__name__endswith', local_var_params['organisation__name__endswith']))  # noqa: E501
        if 'organisation__name__regex' in local_var_params:
            query_params.append(('organisation__name__regex', local_var_params['organisation__name__regex']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/permissions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def permissions_read(self, id, **kwargs):  # noqa: E501
        """permissions_read  # noqa: E501

        Permissions management endpoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permissions_read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this user organisation role. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: OrganisationRole
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.permissions_read_with_http_info(id, **kwargs)  # noqa: E501

    def permissions_read_with_http_info(self, id, **kwargs):  # noqa: E501
        """permissions_read  # noqa: E501

        Permissions management endpoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.permissions_read_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this user organisation role. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(OrganisationRole, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method permissions_read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `permissions_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/permissions/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrganisationRole',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
