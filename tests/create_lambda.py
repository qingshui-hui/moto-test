import boto3
import io
import zipfile

with open("functions/access_log_lambda/app.py", "r", encoding="utf-8") as f:
    lambda_code = f.read()


def _process_lambda(func_str):
    zip_output = io.BytesIO()
    zip_file = zipfile.ZipFile(zip_output, "w", zipfile.ZIP_DEFLATED)
    zip_file.writestr("app.py", func_str)
    zip_file.close()
    zip_output.seek(0)
    return zip_output.read()


def test_create_lambda():
    # 複数回実行してもエラーにならなかった。
    lambda_client = boto3.client("lambda", endpoint_url="http://localhost:5000")
    response = lambda_client.create_function(
        FunctionName="AccessLogLambda",
        Runtime="python3.8",  # for error
        Role="arn:aws:iam::123456789012:role/WeekLambdaRole",
        # Role='arn:aws:iam::123456789012:role/LambdaRole',
        Handler="app.lambda_handler",
        Code={
            # 'S3Bucket': 'lambda',
            # 'S3Key': 'access_log_lambda.zip',
            "ZipFile": _process_lambda(lambda_code),
        },
        Timeout=120,
        MemorySize=256,
        Environment={"Variables": {"string": "string"}},
    )
    print(response)


def test_call_lambda():
    # docker-desktopを立ち上げていないとdocker versionでエラーになった。
    # 次に立ち上げると、lambci/lambdaがpython3.9に対応していないことによるエラーになった。
    # https://github.com/lambci/docker-lambda/issues/343
    # https://hub.docker.com/r/lambci/lambda/
    lambda_client = boto3.client("lambda", endpoint_url="http://localhost:5000")
    res = lambda_client.invoke(FunctionName="AccessLogLambda")
    print(res)
    print("Payload", res["Payload"].read().decode("utf-8"))
