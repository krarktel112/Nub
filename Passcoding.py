import itertools
import sys
import os

os.system('clear')
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
    for combination in itertools.product(range(10), repeat=6):
        z.write(''.join(map(str, combination)))
counter = 0
"""try:
    x = open("passing.txt", "a")
except:
x = open("passcoder.txt", "a+")
counter = int(0)
for combination in itertools.product(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","","X","Y","Z"], repeat=6):
    x.write(''.join(map(str, combination)))
    counter += 1
    print(int(counter), end='\r')"""
