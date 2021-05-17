from threedi_api_client import ThreediApiClient
from openapi_client import *
from threedi_api_client.aio.files import *

import logging

# create logger with 'spam_application'
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)



client = ThreediApiClient("./.env")
upload = {'filename': 'gridadmin.h5',
 'put_url': 'http://minio:9000/3di/10/gridadmin.h5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=buildout%2F20210421%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210421T150451Z&X-Amz-Expires=172800&X-Amz-SignedHeaders=host&X-Amz-Signature=4884b5620e5a38f47748c85d4d71fca9915203b2585943c80017ba847f1a2803'}
path ="/home/casper/threedi_models/v2_bergermeer/3a58dfb2e95f10ca121e26e4259ed68f60e3268f/v2_bergermeer_simple_infil_no_grndwtr/preprocessed/gridadmin.h5"
# download = {'etag': '2d26b0a9214629f13dd89a03c6742ba4',
#  'get_url': 'http://minio:9000/3di/10/gridadmin.h5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=buildout%2F20210422%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210422T132610Z&X-Amz-Expires=172800&X-Amz-SignedHeaders=host&X-Amz-Signature=4d5293c2374512da53a1aae32ad2199e63f125094496641cde47c874dfb63ff2',
#  'size': 16788529}


download = {
    "get_url": "https://files.3di.live/3di/3556/dem_co.tif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=3di%2F20210422%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210422T150117Z&X-Amz-Expires=172800&X-Amz-SignedHeaders=host&X-Amz-Signature=b5cee456904114fd30f620f15b72eaa38fbc427ead09b24e97626d1882cb22e6",
    "etag": "dc9c18a74803f61c3ae56de86285a09a-1",
    "size": 99418787
}
