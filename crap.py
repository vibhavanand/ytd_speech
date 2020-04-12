import random
import string

def abc():
    c=''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
    print(c)

abc()

def string1():
    return "aaa"

print(string1())