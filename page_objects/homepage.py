from com.common_func import BrowserManager
from configuration.config import TEST_URL

class HomePageObject:
    def __init__(self, driver=None, url=TEST_URL):
        self.driver = BrowserManager()
        self.url = url
        if self.driver:
            self.driver.start_browser()
            self.driver.open_url(self.url)