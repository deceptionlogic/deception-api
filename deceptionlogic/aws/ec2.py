"""
Deception Logic AmazonEC2 API Wrapper
"""

import boto3


class EC2(object):
    """
    Base class for Deception Logic integration with AmazonEC2
    """
    ec2 = None
    ec2_resource = None

    permissions = []

    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.ec2_resource = boto3.resource('ec2')

    def clear_ip_permissions(self, group_id):
        """
        Clears the security group ip permissions.
        Call this before setting new ip permissions.
        """
        security_group = self.ec2_resource.SecurityGroup(group_id)
        security_group.revoke_ingress(
            IpPermissions=security_group.ip_permissions)

    def set_ip_permissions(self, name):
        """
        Sets the ip permissions in the security group of
        the provided security group name.
        """
        group_id = self.get_security_group_id(name)

        # First clear ip permissions
        self.clear_ip_permissions(group_id)

        security_group = self.ec2_resource.SecurityGroup(group_id)
        security_group.authorize_ingress(IpPermissions=self.permissions)

    def add_ip_permission(self, service):
        """
        Adds an ip permission to self.permissions, which
        will be used in self.set_ip_permissions()
        """
        model = {'FromPort': 22,
                 'IpProtocol': 'tcp',
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
                 'Ipv6Ranges': [{'CidrIpv6': '::/0'}],
                 'PrefixListIds': [],
                 'ToPort': 22,
                 'UserIdGroupPairs': []}

        model['IpProtocol'] = service[0]['protocol']
        model['ToPort'] = service[0]['internal_port']

        if service[0]['internal_port'] != service[0]['external_port']:
            model['FromPort'] = service[0]['external_port']
        else:
            model['FromPort'] = service[0]['internal_port']

        self.permissions.append(model)

    def get_security_group_id(self, name):
        """
        # Retrieves the security group id for a given security
        # group name
        """
        filters = [{'Name': 'group-name', 'Values': [name]}]
        response = self.ec2.describe_security_groups(Filters=filters)

        return response['SecurityGroups'][0]['GroupId']
