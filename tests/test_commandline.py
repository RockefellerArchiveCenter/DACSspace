import os
from unittest import TestCase


class CommandLineTest(TestCase):

    def test_command_line(self):
        """Ensures command line interface does not contain typos."""
        exit_status = os.system('dacsspace --help')
        assert exit_status == 0
