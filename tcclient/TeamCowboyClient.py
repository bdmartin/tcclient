from .TeamCowboyClientConfig import TeamCowboyClientConfig
import hashlib
import random
import requests
import string
import time


class TeamCowboyClient:
    _url_insecure = 'http://api.teamcowboy.com/v1/'
    _url_secure = 'https://api.teamcowboy.com/v1/'

    def __init__(self, config=None):
        """
        Initialize the class
        """
        self.config = TeamCowboyClientConfig() if config is None else config
        if not isinstance(self.config, TeamCowboyClientConfig):
            raise Exception(
                'No valid configuration found! Config obj: %s' % (self.config)
            )

    def _build_url(self, method):
        """
        Create a dictionary with all of the necessary global parameters.
        """
        # Nonce value must be string of random numbers of length 8 or greater
        random_number = ''.join(
            random.SystemRandom().choice(string.digits) for _ in range(64)
        )
        url_dict = {
            'api_key': self.config.public_api_key,
            'method': method,
            'nonce': random_number,
            'timestamp': str(int(time.time())),
            'response_type': 'json',
        }

        return url_dict

    def _url_request(self, url, data='', m='get'):
        """
        Execute a url request.
        """
        headers = {}
        result = ''

        if m == 'get':
            url = requests.get(url, headers=headers)
        elif m == 'post':
            url = requests.post(url, data, headers=headers)

        result = url.json()

        return result

    def _create_url_string(self, url_dict):
        """
        Create a sorted url from the dictionary
        """
        url_string = ''
        for key in sorted(url_dict.keys()):
            url_string = '&'.join([
                url_string,
                '='.join([
                    key,
                    requests.utils.quote(url_dict[key])
                ])
            ])

        # Return with the first '&' ripped out
        return url_string[1:]

    def _create_sig(self, url_dict, request_type):
        private_api_key = self.config.private_api_key
        request_type = request_type.upper()

        url_string = self._create_url_string(url_dict).lower()
        sig_string = '|'.join([
            private_api_key,
            request_type,
            url_dict['method'],
            url_dict['timestamp'],
            url_dict['nonce'],
            url_string
        ])

        # create the hash
        h = hashlib.sha1(sig_string.encode('utf-8')).hexdigest()

        # save it
        url_dict['sig'] = h

        return url_dict

    def test_getrequest(self, test_param=None):
        """
        This is a very basic testing method for checking that you are able to
        call the Team Cowboy API via a HTTP GET.
        """
        url_dict = self._build_url('Test_GetRequest')

        if test_param is not None:
            url_dict['testParam'] = test_param

        # create the sig
        self._create_sig(url_dict, 'GET')

        request = self._create_url_string(url_dict)

        url = TeamCowboyClient._url_insecure + '?' + request
        res = self._url_request(url)
        return res
