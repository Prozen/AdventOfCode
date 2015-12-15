import string
import re
chars = string.ascii_lowercase.replace('i','').replace('o','').replace('l','')
conseq = re.compile('|'.join([a+b+c for (a,b,c) in zip(string.ascii_lowercase, string.ascii_lowercase[1:], string.ascii_lowercase[2:])]))
def next(password):
    if password =="":
        return "a"
    elif password[-1]== 'z':
        return next(password[:-1]) + "a"
    else:
        return password[:-1] + chars[chars.find(password[-1])+1]
def good(password):
    if not conseq.search(password):
        return False
    if re.search(r"(.)\1.*(.)\2",password):
        return True
    return False
#print(good("ghjaabcc"))

password="cqjxxyzz"
password = next(password)
while not good(password):
    password = next(password)
print(password)
