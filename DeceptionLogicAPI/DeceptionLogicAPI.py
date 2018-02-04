"""
Deception Logic API
"""

import requests


class DeceptionLogicAPI(object):
    """
    Base class for making requests to the Deception Logic API.
    https://deceptionlogic.com
    """
    base_url = "https://api.deceptionlogic.com/"
    api_version = "v0"
    token = None
    identifier = None
    authenticate_endpoint = "/authenticate"
    alerts_endpoint = "/alerts"
    events_endpoint = "/events"
    profiles_endpoint = "/profiles"
    services_endpoint = "/services"
    service_endpoint = "/service"
    agent_endpoint = "/agent"
    agents_endpoint = "/agents"

    def __init__(self, keyid, secretkey):
        """
        Return a DeceptionLogic object
        """
        self.keyid = keyid
        self.secretkey = secretkey

    def _make_request(self, endpoint, method="GET",
                      append_url="", options=None):
        """
        Compose and submit API call.
        """
        data = dict()

        if self.token is None:
            headers = {
                'X-DeceptionLogic-KeyId': self.keyid,
                'X-DeceptionLogic-SecretKey': self.secretkey
            }
        else:
            headers = {
                'X-DeceptionLogic-Token': self.token,
                'X-DeceptionLogic-Id': self.identifier
            }

        if options is not None:
            for key in options:
                data[key] = options[key]

        url = self.base_url + self.api_version + endpoint + "/" + append_url
        result = None

        if method == "GET":
            result = requests.get(url, params=data, headers=headers)
        elif method == "POST":
            headers['Content-Type'] = "application/json"
            result = requests.post(url, json=data, headers=headers)
        else:
            raise Exception("InvalidMethod: " + str(method))

        return result.json()

    def authenticate(self):
        """
        Authenticate to the Deception Logic API.
        """
        return self._make_request(self.authenticate_endpoint)

    def get_alerts(self):
        """
        Get all alerts
        """
        return self._make_request(endpoint=self.alerts_endpoint)

    def get_events(self):
        """
        Get all events
        """
        return self._make_request(endpoint=self.events_endpoint)

    def get_profiles(self):
        """
        Get all profiles
        """
        return self._make_request(endpoint=self.profiles_endpoint)

    def get_services(self):
        """
        Get all services
        """
        return self._make_request(endpoint=self.services_endpoint)

    def get_service(self, guid):
        """
        Get a service record by guid
        """
        return self._make_request(
            endpoint=self.service_endpoint, append_url=guid)

    def get_agents(self):
        """
        Get all agents
        """
        return self._make_request(endpoint=self.agents_endpoint)

    def get_agent(self, agent_id):
        """
        Get an agent record by agent_id
        """
        return self._make_request(
            endpoint=self.agent_endpoint, append_url=agent_id)

    def set_agent_profile(self, agent_id, profile_guid):
        """
        Post update to an agent record by agent_id
        """
        post_data = {'profile_guid': profile_guid}
        return self._make_request(
            endpoint=self.agent_endpoint,
            method="POST",
            append_url=agent_id,
            options=post_data)
