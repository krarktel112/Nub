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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time
import re
from datetime import datetime

  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--enable-javascript') # 启用 JavaScript
options.add_argument('blink-settings=imagesEnabled=false')      # 不加载图片，提升运行速度
options.add_argument('--no-sandbox')                # 解决DevToolsActivePort文件不存在的报错
options.add_argument('--disable-gpu')               # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--hide-scrollbars')           # 隐藏滚动条，应对一些特殊页面
options.add_argument("--headless") #无界面



urls = [
    'https://www.gettyimages.com/photos/people?assettype=image&page=1&phrase=Fashion&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=1&phrase=Actor&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=1&phrase=Concert&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=1&phrase=Music&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=1&phrase=Celebrities&recency=last24hours&sort=newest',
  
    'https://www.gettyimages.com/photos/people?assettype=image&page=2&phrase=Fashion&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=2&phrase=Actor&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=2&phrase=Concert&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=2&phrase=Music&recency=last24hours&sort=newest',

    'https://www.gettyimages.com/photos/people?assettype=image&page=3&phrase=Fashion&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=3&phrase=Actor&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=3&phrase=Concert&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=3&phrase=Music&recency=last24hours&sort=newest', 
    'https://www.gettyimages.com/photos/people?assettype=image&page=3&phrase=Celebrities&recency=last24hours&sort=newest',

    'https://www.gettyimages.com/photos/people?assettype=image&page=4&phrase=Fashion&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=4&phrase=Actor&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=4&phrase=Concert&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=4&phrase=Music&recency=last24hours&sort=newest', 
    'https://www.gettyimages.com/photos/people?assettype=image&page=4&phrase=Celebrities&recency=last24hours&sort=newest',
  
    'https://www.gettyimages.com/photos/people?assettype=image&page=5&phrase=Fashion&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=5&phrase=Actor&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=5&phrase=Concert&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=5&phrase=Music&recency=last24hours&sort=newest', 
    'https://www.gettyimages.com/photos/people?assettype=image&page=5&phrase=Celebrities&recency=last24hours&sort=newest',
  
    'https://www.gettyimages.com/photos/people?assettype=image&page=6&phrase=Fashion&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=6&phrase=Actor&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=6&phrase=Concert&recency=last24hours&sort=newest',
    'https://www.gettyimages.com/photos/people?assettype=image&page=6&phrase=Music&recency=last24hours&sort=newest', 
    'https://www.gettyimages.com/photos/people?assettype=image&page=6&phrase=Celebrities&recency=last24hours&sort=newest',
]

# create an empty list to store the HTML sources
html_sources = []


# iterate over the URLs and get the HTML source
for url in urls:
  try:
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(20)
        driver.get(url)
        time.sleep(6)
        html = driver.page_source
        html_sources.append(html)
        driver.quit()
        print(f"Got HTML for URL: {url}")
   finally
