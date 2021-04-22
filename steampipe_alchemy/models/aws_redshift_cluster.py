from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRedshiftCluster(Base):
    __tablename__ = 'aws_redshift_cluster'
    cluster_identifier = Column('cluster_identifier', Text, nullable=True)
    cluster_namespace_arn = Column('cluster_namespace_arn', Text, nullable=True)
    allow_version_upgrade = Column('allow_version_upgrade', Boolean, nullable=True)
    automated_snapshot_retention_period = Column('automated_snapshot_retention_period', BigInteger, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    availability_zone_relocation_status = Column('availability_zone_relocation_status', Text, nullable=True)
    cluster_availability_status = Column('cluster_availability_status', Text, nullable=True)
    cluster_create_time = Column('cluster_create_time', TIMESTAMP, nullable=True)
    cluster_nodes = Column('cluster_nodes', JSON, nullable=True)
    cluster_parameter_groups = Column('cluster_parameter_groups', JSON, nullable=True)
    cluster_public_key = Column('cluster_public_key', Text, nullable=True)
    cluster_revision_number = Column('cluster_revision_number', Text, nullable=True)
    cluster_security_groups = Column('cluster_security_groups', JSON, nullable=True)
    cluster_snapshot_copy_status = Column('cluster_snapshot_copy_status', JSON, nullable=True)
    cluster_status = Column('cluster_status', Text, nullable=True)
    cluster_subnet_group_name = Column('cluster_subnet_group_name', Text, nullable=True)
    cluster_version = Column('cluster_version', Text, nullable=True)
    data_transfer_progress = Column('data_transfer_progress', JSON, nullable=True)
    db_name = Column('db_name', Text, nullable=True)
    deferred_maintenance_windows = Column('deferred_maintenance_windows', JSON, nullable=True)
    elastic_ip_status = Column('elastic_ip_status', JSON, nullable=True)
    elastic_resize_number_of_node_options = Column('elastic_resize_number_of_node_options', Text, nullable=True)
    encrypted = Column('encrypted', Boolean, nullable=True)
    endpoint = Column('endpoint', JSON, nullable=True)
    enhanced_vpc_routing = Column('enhanced_vpc_routing', Boolean, nullable=True)
    expected_next_snapshot_schedule_time = Column('expected_next_snapshot_schedule_time', TIMESTAMP, nullable=True)
    expected_next_snapshot_schedule_time_status = Column('expected_next_snapshot_schedule_time_status', Text, nullable=True)
    hsm_status = Column('hsm_status', JSON, nullable=True)
    iam_roles = Column('iam_roles', JSON, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    maintenance_track_name = Column('maintenance_track_name', Text, nullable=True)
    manual_snapshot_retention_period = Column('manual_snapshot_retention_period', BigInteger, nullable=True)
    master_username = Column('master_username', Text, nullable=True)
    modify_status = Column('modify_status', Text, nullable=True)
    next_maintenance_window_start_time = Column('next_maintenance_window_start_time', TIMESTAMP, nullable=True)
    node_type = Column('node_type', Text, nullable=True)
    number_of_nodes = Column('number_of_nodes', BigInteger, nullable=True)
    pending_actions = Column('pending_actions', JSON, nullable=True)
    pending_modified_values = Column('pending_modified_values', JSON, nullable=True)
    preferred_maintenance_window = Column('preferred_maintenance_window', Text, nullable=True)
    publicly_accessible = Column('publicly_accessible', Boolean, nullable=True)
    resize_info = Column('resize_info', JSON, nullable=True)
    restore_status = Column('restore_status', JSON, nullable=True)
    snapshot_schedule_identifier = Column('snapshot_schedule_identifier', Text, nullable=True)
    snapshot_schedule_state = Column('snapshot_schedule_state', Text, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    vpc_security_groups = Column('vpc_security_groups', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)