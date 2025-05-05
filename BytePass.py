import random
import string

user_input1 = int(input("Enter the length of password"))
user_input2 = str(input("Symbols? choose Y/N")).lower()
user_input3 = str(input("Digits? choose Y/N")).lower()
data_used = list(string.ascii_letters)
sorted_data = []

if user_input2 == "y":
    data_used += string.punctuation
if user_input3 == "y":
    data_used += string.digits

for x in range(0, user_input1):
    sorted_data.append(random.choice(data_used))
    

print("Password Generated: ","".join(sorted_data))