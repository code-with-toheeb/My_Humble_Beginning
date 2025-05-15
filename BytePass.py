import string
import secrets
import os
import json
import pyperclip

def get_password_length():
    while True:
        try:
            length = int(input("Enter the length of password"))
            
            if length < 12:
                print("Input a value more than 11")
            else:
                break
        except ValueError:
            print("Input a valid number")

    return length


def data_bank():
    data_bank = string.ascii_letters
    
    while True:
        d_wise = input("Do you want to insert digit to your password Y/N").lower()

        if d_wise == 'y':
            data_bank += string.digits
            break
        elif d_wise == 'n':
            rethink = input("Caution!Digit makes password stronger Are you sure you want to continue Y/N").lower()

            if rethink == 'y':
                break
            else:
                continue
     
    while True:
        p_wise = input("Do you want to insert punctuation to your password Y/N").lower()

        if p_wise == 'y':
            data_bank += string.punctuation
            break
        elif d_wise == 'n':
            rethink = input("Caution!Punctuation makes password stronger Are you sure you want to continue Y/N").lower()

            if rethink == 'y':
                break
            else:
                continue
    return data_bank


def pass_storage(length, character_pool):
    pass_storage = " "

    for i in range(length):
        pass_storage += secrets.choice(character_pool)

    return pass_storage


length = get_password_length()
character_pool = data_bank()

password = pass_storage(length, character_pool)

print("Your Secured Password is: ", password)


domain_name = input("Enter the domain you want to create password for: ")

password_domain_list = list()
password_dictionary = dict()


password_dictionary["DOMAIN_NAME"] = domain_name
password_dictionary["PASSWORD"] = pass_storage

filename = 'file1.json'


if not os.path.exists(filename) or os.path.getsize(filename) == 0:
     with open(filename, 'w') as file:
          json.dump([],file)



with open(filename,"r") as file:
     data = json.load(file)

data.append(password_dictionary)

with open(filename, "w") as file:
     json.dump(data, file, indent = 4)

pyperclip.copy(pass_storage)
pyperclip.paste()
print("Password File: ", )