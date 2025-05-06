import random
import string

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
        
        digit_wise = input("Did you want to add  digit to your password Y/N? ").lower()
        if digit_wise == "y":
            data_pick += string.digits
            break
        elif digit_wise == 'n':
             rethink = input("Caution! Digit makes passwword stronger. Are you sure you want to proceed Y/N ").lower()
             if rethink == 'y':
                  break
             else:
                  continue
             
while True:
     character_wise = input("Do you want add character to your password Y/N? ").lower()

     if character_wise == "y":
          data_pick += string.punctuation
          break 
     elif character_wise == 'n':
          rethink = input("Caution! character makes passwword stronger. Are you sure you want to proceed Y/N ").lower()
          if rethink == 'y':
               break
          else:
               continue

print(data_pick)