from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Make sure it is .exe file
PATH = (r"C:/Users/deepa/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
service = Service(executable_path=PATH) 
driver = webdriver.Chrome(service=service)

# Open a website
driver.get('https://www.wikipedia.com')

# Close the browser
driver.quit()
