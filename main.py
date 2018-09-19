import random
import string

def genRandString():
    charList = []
    for chr in range(0,12):
        chr = random.choice(string.printable)
        charList.append(chr)
    str = ''.join(charList)
    return str

print (genRandString())