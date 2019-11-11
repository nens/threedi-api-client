# coding: utf-8

"""
    3Di API

    3Di simulation API   Framework release: 0.0.19   3Di core release: 2.0.2  deployed on:  03:09PM (UTC) on November 07, 2019  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class InpyVersionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def inpy_versions_create(self, data, **kwargs):  # noqa: E501
        """inpy_versions_create  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_create(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InpyVersion data: (required)
        :return: InpyVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.inpy_versions_create_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.inpy_versions_create_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def inpy_versions_create_with_http_info(self, data, **kwargs):  # noqa: E501
        """inpy_versions_create  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_create_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InpyVersion data: (required)
        :return: InpyVersion
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inpy_versions_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in local_var_params or
                local_var_params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `inpy_versions_create`")  # noqa: E501

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
            '/inpy-versions/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InpyVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inpy_versions_delete(self, id, **kwargs):  # noqa: E501
        """inpy_versions_delete  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this inpy version. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.inpy_versions_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.inpy_versions_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def inpy_versions_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """inpy_versions_delete  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this inpy version. (required)
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inpy_versions_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `inpy_versions_delete`")  # noqa: E501

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
            '/inpy-versions/{id}/', 'DELETE',
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

    def inpy_versions_list(self, **kwargs):  # noqa: E501
        """inpy_versions_list  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str threedi_version:
        :param str threedi_version__contains:
        :param str threedi_version__in: Multiple values may be separated by commas.
        :param str threedi_version__startswith:
        :param str threedi_version__istartswith:
        :param str threedi_version__endswith:
        :param str threedi_version__regex:
        :param str threedicore_version:
        :param str threedicore_version__contains:
        :param str threedicore_version__in: Multiple values may be separated by commas.
        :param str threedicore_version__startswith:
        :param str threedicore_version__istartswith:
        :param str threedicore_version__endswith:
        :param str threedicore_version__regex:
        :param str slug:
        :param str slug__contains:
        :param str slug__in: Multiple values may be separated by commas.
        :param str slug__startswith:
        :param str slug__istartswith:
        :param str slug__endswith:
        :param str slug__regex:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.inpy_versions_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.inpy_versions_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def inpy_versions_list_with_http_info(self, **kwargs):  # noqa: E501
        """inpy_versions_list  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str threedi_version:
        :param str threedi_version__contains:
        :param str threedi_version__in: Multiple values may be separated by commas.
        :param str threedi_version__startswith:
        :param str threedi_version__istartswith:
        :param str threedi_version__endswith:
        :param str threedi_version__regex:
        :param str threedicore_version:
        :param str threedicore_version__contains:
        :param str threedicore_version__in: Multiple values may be separated by commas.
        :param str threedicore_version__startswith:
        :param str threedicore_version__istartswith:
        :param str threedicore_version__endswith:
        :param str threedicore_version__regex:
        :param str slug:
        :param str slug__contains:
        :param str slug__in: Multiple values may be separated by commas.
        :param str slug__startswith:
        :param str slug__istartswith:
        :param str slug__endswith:
        :param str slug__regex:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['threedi_version', 'threedi_version__contains', 'threedi_version__in', 'threedi_version__startswith', 'threedi_version__istartswith', 'threedi_version__endswith', 'threedi_version__regex', 'threedicore_version', 'threedicore_version__contains', 'threedicore_version__in', 'threedicore_version__startswith', 'threedicore_version__istartswith', 'threedicore_version__endswith', 'threedicore_version__regex', 'slug', 'slug__contains', 'slug__in', 'slug__startswith', 'slug__istartswith', 'slug__endswith', 'slug__regex', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inpy_versions_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'threedi_version' in local_var_params:
            query_params.append(('threedi_version', local_var_params['threedi_version']))  # noqa: E501
        if 'threedi_version__contains' in local_var_params:
            query_params.append(('threedi_version__contains', local_var_params['threedi_version__contains']))  # noqa: E501
        if 'threedi_version__in' in local_var_params:
            query_params.append(('threedi_version__in', local_var_params['threedi_version__in']))  # noqa: E501
        if 'threedi_version__startswith' in local_var_params:
            query_params.append(('threedi_version__startswith', local_var_params['threedi_version__startswith']))  # noqa: E501
        if 'threedi_version__istartswith' in local_var_params:
            query_params.append(('threedi_version__istartswith', local_var_params['threedi_version__istartswith']))  # noqa: E501
        if 'threedi_version__endswith' in local_var_params:
            query_params.append(('threedi_version__endswith', local_var_params['threedi_version__endswith']))  # noqa: E501
        if 'threedi_version__regex' in local_var_params:
            query_params.append(('threedi_version__regex', local_var_params['threedi_version__regex']))  # noqa: E501
        if 'threedicore_version' in local_var_params:
            query_params.append(('threedicore_version', local_var_params['threedicore_version']))  # noqa: E501
        if 'threedicore_version__contains' in local_var_params:
            query_params.append(('threedicore_version__contains', local_var_params['threedicore_version__contains']))  # noqa: E501
        if 'threedicore_version__in' in local_var_params:
            query_params.append(('threedicore_version__in', local_var_params['threedicore_version__in']))  # noqa: E501
        if 'threedicore_version__startswith' in local_var_params:
            query_params.append(('threedicore_version__startswith', local_var_params['threedicore_version__startswith']))  # noqa: E501
        if 'threedicore_version__istartswith' in local_var_params:
            query_params.append(('threedicore_version__istartswith', local_var_params['threedicore_version__istartswith']))  # noqa: E501
        if 'threedicore_version__endswith' in local_var_params:
            query_params.append(('threedicore_version__endswith', local_var_params['threedicore_version__endswith']))  # noqa: E501
        if 'threedicore_version__regex' in local_var_params:
            query_params.append(('threedicore_version__regex', local_var_params['threedicore_version__regex']))  # noqa: E501
        if 'slug' in local_var_params:
            query_params.append(('slug', local_var_params['slug']))  # noqa: E501
        if 'slug__contains' in local_var_params:
            query_params.append(('slug__contains', local_var_params['slug__contains']))  # noqa: E501
        if 'slug__in' in local_var_params:
            query_params.append(('slug__in', local_var_params['slug__in']))  # noqa: E501
        if 'slug__startswith' in local_var_params:
            query_params.append(('slug__startswith', local_var_params['slug__startswith']))  # noqa: E501
        if 'slug__istartswith' in local_var_params:
            query_params.append(('slug__istartswith', local_var_params['slug__istartswith']))  # noqa: E501
        if 'slug__endswith' in local_var_params:
            query_params.append(('slug__endswith', local_var_params['slug__endswith']))  # noqa: E501
        if 'slug__regex' in local_var_params:
            query_params.append(('slug__regex', local_var_params['slug__regex']))  # noqa: E501
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
            '/inpy-versions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inpy_versions_partial_update(self, id, data, **kwargs):  # noqa: E501
        """inpy_versions_partial_update  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_partial_update(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this inpy version. (required)
        :param InpyVersion data: (required)
        :return: InpyVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.inpy_versions_partial_update_with_http_info(id, data, **kwargs)  # noqa: E501
        else:
            (data) = self.inpy_versions_partial_update_with_http_info(id, data, **kwargs)  # noqa: E501
            return data

    def inpy_versions_partial_update_with_http_info(self, id, data, **kwargs):  # noqa: E501
        """inpy_versions_partial_update  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_partial_update_with_http_info(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this inpy version. (required)
        :param InpyVersion data: (required)
        :return: InpyVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inpy_versions_partial_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `inpy_versions_partial_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in local_var_params or
                local_var_params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `inpy_versions_partial_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

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
            '/inpy-versions/{id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InpyVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inpy_versions_read(self, id, **kwargs):  # noqa: E501
        """inpy_versions_read  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this inpy version. (required)
        :return: InpyVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.inpy_versions_read_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.inpy_versions_read_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def inpy_versions_read_with_http_info(self, id, **kwargs):  # noqa: E501
        """inpy_versions_read  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_read_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this inpy version. (required)
        :return: InpyVersion
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inpy_versions_read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `inpy_versions_read`")  # noqa: E501

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
            '/inpy-versions/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InpyVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inpy_versions_update(self, id, data, **kwargs):  # noqa: E501
        """inpy_versions_update  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_update(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this inpy version. (required)
        :param InpyVersion data: (required)
        :return: InpyVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.inpy_versions_update_with_http_info(id, data, **kwargs)  # noqa: E501
        else:
            (data) = self.inpy_versions_update_with_http_info(id, data, **kwargs)  # noqa: E501
            return data

    def inpy_versions_update_with_http_info(self, id, data, **kwargs):  # noqa: E501
        """inpy_versions_update  # noqa: E501

        Inpy is the service for preparing models to become usable by the Threedi calculation core. Updates in Inpy often result in updates in the calculation core.  This resource keeps track of updates to the Inpy service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.inpy_versions_update_with_http_info(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this inpy version. (required)
        :param InpyVersion data: (required)
        :return: InpyVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inpy_versions_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `inpy_versions_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in local_var_params or
                local_var_params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `inpy_versions_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

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
            '/inpy-versions/{id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InpyVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
