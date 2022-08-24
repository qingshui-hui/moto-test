import boto3
import json
import yaml

import pytest
from botocore.exceptions import ClientError

from moto.core import DEFAULT_ACCOUNT_ID as ACCOUNT_ID


TEMPLATE_ROLE_INSTANCE_PROFILE = """
AWSTemplateFormatVersion: 2010-09-09
Resources:
  RootRole:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: TestUser
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
              - ec2.amazonaws.com
            Action:
              - 'sts:AssumeRole'
      Path: /
      Policies:
        - PolicyName: root
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action: '*'
                Resource: '*'
  RootInstanceProfile:
    Type: 'AWS::IAM::InstanceProfile'
    Properties:
      Path: /
      Roles:
        - !Ref RootRole
"""
stack_name = "ut-stack"

def test_01():
    cf_client = boto3.client("cloudformation", endpoint_url="http://localhost:5000")

    template = TEMPLATE_ROLE_INSTANCE_PROFILE

    cf_client.create_stack(StackName=stack_name, TemplateBody=template)
    # cf_client.update_stack(StackName=stack_name, TemplateBody=template)

    provisioned_resource = cf_client.list_stack_resources(StackName=stack_name)[
        "StackResourceSummaries"
    ][0]
    print(provisioned_resource)


def test_02():
    iam_client = boto3.client("iam", endpoint_url="http://localhost:5000")
    role = iam_client.get_role(RoleName="TestUser")["Role"]
    print(role)

# def test_03():
#     cf_client = boto3.client("cloudformation", endpoint_url="http://localhost:5000")
#     cf_client.delete_stack(StackName=stack_name)

def test_04():
    cf_client = boto3.client("cloudformation", endpoint_url="http://localhost:5000")

    with open("tests/iam_role.yml", "r", encoding="utf-8") as f:
        template = f.read()
    cf_client.create_stack(StackName="LambdaStack", TemplateBody=template)
    # cf_client.update_stack(StackName="LambdaStack", TemplateBody=template)
    provisioned_resource = cf_client.list_stack_resources(StackName="LambdaStack")[
        "StackResourceSummaries"
    ][0]
    print(provisioned_resource)
