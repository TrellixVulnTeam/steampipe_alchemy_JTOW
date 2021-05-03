from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2ClassicLoadBalancer(Base, FormatMixins):
    __tablename__ = 'aws_ec2_classic_load_balancer'
    name = Column('name', Text, primary_key=True, nullable=True)
    scheme = Column('scheme', Text, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    access_log_emit_interval = Column('access_log_emit_interval', BigInteger, nullable=True)
    access_log_enabled = Column('access_log_enabled', Boolean, nullable=True)
    access_log_s3_bucket_name = Column('access_log_s3_bucket_name', Text, nullable=True)
    access_log_s3_bucket_prefix = Column('access_log_s3_bucket_prefix', Text, nullable=True)
    canonical_hosted_zone_name = Column('canonical_hosted_zone_name', Text, nullable=True)
    canonical_hosted_zone_name_id = Column('canonical_hosted_zone_name_id', Text, nullable=True)
    connection_draining_enabled = Column('connection_draining_enabled', Boolean, nullable=True)
    connection_draining_timeout = Column('connection_draining_timeout', BigInteger, nullable=True)
    connection_settings_idle_timeout = Column('connection_settings_idle_timeout', BigInteger, nullable=True)
    cross_zone_load_balancing_enabled = Column('cross_zone_load_balancing_enabled', Boolean, nullable=True)
    dns_name = Column('dns_name', Text, nullable=True)
    health_check_interval = Column('health_check_interval', BigInteger, nullable=True)
    health_check_timeout = Column('health_check_timeout', BigInteger, nullable=True)
    healthy_threshold = Column('healthy_threshold', BigInteger, nullable=True)
    heath_check_target = Column('heath_check_target', Text, nullable=True)
    source_security_group_name = Column('source_security_group_name', Text, nullable=True)
    source_security_group_owner_alias = Column('source_security_group_owner_alias', Text, nullable=True)
    unhealthy_threshold = Column('unhealthy_threshold', BigInteger, nullable=True)
    additional_attributes = Column('additional_attributes', JSON, nullable=True)
    app_cookie_stickiness_policies = Column('app_cookie_stickiness_policies', JSON, nullable=True)
    availability_zones = Column('availability_zones', JSON, nullable=True)
    backend_server_descriptions = Column('backend_server_descriptions', JSON, nullable=True)
    instances = Column('instances', JSON, nullable=True)
    lb_cookie_stickiness_policies = Column('lb_cookie_stickiness_policies', JSON, nullable=True)
    listener_descriptions = Column('listener_descriptions', JSON, nullable=True)
    other_policies = Column('other_policies', JSON, nullable=True)
    security_groups = Column('security_groups', JSON, nullable=True)
    subnets = Column('subnets', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)