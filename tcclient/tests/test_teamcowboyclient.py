from unittest import TestCase

import tcclient
import json
import pprint


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
        self.assertIn('api_key', url_dict)
        self.assertIn('method', url_dict)
        self.assertIn('nonce', url_dict)
        self.assertIn('timestamp', url_dict)
        self.assertIn('response_type', url_dict)

        method = url_dict['method']
        self.assertIs(test_method_name, method)
        self.assertEqual(test_method_name, method)

    def test_url_request(self):
        # Arrange
        tcc = tcclient.TeamCowboyClient()
        test_url = 'https://api.github.com/users/bdmartin/repos'

        # Act
        response = tcc._url_request(test_url)

        # Assert
        # print(json.dumps(response, indent=2, sort_keys=True))
        self.assertIsNotNone(response)

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
        self.assertIsNotNone(response)
        self.assertIsInstance(response, basestring)
        self.assertEquals(expected_string, response)

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
        self.assertIsNotNone(response)
        self.assertIsInstance(response, basestring)
        self.assertEquals(expected_string, response)

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
        self.assertIsNotNone(first_response)
        self.assertIn('sig', test_dict)
        self.assertIn('timestamp', test_dict)
        self.assertIn('method', test_dict)
        self.assertIn('nonce', test_dict)

        # Arrange
        test_request_type = 'get'

        # Act
        second_response = tcc._create_sig(test_dict, test_request_type)

        # Assert
        # print(pprint.pformat(second_response))
        self.assertIsNotNone(second_response)
        self.assertIn('sig', test_dict)
        self.assertIn('timestamp', test_dict)
        self.assertIn('method', test_dict)
        self.assertIn('nonce', test_dict)
        self.assertEquals(first_response['sig'], second_response['sig'])

    def test_test_get_request(self):
        # Arrange
        tcc = tcclient.TeamCowboyClient()

        # Act
        response = tcc.test_getrequest()

        # Assert
        print(pprint.pformat(response))
        self.assertIsNotNone(response)
