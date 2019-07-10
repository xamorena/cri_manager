import json
import logging

LOGGER = logging.getLogger(__name__)

class CriManagerConfiguration(object):

    def __init__(self, **kvargs):
        super(CriManagerConfiguration, self).__init__(**kvargs)

    def load(self):
        LOGGER.info('Loading configuration')
