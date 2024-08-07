from selenium import webdriver
 
#headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
 
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")
 
print(driver.title)
 
driver.quit()
