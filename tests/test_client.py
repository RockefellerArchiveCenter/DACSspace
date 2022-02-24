import unittest
import argparse
from configparser import ConfigParser
from asnake.aspace import ASpace
from dacsspace.client import ArchivesSpaceClient


class ArchivesSpaceClient(unittest.TestCase):
    def test_client(self):
        result = ArchivesSpaceClient().get_resources(args.published_only)
        self.assertTrue(isinstance(result, list))
