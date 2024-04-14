import random
import secrets
import string

# Define the possible characters for the random number
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

b = random.choice(all_characters)
#print(a)
#print(b)

y = secrets.choice(all_characters)
#print(y)

count = 0
while count < 150:
    c = secrets.choice(all_characters)
    print('随机数字是：', c)
    if c == 'A':
        print(f'循环了{count}次')
        break
    count += 1
else:
    print(f'循环了{count}次')
 
