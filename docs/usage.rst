Threedi Api
===========

The ``threedi_api_client.ThreediApi`` is the main entry point to make calls
to the 3Di API. It handles the login process for you and can be
directly used as client for all API endpoints.

In earlier ``threedi_api_client`` versions, the main entry point was
``threedi_api_client.ThreediApiClient``. This will remain available until
``threedi_api_client`` version 4. Read below how to migrate to the new usage.


ThreediApi
----------

.. autoclass:: threedi_api_client.ThreediApi

    
Migration from ThreediApiClient
-------------------------------

.. automodule:: threedi_api_client.aio.files
    :members: download_file, upload_file
