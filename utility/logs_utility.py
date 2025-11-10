import logging
from configuration.config import MAIN_LOG_PATH

def configure_logging():
    logging.basicConfig(filename=MAIN_LOG_PATH,
                        level=logging.INFO,
                        format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s')