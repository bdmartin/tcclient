import ConfigParser
import logging
import os.path


class TeamCowboyClientConfig:

    def __init__(self, config_file='tcclient.ini', public_api_key=None, private_api_key=None):
        """
        Initialize the client configuration file.
        """
        log = logging.getLogger(__name__)

        self.public_api_key = None
        self.private_api_key = None

        if os.path.isfile(config_file):
            config = ConfigParser.ConfigParser()
            config.read(config_file)
            log.debug('Config sections: %s', config.sections())
        else:
            log.warn('No client config file found at %s.' % (config_file))

        # Override config with explicit parameters
        if public_api_key is not None:
            self.public_api_key = public_api_key

        if private_api_key is not None:
            self.private_api_key = private_api_key
