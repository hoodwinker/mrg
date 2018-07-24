from selenium import webdriver
import platform
 
class SeleniumWrapper:
  _instance = None
 
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
    return cls._instance
 
  def initialize(self, host="https://dev.host.com/"):

    if platform.system().startswith('Win'):
        self.driver = webdriver.Chrome('C:\Dev\chromedriver.exe')
    else:
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    self.base_url = host
    self.driver.get(self.base_url)
    return self.driver