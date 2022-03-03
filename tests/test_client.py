import shutil
import unittest
from unittest.mock import patch

# from dacsspace.client import ArchivesSpaceClient


class ArchivesSpaceClient(unittest.TestCase):
    def setUp(self):
        shutil.copy("dacsspace/local_settings.example", "dacsspace/local_settings.cfg")
        pass

    @patch("requests.get")
    @patch("requests.post")
    def test_configfile(self, mock_post, mock_get):
        """check for config file
        config file is found - proceed
        config file is not found - error message saying that config file is not there, does not have sections"""
        # ArchivesSpaceClient()
        pass

    def test_connection(self):
        """check connection to AS
        connection is ok - proceed with no errors
        connection fails - test for incorrect authentication (password), incorrect baseURL, incorrect repository - specific error message"""
        pass

    def test_published_only(self):
        """check published_only argument is correct
        test with_params method on both sides"""
        pass

    def test_data(self):
        """check getting correct data
        test data type (dict)
        test getting back resources"""
        pass

# check for config file
# check connection to AS
# check published_only argument is correct
# check that getting right data back
