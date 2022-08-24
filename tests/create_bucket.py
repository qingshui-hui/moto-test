import boto3


def test_put():
    # Create Bucket so that test can run
    conn = boto3.resource("s3", endpoint_url="http://localhost:5000")
    bucket = conn.create_bucket(Bucket="lambda", CreateBucketConfiguration={
        "LocationConstraint": "ap-northeast-1"
    })
    ####################################
    with open('zip/access_log_lambda.zip', 'r') as f:
        value = f.buffer.read()
    bucket.put_object(Key='access_log_lambda.zip', Body=value)

def test_get():
    conn = boto3.resource("s3", endpoint_url="http://localhost:5000")
    bucket = conn.Bucket("lambda")
    ####################################
    bucket.download_file("access_log_lambda.zip", "access_log_lambda.zip")
