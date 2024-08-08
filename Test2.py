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

ser = Service(r"/data/data/com.turmux/files/home/chromedriver.exe")
"""driver = webdriver.Chrome(service=ser)"""

driver.get("https://www.google.com")

get_url = driver.current_url

print("The current url is:"+str(get_url))

#Redirect
val = input("Enter a url: ")
wait = WebDriverWait(driver, 10)
driver.get(val)
wait.until(EC.url_to_be(val))
page_source = driver.page_source

soup = BeautifulSoup(page_source,features="html.parser")
title = soup.title.text
file=codecs.open('article_titles.txt', 'a+')
file.write(title+"\n")
file.close()

get_url = driver.current_url 
print("The current url is:"+str(get_url))

val = input("Enter a url: ")
wait = WebDriverWait(driver, 10)
driver.get(val)
wait.until(EC.url_to_be(val))
page_source = driver.page_source
soup2 = BeautifulSoup(page_source,features="html.parser")
title = soup2.title.text
file=codecs.open('article_titles.txt', 'a+')
file.write(str(title)+"\n")
file.close()

get_url = driver.current_url 
print("The current url is:"+str(get_url))
driver.quit()
