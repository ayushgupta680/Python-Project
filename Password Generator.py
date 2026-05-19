import random
import string

length = int(input("Enter the length:"))


lower = random.choice(string.ascii_lowercase)
upper = random.choice(string.ascii_uppercase)
digit = random.choice(string.digits)
symbol = random.choice(string.punctuation)


all_chars = string.ascii_letters + string.digits + string.punctuation
remaining = ""


for i in range(length - 4):
    remaining += random.choice(all_chars)

password = lower + upper + digit + symbol + remaining

password_list = list(password)
random.shuffle(password_list)

final_password = "".join(password_list)

print("Strong password:", final_password)