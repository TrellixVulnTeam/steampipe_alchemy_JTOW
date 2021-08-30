from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2NetworkInterface(Base, FormatMixins):
    __tablename__ = 'aws_ec2_network_interface'
    association_customer_owned_ip = Column('association_customer_owned_ip', psql.INET, nullable=True)
    private_ip_address = Column('private_ip_address', psql.INET, nullable=True)
    attachment_time = Column('attachment_time', TIMESTAMP, nullable=True)
    requester_managed = Column('requester_managed', Boolean, nullable=True)
    source_dest_check = Column('source_dest_check', Boolean, nullable=True)
    groups = Column('groups', JSON, nullable=True)
    ipv6_addresses = Column('ipv6_addresses', JSON, nullable=True)
    private_ip_addresses = Column('private_ip_addresses', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    delete_on_instance_termination = Column('delete_on_instance_termination', Boolean, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    device_index = Column('device_index', BigInteger, nullable=True)
    association_carrier_ip = Column('association_carrier_ip', psql.INET, nullable=True)
    association_public_ip = Column('association_public_ip', psql.INET, nullable=True)
    outpost_arn = Column('outpost_arn', Text, nullable=True)
    private_dns_name = Column('private_dns_name', Text, nullable=True)
    requester_id = Column('requester_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    network_interface_id = Column('network_interface_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    interface_type = Column('interface_type', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    association_allocation_id = Column('association_allocation_id', Text, nullable=True)
    association_id = Column('association_id', Text, nullable=True)
    association_ip_owner_id = Column('association_ip_owner_id', Text, nullable=True)
    association_public_dns_name = Column('association_public_dns_name', Text, nullable=True)
    attached_instance_id = Column('attached_instance_id', Text, nullable=True)
    attached_instance_owner_id = Column('attached_instance_owner_id', Text, nullable=True)
    attachment_id = Column('attachment_id', Text, nullable=True)
    attachment_status = Column('attachment_status', Text, nullable=True)
    mac_address = Column('mac_address', Text, nullable=True)