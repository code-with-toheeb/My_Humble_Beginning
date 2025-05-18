import string
import secrets
import os
import json


domain_name = input("Enter the domain you want to create password for: ")
filename = input("Enter filename: ")

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



def pass_storage(length, character_pool):
    pass_storage = " "

    for i in range(length):
        pass_storage += secrets.choice(character_pool)

    return pass_storage

length = get_password_length()
data_bank = string.ascii_letters + string.digits + string.punctuation
password = pass_storage(length, data_bank)


def send_to_file():
    global password
    global domain_name
    global filename

    password_dictionary = dict()

    password_dictionary["DOMAIN NAME"] = domain_name
    password_dictionary["PASSWORD"] = password

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        with open(filename, "w") as file:
            json.dump([], file)

    with open(filename, "r") as file:
        data = json.load(file)
    
    data.append(password_dictionary)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


send_to_file()