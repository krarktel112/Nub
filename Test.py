from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

def driver(request):
    """Set up webdriver fixture."""
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path="firefox.geckodriver")
    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.get("https://www.facebook.com/login/web/?email=amschwab%40comcast.net&is_from_lara=1")
    driver.implicitly_wait(10)
    login_box = find_element(By.NAME, 'tryanotherway')
    login_box.click()

    yield driver
    driver.quit()
print ("Done")
input('Press anything to quit')
print("Finished")
