import random
""" This program generates a ramdom password with the length of 8.
    Each time the program is run, a different password will be generated.
The password will include:
2 uppercase letters from A to Z,
2 lowercase letters from a to z,
2 digits from 0 to 9,
2 punctuation signs such as !, ?, “, # etc.
"""

print("This program will generate a random password with the length of 8.\n")

# for uppercase letters ascii code is between 65 and 90 (both inclusive)
# we will use the chr() function to convert ascii code to letters
uppercase1 = chr(random.randint(65, 90))
uppercase2 = chr(random.randint(65, 90))

# for lowercase letters ascii code is between 97 and 122 (both inclusive)
lowercase1 = chr(random.randint(97, 122))
lowercase2 = chr(random.randint(97, 122))

# for digits
digit1 = str(random.randint(0, 9))
digit2 = str(random.randint(0, 9))

# for punctuation ascii code is between 33 to 47
punctuation1 = chr(random.randint(33, 47))
punctuation2 = chr(random.randint(33, 47))

password = uppercase1 + uppercase2 + lowercase1 + lowercase2 
password += digit1 + digit2 + punctuation1 + punctuation2

password_list = []

for i in password:
    password_list.append(i)

random.shuffle(password_list)

random_password = ""
for i in password_list:
    random_password += i

print(f"Randomly generated password is: {random_password}\n")
