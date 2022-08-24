import boto3
import os

def lambda_handler(event, context):
    # http://docs.getmoto.org/en/latest/docs/services/lambda.html#lambda
    url = os.environ.get("MOTO_HTTP_ENDPOINT")
    dynamodb = boto3.resource("dynamodb", endpoint_url=url)
    table = dynamodb.Table("Thread")
    table.put_item(Item={
        "forum_name": "forum1"
    })
    return {
        "status_code": 200,
        "body": "hello"
    }
