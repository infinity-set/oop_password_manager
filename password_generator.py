# Import the 'random' module and the 'Tkinter' library for generating passwords and creating GUI
import random as r
from tkinter import *

# Define the 'PasswordGenerator' class
class PasswordGenerator:
    def __init__(self):
        pass  # There are no attributes to initialize

    # Method for generating a random password
    def generate_password(self, password_entry):
        # Check if the input password entry is empty, if so then proceed
        if len(password_entry.get()) == 0:
            # Define character sets for letters, numbers, and symbols
            letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '0123456789'
            symbols = '!#$%&()*+'

            # Generate a random password by selecting characters from the sets
            password_list = [r.choice(letters) for _ in range(r.randint(8, 10))]
            password_list += [r.choice(symbols) for _ in range(r.randint(2, 4))]
            password_list += [r.choice(numbers) for _ in range(r.randint(2, 4))]

            # Shuffle the characters to create a more random password
            r.shuffle(password_list)
            password = "".join(password_list)

            # Insert the generated password into the password entry field
            password_entry.insert(0, string=password)
        else:
            # If the password entry is not empty, clear it and generate a new password
            password_entry.delete(0, END)
            self.generate_password(password_entry)
