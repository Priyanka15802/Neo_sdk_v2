import json
from pickletools import uint1

from requests import session
from json import JSONDecodeError

from neo_api_client.urls import PROD_BASE_URL_GW_NAPI


class QrCodeAPI(object):

    def __init__(self, api_client):
        self.api_client = api_client
        # self.base64_token = api_client.configuration.bas8e64_token
        self.rest_client = api_client.rest_client
        self.totp_session = None

    def qr_code_get_link(self, ucc=None):
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}
        if self.api_client.configuration.base_url == PROD_BASE_URL_GW_NAPI:
            URL = self.api_client.configuration.get_url_details("qr_code_get_link_napi")
        else:
            URL = self.api_client.configuration.get_url_details("qr_code_get_link")
        query_params = {'id': ucc}
        qr_code_link = self.rest_client.request(
            url=URL, method='GET',
            headers=header_params,
            query_params=query_params
        )
        try:
            qr_code_link_data = qr_code_link.json()
        except JSONDecodeError:
            print("Received non-JSON response:", qr_code_link.text)
            return {
                "Error": "Unexpected response format. Expected JSON but received something else."
            }
        return qr_code_link_data

    def qr_code_generate_session(self, ott=None, ucc=None):
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token, 'neo-fin-key': self.api_client.configuration.get_neo_fin_key()}
        if self.api_client.configuration.base_url == PROD_BASE_URL_GW_NAPI:
            URL = self.api_client.configuration.get_url_details("qr_code_generate_session_napi")
        else:
            URL = self.api_client.configuration.get_url_details("qr_code_generate_session")
        body_params = {
            "ott": ott,
            "id": ucc
        }
        session = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        session_data = None
        if session.status_code == 200:
            session_data = session.json()
            self.api_client.configuration.edit_token = session_data.get("data").get("token")
            self.api_client.configuration.edit_sid = session_data.get("data").get("sid")
            self.api_client.configuration.edit_rid = session_data.get("data").get("rid")
            self.api_client.configuration.serverId = session_data.get("data").get("hsServerId")
            self.api_client.configuration.data_center = session_data.get("data").get("dataCenter")
        return session_data

