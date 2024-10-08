=======
History
=======

4.1.9 (unreleased)
------------------

- Pin aiohttp to <3.10
- Add test workflow for Python 3.12 and 3.13


4.1.8 (2024-10-03)
------------------

- Release 3.4.3
- Customized result files
- Diffusion coefficient for water quality


4.1.7 (2024-06-05)
------------------

- started from field for simulation


4.1.6 (2024-04-12)
------------------

- Generated with generator version v4.4.0


4.1.6b (2023-12-14)
-------------------

- Water quality and other additions.


4.1.5 (2023-11-21)
------------------

- Update to framework release 3.2.75


4.1.4 (2023-06-19)
------------------

- Allow passing (extra) HTTP headers via `file_upload` function.


4.1.3 (2023-06-14)
------------------

- Release 3.2.34
- Build the release with the build package instead of setuptools.
- Rewrite release workflow to use a supported github action for github release.


4.1.2 (2023-04-25)
------------------

- Public release.


4.1.2b (2023-03-13)
-------------------

- Updated to framework release 3.2.6

- Fix timeout when retrying uploads.


4.1.1 (2022-11-21)
------------------

- Also improve support for HTTP proxies for async upload/download functionality.


4.1.0 (2022-11-21)
------------------

- Support S3 (object storage) temp-urls in upload/download functions in aio/files.py by
  disabling the automatic addition of the 'content-type' header by aiohttp.

- Increase default socket read timeout for (async) downloads to 60 seconds.

- Increase default socket connect timeout for uploads to 30 seconds.

- Make the sync and async ApiException the same.

- Improved support for HTTP proxies with async API client.

- Support the November 2022 API (3.0) release.


4.0.1 (2022-06-08)
------------------

- Support personal api tokens authentication.

- Added OAuth2 token and OAuth2 token refresh capability (for both public
  and private clients).

- Make server-side MD5 check optional to account for the fact that S3 presigned
  urls cannot be used with custom headers (like Content-MD5) unless they are included
  in the signing procedure.

- Allow usage of the API client without supplying a refresh token.

- Added automatic refresh for OAuth2 tokens obtained through the client credentials grant.


4.0.0 (2022-02-11)
------------------

- First stable release with new `ThreediApi` client included

- Show warning when data fetched from API cannot be succesfully valided by the client-side validation.


4.0.0b4 (2022-01-26)
--------------------

- Renamed `simulation_templates` to `simulation-templates`


4.0.0b3 (2022-01-26)
--------------------

- Added Threedimodel `is_valid` field as alias for `inp_success`

- Added Simulation `threedicore_version` field and `cloned_from` field

- Added `status` endpoints and `version` endpoints


4.0.0b2 (2022-01-17)
--------------------

- Fix distribution.


4.0.0b1 (2022-01-17)
--------------------

- Added support for `periodic` (`daily` only for now) lateral file

- Support for 1D initial waterlevels from file.

- Show warnings in cases of unknown enum values instead of raising errors.

- Added callback support for async/sync download/upload functions

- Added structure controls file upload

- Added support for `THREEDI_API_ACCESS_TOKEN` and `THREEDI_API_REFRESH_TOKEN` configuration variables

- Added a new, versioned, API in threedi_api_client.openapi / threedi_api_client.api.openapi.
  A warning will be emitted if the old one is used (openapi_client).

