from selenium import webdriver
 
#headless mode
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = Service(executable_path="firefox.geckodriver")
driver = webdriver.Firefox(options=options, service=service)
