import json
import logging

LOGGER = logging.getLogger(__name__)

class CriManagerConfiguration(object):

    DEFAULT_CONFIG_FILE = "etc/config.json"

    def __init__(self, filename=None, **kvargs):
        super(CriManagerConfiguration, self).__init__(**kvargs)
        self.filename = filename if filename != None else self.DEFAULT_CONFIG_FILE
        self.settings = None

    def load_configuration(self):
        try:
            with open(self.filename, "r") as cfgfile:
                LOGGER.info("loading configuration")  
                self.settings = json.load(cfgfile)
                LOGGER.info("configuration loaded")  
        except Exception as err:
            LOGGER.error("load configuration failed: {e}".format(e=err))
