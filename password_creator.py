import random
import string
import re

number = input('How many passwords?')
input_number = int(number)

def create_pass():
    random_password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(12)])
    return random_password

def isAllPresent(str):
    regex = ("^(?=.*[a-z])(?=." + "*[A-Z])(?=.*\\d)" + "(?=.*[-+_!@#$%^&*., ?]).+$")
    p = re.compile(regex)
    if (re.search(p, str)):
        return True
    else:
        return False


with open('my_passwords.txt', mode='w') as f:
    f.write('Here are your passwords.\n')


def saving_pass(rand_pass):
    with open('my_passwords.txt', mode='a') as f:
        f.write(rand_pass + '\n')


while input_number>0:
    rand_pass = create_pass()
    if isAllPresent(rand_pass) == True:
        pass_list = saving_pass(rand_pass)
        input_number = input_number - 1


with open('my_passwords.txt', mode='r') as  f:
    print(f.read())