#!/usr/bin/env python3

import logging


# Only log messages at level "INFO" or higher
logging.basicConfig(level=logging.WARNING)


logger = logging.getLogger(__name__)
logger.info('Start reading database')
logger.error('End reading database')
