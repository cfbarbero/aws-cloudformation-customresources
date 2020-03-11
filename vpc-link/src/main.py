import crhelper
import boto3

# initialise logger
logger = crhelper.log_config({"RequestId": "CONTAINER_INIT"})
logger.info('Logging configured')
# set global to track init failures
init_failed = False

client = boto3.client('apigateway')

try:
    # Place initialization code here
    logger.info("Container initialization completed")
except Exception as e:
    logger.error(e, exc_info=True)
    init_failed = e


def create(event, context):
    # response = client.create_vpc_link(
    #     name='string',
    #     description='string',
    #     targetArns=[
    #         'string',
    #     ]
    # )

    physical_resource_id = 'cb-test-resource'
    response_data = {'blah': 'other'}
    return physical_resource_id, response_data


def update(event, context):
    """
    Place your code to handle Update events here

    To return a failure to CloudFormation simply raise an exception, the exception message will be sent to CloudFormation Events.
    """
    physical_resource_id = event['PhysicalResourceId']
    response_data = {'blah': 'update'}
    return physical_resource_id, response_data


def delete(event, context):
    """
    Place your code to handle Delete events here

    To return a failure to CloudFormation simply raise an exception, the exception message will be sent to CloudFormation Events.
    """
    return


def handler(event, context):
    """
    Main handler function, passes off it's work to crhelper's cfn_handler
    """
    # update the logger with event info
    global logger
    logger = crhelper.log_config(event)
    return crhelper.cfn_handler(event, context, create, update, delete, logger,
                                init_failed)
