import itertools
import sys
from time import sleep
from bs4 import BeautifulSoup
import requests
import mechanize
import os

os.system('clear')
f = open("6digits.txt", "a")
for combination in itertools.product(range(10), repeat=6):
    f.write(''.join(map(str, combination)))
print("done")
f.close()
z = open("8digits.txt", "a")
for combination in itertools.product(range(10), repeat=8):
    f.write(''.join(map(str, combination)))
z.close()
print("Done 2")
