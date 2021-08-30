from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsLambdaFunction(Base, FormatMixins):
    __tablename__ = 'aws_lambda_function'
    vpc_subnet_ids = Column('vpc_subnet_ids', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    code_size = Column('code_size', BigInteger, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    reserved_concurrent_executions = Column('reserved_concurrent_executions', BigInteger, nullable=True)
    memory_size = Column('memory_size', BigInteger, nullable=True)
    vpc_security_group_ids = Column('vpc_security_group_ids', JSON, nullable=True)
    version = Column('version', Text, nullable=True)
    master_arn = Column('master_arn', Text, nullable=True)
    revision_id = Column('revision_id', Text, nullable=True)
    role = Column('role', Text, nullable=True)
    runtime = Column('runtime', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    state_reason = Column('state_reason', Text, nullable=True)
    state_reason_code = Column('state_reason_code', Text, nullable=True)
    last_update_status = Column('last_update_status', Text, nullable=True)
    last_update_status_reason = Column('last_update_status_reason', Text, nullable=True)
    last_update_status_reason_code = Column('last_update_status_reason_code', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    code_sha_256 = Column('code_sha_256', Text, nullable=True)
    dead_letter_config_target_arn = Column('dead_letter_config_target_arn', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    handler = Column('handler', Text, nullable=True)
    kms_key_arn = Column('kms_key_arn', Text, nullable=True)
    last_modified = Column('last_modified', Text, nullable=True)
    timeout = Column('timeout', Text, nullable=True)