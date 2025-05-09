import string
import secrets
import json

data_pick = string.ascii_letters

while True:
    try:
        password_length = int(input("Enter the length of password: "))
        if password_length < 12:
            print("Enter a Number greater than 11")
        else:
            break
    except ValueError:
        print("Enter a valid number")
    
while True:
        digit_wise = input("Did you want to add  digits to your password Y/N? ").lower()
        if digit_wise == "y":
            data_pick += string.digits
            break
        elif digit_wise == 'n':
             rethink = input("Caution! Digit makes password stronger. Are you sure you want to proceed Y/N ").lower()
             if rethink == 'y':
                  break
             else:
                  continue
             
while True:
     character_wise = input("Do you want add characters to your password Y/N? ").lower()
     if character_wise == "y":
          data_pick += string.punctuation
          break 
     elif character_wise == 'n':
          rethink = input("Caution! character makes password stronger. Are you sure you want to proceed Y/N ").lower()
          if rethink == 'y':
               break
          else:
               continue

pass_storage = ""
for x in range(password_length):
     pass_storage += secrets.choice(data_pick)


domain_name = input("Enter the domain you want to create password for: ")

password_domain_list = list()
password_dictionary = dict()

list_of_domain = ["DOMAIN NAME"]
list_of_password = ["PASSWORD"]


for i in list_of_domain:
     password_dictionary[i] = domain_name
for j in list_of_password:
     password_dictionary[j] = pass_storage

password_domain_list.append(password_dictionary)

with open("file1.json","r") as file:
     existing_data = json.load(file)
     existing_data.append(password_dictionary)

with open("file1.json", "w") as file:
     json.dump(existing_data,file)



