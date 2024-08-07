from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

usr=input('Enter Email Id:') 
pwd=input('Enter Password:')

def driver(request):
    """Set up webdriver fixture."""
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path="firefox.geckodriver")
    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.get('https://www.facebook.com/')
    print ("Opened facebook")
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/login/web/?email=amschwab%40comcast.net&is_from_lara=1")
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/recover/initiate/?ars=facebook_login&is_from_lara_screen=1")
    driver.implicitly_wait(10)
    login_box = find_element(By.NAME, 'continue')
    login_box.click()

    yield driver
    driver.quit()
print ("Done")
input('Press anything to quit')
print("Finished")
