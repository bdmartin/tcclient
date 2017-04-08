try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
import logging
import os.path


class TeamCowboyClientConfig:

    def __init__(self,
                 config_file=None,
                 public_api_key=None,
                 private_api_key=None):
        """
        Initialize the client configuration file.
        This reads in config from '~/tcclient.ini
        """
        # Set the defaults
        self.public_api_key = None
        self.private_api_key = None

        # Parse config file if specified, else fall back
        if config_file is not None:
            self._parse_config_file(config_file)
        else:
            config_filename = 'tcclient.ini'

            # Read from home directory first
            home_config = os.path.sep.join(
                [os.path.expanduser('~'), config_filename]
            )
            self._parse_config_file(home_config)

            # Override from the local directory
            local_config = config_filename
            self._parse_config_file(local_config)

        # Override config with explicit parameters
        if public_api_key is not None:
            self.public_api_key = public_api_key

        if private_api_key is not None:
            self.private_api_key = private_api_key

    def _parse_config_file(self, config_file=None):
        """
        Helper function to parse a config file.
        This will overwrite any existing variables if necessary.
        """
        log = logging.getLogger(__name__)

        if os.path.isfile(config_file):
            config = ConfigParser()
            config.read(config_file)
            log.debug('Config sections: %s', config.sections())

            public_key = config.get('Default', 'public_api_key')
            if public_key is not None:
                self.public_api_key = public_key
            private_key = config.get('Default', 'private_api_key')
            if private_key is not None:
                self.private_api_key = private_key
        else:
            log.warn('No client config file found at %s.' % (config_file))
