from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamServerCertificate(Base, FormatMixins):
    __tablename__ = 'aws_iam_server_certificate'
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    upload_date = Column('upload_date', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    expiration = Column('expiration', TIMESTAMP, nullable=True)
    path = Column('path', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    server_certificate_id = Column('server_certificate_id', Text, nullable=True)
    certificate_body = Column('certificate_body', Text, nullable=True)
    certificate_chain = Column('certificate_chain', Text, nullable=True)