import os
from logging import INFO, basicConfig, getLogger

basicConfig(level=os.getenv('LOG_LEVEL'.upper(), INFO))
logger = getLogger(__name__)
