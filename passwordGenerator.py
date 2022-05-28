import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers ="0123456789"
symbols = "!@#$%&*<>"

def passwordGenerator():
    strings = lower + upper + numbers + symbols
    length = 12 # length is the length of the password
    password = "".join(random.sample(strings,length))
    return password

if __name__ == '__main__':
    print('The generated 12 digit password is ',passwordGenerator())
