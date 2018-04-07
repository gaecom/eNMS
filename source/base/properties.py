from collections import OrderedDict

object_common_properties = (
    'name',
    'description',
    'location',
    'type',
    'vendor'
)

node_common_properties = (
    'operating_system',
    'os_version',
    'ip_address',
    'longitude',
    'latitude',
    'secret_password'
)

link_common_properties = (
    'source',
    'destination',
)

node_public_properties = (
    object_common_properties +
    node_common_properties[:-1]
)

link_public_properties = (
    object_common_properties +
    link_common_properties
)

public_properties = (
    node_public_properties +
    link_public_properties
)

type_to_public_properties = OrderedDict([
    ('Antenna', node_public_properties),
    ('Firewall', node_public_properties),
    ('Host', node_public_properties),
    ('Optical switch', node_public_properties),
    ('Regenerator', node_public_properties),
    ('Router', node_public_properties),
    ('Switch', node_public_properties),
    ('Server', node_public_properties),
    ('BGP peering', link_public_properties),
    ('Etherchannel', link_public_properties),
    ('Ethernet link', link_public_properties),
    ('Optical channel', link_public_properties),
    ('Optical link', link_public_properties),
    ('Pseudowire', link_public_properties)
])

## Diagram properties (for the dashboard)

object_diagram_properties = (
    'description',
    'location',
)

node_diagram_properties = object_diagram_properties + (
    'type',
    'vendor',
    'operating_system',
    'os_version'
)

link_diagram_properties = object_diagram_properties + (
    'type',
    'vendor'
)

user_diagram_properties = (
    'type',
    'access_rights',
)

workflow_diagram_properties = (
    'type',
    'vendor',
    'operating_system'
)

script_diagram_properties = (
    'type',
    'vendor',
    'operating_system'
)

task_diagram_properties = (
    'type',
    'recurrent',
)

type_to_diagram_properties = {
    'node': node_diagram_properties,
    'link': link_diagram_properties,
    'user': user_diagram_properties,
    'script': script_diagram_properties,
    'workflow': workflow_diagram_properties,
    'task': task_diagram_properties
}

pretty_names = OrderedDict([
    ('access_rights', 'Access rights'),
    ('content', 'Content'),
    ('description', 'Description'),
    ('destination', 'Destination'),
    ('email', 'Email'),
    ('ip_address', 'IP address'),
    ('longitude', 'Longitude'),
    ('latitude', 'Latitude'),
    ('location', 'Location'),
    ('name', 'Name'),
    ('operating_system', 'Operating System'),
    ('os_version', 'OS version'),
    ('secret_password', 'Secret password'),
    ('source', 'Source'),
    ('type', 'Type'),
    ('vendor', 'Vendor'),
])

reverse_pretty_names = {v: k for k, v in pretty_names.items()}
