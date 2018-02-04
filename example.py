#!/usr/bin/env python
"""
Example script for DeceptionLogicAPI

In this example, API credentials must be exported to environment variables:
export DECEPTIONLOGIC_KEYID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
export DECEPTIONLOGIC_SECRETKEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

from __future__ import print_function
import os
import json
from DeceptionLogicAPI import DeceptionLogicAPI


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
    delo = DeceptionLogicAPI.DeceptionLogicAPI(keyid, secret)

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
            'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX')
        out(status)

        # Get a single agent
        # Parameter is the agent_id
        agent = delo.get_agent(
            'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        out(agent)
        """


if __name__ == '__main__':
    main()
