from .cri_manager_config import CriManagerConfiguration

import json
import docker
import random
import logging
import functools

LOGGER = logging.getLogger(__name__)


class CriManager(object):

    def __init__(self, config=CriManagerConfiguration(), **kvargs):
        super(CriManager, self).__init__(**kvargs)
        self.config = config if config != None else CriManagerConfiguration()
        self.config.load_configuration()

    def start(self):
        LOGGER.info('Starting manager')
