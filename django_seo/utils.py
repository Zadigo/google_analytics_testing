import requests
from urllib.parse import urlencode


class GetAddress:
    """Verify that an address actually exists"""
    api_url = 'https://api-adresse.data.gouv.fr/search'

    def __init__(self, addressline, zip_code=None):
        self.errors = []
        self.response = {}
        url = self.get_url(q=addressline, postcode=zip_code)
        try:
            response = requests.get(url)
        except:
            pass
        else:
            if response.ok:
                try:
                    self.response = response.json()
                except:
                    pass

    def get_url(self, **kwargs):
        return f'{self.api_url}?{urlencode(kwargs)}'
