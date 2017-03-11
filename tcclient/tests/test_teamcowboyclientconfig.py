from unittest import TestCase

import tcclient


class TestTeamCowboyClientConfig(TestCase):

    def test_obj_construction(self):
        # Arrange

        # Act
        tcc_config = tcclient.TeamCowboyClientConfig(config_file='')

        # Assert
        self.assertTrue(isinstance(tcc_config, tcclient.TeamCowboyClientConfig))
        self.assertIsNone(tcc_config.public_api_key)
        self.assertIsNone(tcc_config.private_api_key)

    def test_obj_construction_overrides(self):
        # Arrange
        test_public = 'test_public_api_key'
        test_private = 'test_private_api_key'

        # Act
        tcc_config = tcclient.TeamCowboyClientConfig(public_api_key=test_public, private_api_key=test_private)

        # Assert
        self.assertTrue(isinstance(tcc_config, tcclient.TeamCowboyClientConfig))
        self.assertEqual(tcc_config.public_api_key, test_public)
        self.assertEqual(tcc_config.private_api_key, test_private)
