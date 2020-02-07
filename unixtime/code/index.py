from __future__ import print_function
from crhelper import CfnResource
import requests
import logging
import json

helper = CfnResource()
logger = logging.getLogger()

@helper.create
@helper.update
def unixtime(event, context):
    logger.info("Getting Data from the API")
    r = requests.get('http://worldtimeapi.org/api/timezone/Europe/' + event['ResourceProperties']['State'])
    res = (json.loads(r.text))['unixtime']
    helper.Data['Res'] = res
    logger.info("Processing Completed ....")
@helper.delete
def no_op(event, context):
    pass

def handler(event, context):
    helper(event, context)