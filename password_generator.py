'''
This code generates a strong password based on user input for length.
The length of the password must be at least 8 characters.
The password is composed of 30% uppercase characters, 30% lowercase characters,
20% digits, and 20% special characters.
'''

import string, random

# Create lists of lowercase, uppercase, digits, and special characters
lower = list(string.ascii_lowercase)    # a list of lowercase characters
upper = list(string.ascii_uppercase)    # a list of uppercase characters
digits = list(string.digits)            # a list of digits from 0 to 9
special = list(string.punctuation)      # a list of special characters like !, @, #

# Shuffle all lists to ensure randomness in selection
random.shuffle(lower)   
random.shuffle(upper)
random.shuffle(digits)
random.shuffle(special)

# Prompt the user for the desired password length
length = input("Make sure the length of password you enter is at least 8 characters.\n\
Please enter the length of password in numbers: ")

# Input validation loop to ensure the user enters a valid number and length is at least 8
while True:
    try:
        length = int(length)  # Convert the input to integer
        if length < 8:  # Check if the entered length is less than 8
            print("Length of password must be at least 8 characters.")
            length = input("Please enter the length of the password again: ")
        else:
            break  # Exit the loop if the length is valid
    except:  # Catch ValueError for invalid number input
        print('Length of password must be entered in numbers only.')
        length = input("Please enter the length of the password again: ")

# Calculate the number of characters from each category based on the given percentages
letters_part = round(length * 0.3)  # 30% for uppercase and lowercase letters
digit_special_part = round(length * 0.2)  # 20% for digits and special characters

password = []  # Initialize an empty list to store the password characters

# Add the calculated number of lowercase and uppercase characters to the password
for i in range(letters_part):
    password.append(lower[i % len(lower)])  # Use modulus to avoid index out of range
    password.append(upper[i % len(upper)])  # Use modulus to avoid index out of range

# Add the calculated number of digits and special characters to the password
for j in range(digit_special_part):
    password.append(digits[j % len(digits)])    # Use modulus to avoid index out of range
    password.append(special[j % len(special)])  # Use modulus to avoid index out of range

# Shuffle the password list randomly for extra randomness
for k in range(random.randint(10, 50)):
    random.shuffle(password)

# Convert the password list into a string to display
password = "".join(password)

# Output the final generated password
print(f"Your password is: {password}")