import yaml
import logging
import logging.config


_file = 'loggers.conf.yml'

with open(_file, 'rt') as fo:
    _config = yaml.safe_load(fo)

logging.config.dictConfig(_config)

log_to_file = logging.getLogger('to_file')
log_to_console = logging.getLogger('to_console')
