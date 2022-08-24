from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from moto import mock_dynamodb
import boto3


class Thread(Model):
    class Meta:
        table_name = 'Thread'
        # region = os.environ["AWS_DEFAULT_REGION"]
    forum_name = UnicodeAttribute(hash_key=True)
    my_nullable_attribute = UnicodeAttribute(null=True)

@mock_dynamodb
def test_01():
    Thread.create_table()
    dynamodb = boto3.resource('dynamodb')

    for table in dynamodb.tables.all():
        print(table.name)
