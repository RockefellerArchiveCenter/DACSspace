from configparser import ConfigParser
from os.path import isfile

from asnake.aspace import ASpace


class ASnakeConfigError(Exception):
    pass


class ArchivesSpaceClient:
    """Handles communication with ArchivesSpace."""

    def __init__(self):
        config_filepath = "dacsspace/local_settings.cfg"
        if not isfile("dacsspace/local_settings.cfg"):
            raise IOError(
                "Could not find a configuration file at {}".format(config_filepath))
        config = ConfigParser()
        config.read(config_filepath)
        self.aspace = ASpace(baseurl=config.get('ArchivesSpace', 'baseurl'),
                             username=config.get('ArchivesSpace', 'user'),
                             password=config.get('ArchivesSpace', 'password'))
        self.repo = self.aspace.repositories(
            config.get('ArchivesSpace', 'repository'))
        if isinstance(self.repo, dict):
            raise ASnakeConfigError(
                "Error getting repository: {}".format(
                    self.repo.get("error")))

    def get_resources(self, published_only):
        """Returns data about resource records from AS.
        Args:
          published_only (boolean): Fetch only published records from AS
        Returns:
          resources (list): Full JSON of AS resource records
        """
        if published_only:
            search_query = "publish:true AND primary_type:resource"
        else:
            search_query = "primary_type:resource"
        for resource in self.repo.search.with_params(q=search_query):
            resource_json = resource.json()
            yield resource_json
