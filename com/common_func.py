from configuration.config import BROWSER_TYPE, EXECUTABLE_PATH, TEST_URL
from utility.logs_utility import configure_logging
from selenium import webdriver
import logging

configure_logging()
logger = logging.getLogger(__name__)

# @pytest.fixture(scope="function")
class BrowserManager:

    def __init__(self):
        self.browser_type = BROWSER_TYPE
        self.executable_path = EXECUTABLE_PATH
        self.driver = None
 
    def start_browser(self):
        self.logger = logging.getLogger(__name__)
        self.driver = webdriver.Chrome() #if self.browser_type == "chrome" else webdriver.Firefox(executable_path=self.executable_path)
        logger.info(f"Starting {BROWSER_TYPE} browser.")
        return self.driver
    
    def close_browser(self):
        if self.driver:
            self.driver.close()

    def open_url(self, url):
        if self.driver:
            self.driver.get(url)
    
    def get_title(self):
        if self.driver:
            return self.driver.title
    
