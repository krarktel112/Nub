from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')
browser.get('https://www.twitter.com')
