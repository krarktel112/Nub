
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
    driver.get(https://www.facebook.com/login/identify/?ctx=recover&next=https%3A%2F%2Fwww.facebook.com%2Flogin%2Fidentify%2F%3Fctx%3Drecover%26ars%3Dfacebook_login%26from_login_screen%3D0&from_login_screen=0)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
