import urllib.request
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
WebDriver driver=new ChromeDriver():

webUrl=urllib.request.urlopen('https://www.facebook.com/')

htmldata=webUrl.read()
"""print("result: "+str(webUrl.getCode()))"""
print(htmldata)
