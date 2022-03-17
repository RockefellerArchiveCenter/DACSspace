from configparser import ConfigParser

from asnake.aspace import ASpace


class ASnakeConfigError(Exception):
    pass


class ArchivesSpaceClient:
    """Handles communication with ArchivesSpace."""

    def __init__(self):
        config = ConfigParser()
        config.read("dacsspace/local_settings.cfg")
        self.aspace = ASpace(baseurl=config.get('ArchivesSpace', 'baseURL'),
                             username=config.get('ArchivesSpace', 'user'),
                             password=config.get('ArchivesSpace', 'password'))
        self.repo = self.aspace.repositories(config.get('ArchivesSpace', 'repository'))
        if isinstance(self.repo, dict):
            raise ASnakeConfigError("Error getting repository: {}".format(self.repo.get("error")))

    def get_resources(self, published_only):
        """Returns data about resource records from AS.
        Args:
          published_only (boolean): Fetch only published records from AS
        Returns:
          resources (list): Full JSON of AS resource records
        """
        if published_only is True:
            repo_params_search = self.repo.search.with_params(q='publish:true AND primary_type:resource')
        else:
            repo_params_search = self.repo.search.with_params(q='primary_type:resource')
        for resource in repo_params_search:
            resource_json = resource.json()
            yield resource_json
