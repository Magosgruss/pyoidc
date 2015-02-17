import json
import urllib
import requests
from oic.oauth2 import NoClientInfoReceivedError


class MDQClient(object):
    def __init__(self, url):
        self.url = url

    def __getitem__(self, item):
        mdx_url = "{}/entities/{}".format(self.url, urllib.quote(item, safe=''))
        response = requests.request("GET", mdx_url, headers={'Accept': 'application/json',
                                                             'Accept-Encoding': 'gzip'})
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise NoClientInfoReceivedError("{} {}".format(response.status_code,
                                                           response.reason))