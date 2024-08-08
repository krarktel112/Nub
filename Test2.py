import urllib.request
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

webUrl=urllib.request.urlopen('https://www.facebook.com/')

htmldata=webUrl.read()
"""print("result: "+str(webUrl.getCode()))"""
print(htmldata)
