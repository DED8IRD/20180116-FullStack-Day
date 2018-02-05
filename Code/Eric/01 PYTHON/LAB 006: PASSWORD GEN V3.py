import random
import string

password = []
password_string = ""

print('\nWelcome to the password generator!\nI will help you generate a secure password consisting of numbers, '
      '\ncapital & lowercase letters, & punctuation characters! Now...')
numbers = input('\nhow many numbers would you like in your password?\n:')
for y in range(0, int(numbers)):
    pass_num = random.choice(string.digits)
    password.append(pass_num)
capitals = input('\nhow many capital letters would you like in your password?\n:')
for z in range(0, int(capitals)):
    caps_list = random.choice(string.ascii_uppercase)
    password.append(caps_list)
lowercase = input('\nand lower case letters?\n:')
for b in range(0, int(lowercase)):
    low_list = random.choice(string.ascii_lowercase)
    password.append(low_list)
punctuation = input('\nand lastly, how many punctuation characters would you like to use?\n:')
for a in range(0, int(punctuation)):
    punct_list = random.choice(string.punctuation)
    while punct_list == " " or punct_list == "\n":
        punct_list = random.choice(string.punctuation)
    password.append(punct_list)

random.shuffle(password)
for p in password:
    password_string = password_string + p

print('Okay! Your password is \n\n:' + '"' + password_string + '"' + '\nBe sure to keep it somewhere safe!')