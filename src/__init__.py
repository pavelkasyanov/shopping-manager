import logging
from logging.handlers import TimedRotatingFileHandler

import os

#log_file_name = os.path.abspath(os.path.dirname(__file__)) + '/../my_log.log'

#handler = TimedRotatingFileHandler(log_file_name, when='D')
#formatter = logging.Formatter(u'%(asctime)s %(levelname)-8s %(message)s')
#handler.setFormatter(formatter)
#handler.suffix = "%Y-%m-%d"

logger = logging.getLogger()
#logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
