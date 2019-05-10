======================
threedi-openapi-client
======================


.. image:: https://img.shields.io/pypi/v/threedi_openapi_client.svg
        :target: https://pypi.python.org/pypi/threedi_openapi_client

.. image:: https://img.shields.io/travis/larsclaussen/threedi_openapi_client.svg
        :target: https://travis-ci.org/larsclaussen/threedi_openapi_client

.. image:: https://readthedocs.org/projects/threedi-openapi-client/badge/?version=latest
        :target: https://threedi-openapi-client.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/larsclaussen/threedi_openapi_client/shield.svg
     :target: https://pyup.io/repos/github/larsclaussen/threedi_openapi_client/
     :alt: Updates



* A Python library for the 3DI API 


* Free software: BSD license
* Documentation: https://threedi-openapi-client.readthedocs.io.


Features
--------

* OOP API interaction
* async support
* ...


Getting started
---------------

get your auth tokens::

        from openapi_client import ApiClient
        from openapi_client import Configuration
        from openapi_client import AuthApi
        from openapi_client.models import TokenObtainPair

        configuration = Configuration()
        api_client = ApiClient(configuration)
        auth = AuthApi(api_client)
        tokens = auth.auth_token_create(
            TokenObtainPair(username, password)
        )

        configuration.api_key['Authorization'] = tokens.access
        configuration.api_key_prefix['Authorization'] = 'Bearer'
        # new client instance with auth headers 
        client = ApiClient(configuration)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
