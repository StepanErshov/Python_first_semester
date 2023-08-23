#generate password

import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '@#$%^&*/\?!'

user_for = lower_case + upper_case + number + symbols
lenght_for_pass = 12

password = ''.join(random.sample(user_for, lenght_for_pass))

print('Your generated password is :',password)