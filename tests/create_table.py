"""motoのサーバーのテストを行う。
"""

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import boto3
import pytest

class Thread(Model):
    class Meta:
        table_name = 'Thread'
        # region = os.environ["AWS_DEFAULT_REGION"]
        host = "http://localhost:5000"
    forum_name = UnicodeAttribute(hash_key=True)
    my_nullable_attribute = UnicodeAttribute(null=True)


def test_01():
    Thread.create_table()
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:5000")
    print("aa")
    for table in dynamodb.tables.all():
        print(table.name)

def test_02():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:5000")
    for table in dynamodb.tables.all():
        print(table.name)

def test_03():
    thread = Thread("forum1")
    thread.save()
    print(thread.attribute_values)

def test_04():
    thread = Thread.get("forum1")
    print(thread.attribute_values)

def test_05():
    with pytest.raises(Thread.DoesNotExist):
        thread = Thread.get("forum2")
