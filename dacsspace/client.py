#!/usr/bin/env python3

import argparse
from configparser import ConfigParser
from asnake.aspace import ASpace

#published_only = False

class ArchivesSpaceClient:
    """Handles communication with ArchivesSpace."""

    def __init__(self):
        config = ConfigParser()
        config.read("local_settings.cfg")
        self.aspace = ASpace(baseurl=config.get('ArchivesSpace', 'baseURL'),
                             username=config.get('ArchivesSpace', 'user'),
                             password=config.get('ArchivesSpace', 'password'))
        self.repo = self.aspace.repositories(config.get('ArchivesSpace', 'repository'))

    def get_resources(self, published_only):
        """Returns data about resource records from AS.
        Args:
          published_only (boolean): Fetch only published records from AS
        Returns:
          resources (list): Full JSON of AS resource records
        """
        if published_only is True:
            for resource in self.repo.search.with_params(q='publish:true AND primary_type:resource'):
                resource_json = resource.json()
            return resource_json
        else:
            for resource in self.repo.search.with_params(q='primary_type:resource'):
                resource_json = resource.json()
            return resource_json

                #return resource.publish
                         #return resource_json
        #return resource.publish

        #build in tests

#ArchivesSpaceClient().get_resources(published_only)
