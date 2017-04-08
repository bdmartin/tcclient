# from builtins import str
from past.builtins import basestring
from unittest import TestCase
import pprint
import tcclient


class TestTeamCowboyClient(TestCase):

    def test_obj_construction(self):
        # Arrange

        # Act
        tcc = tcclient.TeamCowboyClient()

        # Assert
        self.assertTrue(isinstance(tcc, tcclient.TeamCowboyClient))

    def test_build_url(self):
        # Arrange
        tcc = tcclient.TeamCowboyClient()
        test_method_name = 'test_method'

        # Act
        url_dict = tcc._build_url(test_method_name)

        # Assert
        self.assertTrue('api_key' in url_dict)
        self.assertTrue('method' in url_dict)
        self.assertTrue('nonce' in url_dict)
        self.assertTrue('timestamp' in url_dict)
        self.assertTrue('response_type' in url_dict)

        method = url_dict['method']
        self.assertTrue(test_method_name is method)
        self.assertEqual(test_method_name, method)

    def test_url_request(self):
        # Arrange
        tcc = tcclient.TeamCowboyClient()
        test_url = 'https://api.github.com/users/bdmartin/repos'

        # Act
        response = tcc._url_request(test_url)

        # Assert
        self.assertTrue(response is not None)

    def test_create_url_string_basic(self):
        # Arrange
        tcc = tcclient.TeamCowboyClient()
        test_key = 'test_key'
        test_value = 'test_value'
        test_dict = {test_key: test_value}
        expected_string = test_key + '=' + test_value

        # Act
        response = tcc._create_url_string(test_dict)

        # Assert
        self.assertTrue(response is not None)
        print(type(response))
        self.assertTrue(isinstance(response, basestring))
        self.assertEqual(expected_string, response)

    def test_create_url_string_order(self):
        # Arrange
        tcc = tcclient.TeamCowboyClient()
        test_dict = {
            'c': 'c',
            'a': 'a',
            'b': 'b',
        }
        expected_string = 'a=a&b=b&c=c'

        # Act
        response = tcc._create_url_string(test_dict)

        # Assert
        self.assertTrue(response is not None)
        print(type(response))
        self.assertTrue(isinstance(response, basestring))
        self.assertEqual(expected_string, response)

    def test_create_sig(self):
        # Arrange
        tcc = tcclient.TeamCowboyClient()
        test_dict = {
            'method': 'c',
            'timestamp': 'a',
            'nonce': 'b',
        }
        test_request_type = 'GET'

        # Act
        first_response = tcc._create_sig(test_dict, test_request_type)

        # Assert
        # print(pprint.pformat(first_response))
        self.assertTrue(first_response is not None)
        self.assertTrue('sig' in test_dict)
        self.assertTrue('timestamp' in test_dict)
        self.assertTrue('method' in test_dict)
        self.assertTrue('nonce' in test_dict)

        # Arrange
        test_request_type = 'get'

        # Act
        second_response = tcc._create_sig(test_dict, test_request_type)

        # Assert
        # print(pprint.pformat(second_response))
        self.assertTrue(second_response is not None)
        self.assertTrue('sig' in test_dict)
        self.assertTrue('timestamp' in test_dict)
        self.assertTrue('method' in test_dict)
        self.assertTrue('nonce' in test_dict)
        self.assertEqual(first_response['sig'], second_response['sig'])

    def test_test_get_request(self):
        # Arrange
        tcc = tcclient.TeamCowboyClient()

        # Act
        response = tcc.test_getrequest()

        # Assert
        print(pprint.pformat(response))
        self.assertTrue(response is not None)
