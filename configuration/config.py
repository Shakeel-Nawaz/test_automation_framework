import os

CUR_DIR = os.getcwd()
BROWSER_TYPE = 'Chrome'
TEST_URL = ''
PROD_URL = ''
EXECUTABLE_PATH = os.path.join(CUR_DIR,'configuration','chromedriver.exe') 
MAIN_LOG_PATH = os.path.join(CUR_DIR, 'logs', 'main.log')