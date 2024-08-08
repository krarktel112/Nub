"""import urllib.request"""
"""from selenium import webdriver"""
"""from selenium.webdriver.firefox.options import Options"""
"""from selenium.webdriver.firefox.service import Service"""
"""from selenium.webdriver.chrome.service import Service"""
"""from webdriver_manager.chrome import ChromeDriverManager"""
"""System.setProperty("webdriver.chrome.driver","driver-location/chromedriver.exe");"""

"""webUrl=urllib.request.urlopen('https://www.facebook.com/')"""
"""get_url = webdriver.current_url"""
"""print("The current url is:"+str(get_url))"""
"""htmldata=webUrl.read()"""
"""print("result: "+str(webUrl.getCode()))"""
"""print(htmldata)"""
"""print (y)"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs

from selenium import webdriver

driver = webdriver.Firefox(r'/non_root_user/Downloads/geckodriver')
driver.get("http://google.com/")
driver.quit()
