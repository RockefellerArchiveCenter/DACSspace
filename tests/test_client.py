import os
import shutil
import unittest
from unittest.mock import Mock, patch

from dacsspace.client import ArchivesSpaceClient


class ArchivesSpaceClientTests(unittest.TestCase):
    def setUp(self):
        """Move existing config file and replace with sample config."""
        if os.path.isfile("dacsspace/local_settings.cfg"):
            shutil.move("dacsspace/local_settings.cfg", "dacsspace/local_settings.old")
        shutil.copy("dacsspace/local_settings.example", "dacsspace/local_settings.cfg")

    @patch("requests.get")
    @patch("requests.post")
    def test_config_file(self, mock_post, mock_get):
        """Asserts that configuration files are correctly handled:
            - Missing configuration files cause an exception to be raised.
            - Configuration files without all the necessary values cause an exception to be raised.
            - Valid configuration file allows for successful instantiation of ArchivesSpaceClient class.
        """
    #    ArchivesSpaceClient()

    @patch("requests.Session.get")
    @patch("requests.Session.post")
    def test_connection(self, mock_post, mock_get):
        """Asserts that ArchivesSpace connection is correctly handled:
            - Incorrect authentication details should cause an exception to be raised.
            - An incorrect base URL for the AS instance should cause an exception to be raised.
            - An identifier which points to a non-existent AS repository should cause an exception to be raised.
            - Valid connection details should allow for successful instantiation of the ArchivesSpaceClient class.
        """
        # Incorrect authentication credentials
        with self.assertRaises(Exception, msg="Incorrect authentication credentials"):
            mock_post.return_value.status_code = 403

        # Incorrect base URL
        with self.assertRaises(Exception, msg="Incorrect base URL"):
            mock_post.return_value.status_code = 404

        # Incorrect repository
        with self.assertRaises(Exception, msg="Incorrect repository"):
            mock_post.return_value.status_code = 200
            mock_post.return_value.text = "{\"session\": \"12355\"}"
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = "v3.0.2"
            mock_get.return_value.json.return_value = {'error': 'Repository not found'}
        ArchivesSpaceClient()

    @patch("asnake.client.web_client.ASnakeClient.get.return_value.json.return_value.search.with_params")
    @patch("asnake.client.web_client.ASnakeClient.get")
    @patch("asnake.client.web_client.ASnakeClient.authorize")
    def test_published_only(self, mock_authorize, mock_get, mock_search):
        """Asserts that the `published_only` flag is handled correctly."""
        mock_get.return_value.text = "v3.0.2"  # Allows ArchivesSpaceClient to instantiate
        client = ArchivesSpaceClient()  # Instantiates ArchivesSpaceClient for testing

        # Test search for only published resources
        list(client.get_resources(True))
        self.assertEqual(mock_search.call_count, 1)
        mock_search.assert_called_with(q='publish:true AND primary_type:resource')
        mock_search.reset_mock()

        # Test search for all resources
        list(client.get_resources(False))
        self.assertEqual(mock_search.call_count, 1)
        mock_search.assert_called_with(q='primary_type:resource')

    @patch("asnake.client.web_client.ASnakeClient.get.return_value.json.return_value.search.with_params")
    @patch("asnake.client.web_client.ASnakeClient.get")
    @patch("asnake.client.web_client.ASnakeClient.authorize")
    def test_data(self, mock_authorize, mock_get, mock_search):
        """Asserts that individual resources are returned"""
        mock_get.return_value.text = "v3.0.2"
        client = ArchivesSpaceClient()

        # create a mocked object which acts like an `asnake.jsonmodel.JSONModel` object
        mock_resource = Mock()
        expected_return = {"jsonmodel_type": "resource"}
        mock_resource.json.return_value = expected_return
        mock_search.return_value = [mock_resource]

        result = list(client.get_resources(True))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], expected_return)

    def tearDown(self):
        """Replace sample config with existing config."""
        if os.path.isfile("dacsspace/local_settings.old"):
            shutil.move("dacsspace/local_settings.old", "dacsspace/local_settings.cfg")
