from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from enum import Enum
 
class BrowserType(Enum):
    Chrome = 'chrome'
    Firefox = 'firefox'

class Common():
    def openBrowser(self, browserType = BrowserType.Chrome):
        driver = None
        if browserType == BrowserType.Chrome:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browserType == BrowserType.Firefox:
            driver = webdriver.Firefox(GeckoDriverManager().install())
        driver.maximize_window()
        return driver