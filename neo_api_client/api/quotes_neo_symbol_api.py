import urllib.parse
from json import JSONDecodeError

from neo_api_client.urls import PROD_BASE_URL_GW_NAPI


class QuotesAPI(object):

    def __init__(self, api_client):
        self.api_client = api_client
        # self.base64_token = api_client.configuration.base64_token
        self.rest_client = api_client.rest_client

    def get_quotes(self, instrument_tokens=None, quote_type=None):
        if not quote_type:
            quote_type = 'all'
        neo_symbol_str = ",".join(f"{item['exchange_segment']}|{item['instrument_token']}" for item in instrument_tokens)
        encoded_neo_symbol_str = urllib.parse.quote(neo_symbol_str)
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}
        if self.api_client.configuration.base_url == PROD_BASE_URL_GW_NAPI:
            URL = self.api_client.configuration.get_url_details("quotes_neo_symbol_napi")
        else:
            URL = self.api_client.configuration.get_url_details("quotes_neo_symbol")
        URL = URL.format(neo_symbols=encoded_neo_symbol_str, quote_type=quote_type)
        quotes = self.rest_client.request(
            url=URL, method='GET',
            headers=header_params
        )
        try:
            quotes_data = quotes.json()
        except JSONDecodeError:
            print("Received non-JSON response:", quotes.text)
            return {
                "Error": "Unexpected response format. Expected JSON but received something else."
            }
        return quotes_data