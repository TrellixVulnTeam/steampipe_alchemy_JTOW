from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRedshiftParameterGroup(Base, FormatMixins):
    __tablename__ = 'aws_redshift_parameter_group'
    akas = Column('akas', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    family = Column('family', Text, nullable=True)
    title = Column('title', Text, nullable=True)