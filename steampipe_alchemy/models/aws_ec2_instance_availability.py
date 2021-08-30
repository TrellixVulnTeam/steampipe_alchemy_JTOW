from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2InstanceAvailability(Base, FormatMixins):
    __tablename__ = 'aws_ec2_instance_availability'
    akas = Column('akas', JSON, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    location = Column('location', Text, nullable=True)
    location_type = Column('location_type', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)