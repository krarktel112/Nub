import itertools
import sys
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
z = open("passing.txt", "a")
for combination in itertools.product([0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]), repeat=6):
    z.write(''.join(map(str, combination)))
z.close()