- The API version should now be omitted from the API_HOST setting (e.g.
  https://api.3di.live instead of https://api.3di.live/v3.0). A warning will be emitted if
  a version is included.

- Make V3AlphaApi a subclass of V3BetaApi, and V3BetaApi a superset of V3Api.

- Added a ``retries`` to the ``ThreediApi`` which enables setting a retry policy.
  For the async client, ``aiohttp_retry`` is included.

- Changed the default ``timeout`` of asynchronous file down/upload from 5 minutes total to
  only socket timeouts of 5 seconds. This allows upload of larger files.

- Changed the default socket read ``timeout`` of uploads from 5 seconds to 10 minutes
  to accomodate large file uploads.


3.0.29 (2021-06-02)
-------------------

- Moved documentation to readthedocs and consistently named the project from
  threedi-api-client (instead of threedi-openapi-client).


3.0.28 (2021-05-04)
-------------------

- Renamed general settings to physical settings.


3.0.27 (2021-04-26)
-------------------

- Dropped support for Python 3.5.

- Added upload and download file functions (sync and async).


3.0.26 (2021-04-07)
-------------------

- Put leakage back. Was missing because local API definition was out of sync.


3.0.25 (2021-04-07)
-------------------

- Added simulation settings.


3.0.24 (2021-03-19)
-------------------

- Added leakage to API


3.0.23 (2021-03-03)
-------------------

- Removed print statement.


3.0.22 (2021-02-12)
-------------------

- Fix: The expiry function for automatic token renewal did not work.


3.0.21 (2021-01-21)
-------------------

- New filters and usage statistics models.


3.0.20 (2021-01-07)
-------------------

- Fix threedi_api_client import.


3.0.19 (2021-01-07)
-------------------

- Run pytest with `python -m pyest...` to make sure the current path is added to the PYTHONPATH.


3.0.18 (2021-01-07)
-------------------

- Make sure aio module is distributed as well.


3.0.17 (2020-12-01)
-------------------

- Added boundary conditions (file) upload


3.0.16 (2020-11-04)
-------------------

- Pinned aiohttp to 3.6.3,  with >= 3.7.0 yarl and mulitdict
  needs to be build with GCC.

- Removed laterals/file/upload endpoint

- Added endpoint for retrying Lizard (results) postprocessing


3.0.15 (2020-10-14)
-------------------

- Added user to lizardrasterrain and lizard raster sources&sinks


3.0.14 (2020-10-14)
-------------------

- Retrying release


3.0.13 (2020-10-14)
-------------------

- Added extent/point swagger definitions

- Added filelateral to swagger


3.0.12 (2020-10-13)
-------------------

- Retrying release


3.0.11 (2020-10-13)
-------------------

- Added user to Lizard raster rain and Lizard raster sources sinks

- Added gh-actions release pipeline.


3.0.10 (2020-09-29)
-------------------

- Added bulk-lateral events.


3.0.9 (2020-09-16)
------------------

- Added table and memory structure controls.


3.0.8 (2020-09-04)
------------------

- Renamed timestructurecontrol to timestructurecontrols.


3.0.7 (2020-08-20)
------------------

- Add example notebooks in the documentation.


3.0.6 (2020-07-31)
------------------

- Update exit code definitions.


3.0.5 (2020-07-31)
------------------

- Added exit_code field to status resource.

- Added breaches graph endpoint.


3.0.4 (2020-07-15)
------------------

- Added pumps discharge graph endpoint

- Added more filtering options on contracts


3.0.4b3 (2020-07-10)
--------------------

- Added id field everywhere


3.0.4b2 (2020-07-08)
--------------------

- Generated with generator version v4.3.0

- Fixed problem with threedimodel on simulation resource (was integer should be string)


3.0.4b1 (2020-07-07)
--------------------

- Damage estimation is not required


3.0.3 (2020-06-16)
------------------

- Changed Lizard postprocessing overview endpoint


3.0.2 (2020-06-12)
------------------

- Username filters for simulations endpoint.


3.0.1 (2020-06-09)
------------------

- Added statistics endpoint

- Changed Lizard post-processing endpoint
  (not backwards compatible, however intended to be used only by Lizard)


3.0 (2020-05-25)
----------------

- Official production release


3.0.b24 (2020-05-22)
--------------------

- All uid fields on events should be read-only


3.0.b23 (2020-05-20)
--------------------

- Added wind global drag coefficient


3.0.b22 (2020-05-18)
--------------------

- Added max_rate to actions


3.0.b21 (2020-05-15)
--------------------

- Status field crash_report has become detail.


3.0.b20 (2020-05-11)
--------------------

- Added breaches and more fields to potentialbreaches


3.0.b19 (2020-04-24)
--------------------

- File filter exclude/include simulation status.


3.0.b18 (2020-04-24)
--------------------

- Added 'active' to inpy-version resource


3.0.b17 (2020-04-20)
--------------------

- Added icontains filters


3.0.b16 (2020-04-10)
--------------------

- Added uuid field to initial saved state serializer.


3.0.b15 (2020-04-01)
--------------------

- Added simulation websocket channels overview endpoints


3.0.b14 (2020-03-23)
--------------------

- Added raster-edits processing endpoints


3.0.b13 (2020-03-20)
--------------------

- Split up waterlevel graph endpoint in
  waterflow and waterlevel graph endpoint

- Added waterprofile graph endpoint


3.0.b12 (2020-03-10)
--------------------

- Added waterlevel graph endpoint


3.0.b11 (2020-03-06)
--------------------

- Added users endpoint

- Changed user endpoint to profile endpoint

- Added more filters


3.0b10 (2020-02-19)
-------------------

- Simulation model now has a 'tags' field.


3.0.b9 (2020-02-12)
-------------------

- Support for interactive simulations.

- Result API endpoints.


3.0.b8 (2020-02-10)
-------------------

- Edit Constant and Timeseries Wind events


3.0.b7 (2020-02-03)
-------------------

- Added wind

- Added visualization endpoints


3.0.b6 (2020-01-29)
-------------------

- Something went wrong with the 3.0.b5 release, next rty.


3.0.b5 (2020-01-27)
-------------------

- Raster edits, event uuids.


3.0.b4 (2019-12-12)
-------------------

- Local rain events.


3.0.b3 (2019-12-09)
-------------------

- Less strict requirement for dependencies 'six' and 'urllib3' to
  avoid pipenv resolve issues at Lizard


3.0.b2 (2019-12-02)
-------------------

- Changed 'set_pump_discharge' to 'set_pump_capacity'.


3.0.b1 (2019-11-28)
-------------------

- Updated API descriptions

- Raster resource filtering


3.0.b0 (2019-11-28)
-------------------

- First 3.0 release candidate

- All swagger schema's are automatically saved in
  schemas/swagger_xxx.yaml

0.0.23 (2019-11-26)
-------------------

- Fixing releases


0.0.22 (2019-11-26)
-------------------

- Added `initialwaterlevel rasters` and `postprocessing`


0.0.21 (2019-11-18)
-------------------

- Fixed ThreediApiClient constructor not working with config keywords and
  .env file.

- Added initial waterlevels


0.0.20 (2019-11-11)
-------------------

- Added `simulation` and `simulation_id` to statuses serializer.

- Automatically get a new JWT token when
  the current one is valid less than 5 minutes.

- Use `mkdocs` for documentation.

0.0.17.3 (2019-11-04)
---------------------

- Test release.


0.0.17.2 (2019-11-04)
---------------------

- Test release.


0.0.17.1 (2019-11-01)
---------------------

- Add boundary model.


0.0.17c (2019-11-01)
--------------------

- Added boundaries to simulation events and updated docs.


0.0.17b (2019-10-31)
--------------------

- Bulk boundary conditions.


0.0.17a (2019-10-31)
--------------------

- Boundary conditions.


0.0.17 (2019-10-30)
-------------------

- Limit compatible python versions


0.1.9 (2019-10-30)
------------------

- Added resource `statuses`.


0.1.8 (2019-10-17)
------------------

- Added timed control


0.1.7 (2019-09-25)
------------------

- Laterals now have id field.

- Usage integration


0.1.6 (2019-09-04)
------------------

- Added geojson/gridadmin/rasters upload & download


0.1.5 (2019-07-03)
------------------

- Updated file uploading


0.1.4 (2019-06-24)
------------------

- Include modules.


0.1.3 (2019-06-24)
------------------

- Fix package name


0.1.2 (2019-06-24)
------------------

- PyPi release.


0.1.1 (2019-06-21)
------------------

* Included more endpoints


0.1.0 (2019-05-10)
------------------

* First release on PyPI.
