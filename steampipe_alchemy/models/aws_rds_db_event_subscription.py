from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRdsDbEventSubscription(Base, FormatMixins):
    __tablename__ = 'aws_rds_db_event_subscription'
    enabled = Column('enabled', Boolean, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    subscription_creation_time = Column('subscription_creation_time', TIMESTAMP, nullable=True)
    event_categories_list = Column('event_categories_list', JSON, nullable=True)
    source_ids_list = Column('source_ids_list', JSON, nullable=True)
    source_type = Column('source_type', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    cust_subscription_id = Column('cust_subscription_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    customer_aws_id = Column('customer_aws_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    sns_topic_arn = Column('sns_topic_arn', Text, nullable=True)