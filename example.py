#!/usr/bin/env python
"""
Example script for using the Deception Logic API client

In this example, API credentials must be exported to environment variables:
export DECEPTIONLOGIC_KEYID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
export DECEPTIONLOGIC_SECRETKEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

from __future__ import print_function
import os
import json
from deceptionlogic import api, aws


def out(json_data):
    """
    Output json data in pretty format
    """
    print(json.dumps(json_data, indent=4))


def main():
    """
    The main fuction for executing example code
    """

    # Get API keys from environment variables and create the
    # Deception Logic API object.
    keyid = os.environ["DECEPTIONLOGIC_KEYID"]
    secret = os.environ["DECEPTIONLOGIC_SECRET"]
    delo = api.Client(keyid, secret)

    # Authenticate to the API and retreive API tokens.
    result = delo.authenticate()

    # Check for authentication status
    if result["status"] != "success":
        print("Authentiaction failed.")
    else:
        # Store token and id values to the class object variables
        # token and identifier respectivley
        delo.token = result["token"]
        delo.identifier = result["id"]

        # Get all profiles
        profiles = delo.get_profiles()
        out(profiles)

        # Get all services
        services = delo.get_services()
        out(services)

        # Get all agents
        agents = delo.get_agents()
        out(agents)

        """
        # Example of changing an agent's profile
        # First parameter is the agent_id
        # Second parameter is the profile_guid
        status = delo.set_agent_profile(
            'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            '00000000-0000-0000-0000-000000000001')
        out(status)

        # Get a single agent
        # Parameter is the agent_id
        agent = delo.get_agent(
            'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        out(agent)
        """

        """
        # Example of updating Amazon EC2 security group based on a profile.
        # The deceptionlogic.aws module implements the boto3 SDK,
        # see documentation for configuring AWS credentials and region:
        # http://boto3.readthedocs.io/en/latest/guide/quickstart.html#configuration
        ec2 = aws.EC2()

        # get profile record
        profile = delo.get_profile('00000000-0000-0000-0000-000000000001')

        # get services defined in profile record
        services = profile[0]['services'][0]

        # add an ip permission for each service
        for service in services:
            ec2.add_ip_permission(delo.get_service(service['guid']))

        # set security group ip permissions based on security group name
        ec2.set_ip_permissions('launch-wizard-1')
        """


if __name__ == '__main__':
    main()
