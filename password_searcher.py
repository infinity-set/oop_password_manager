# Import necessary modules
from tkinter import messagebox  # For displaying message boxes in the GUI
import pyperclip  # For clipboard operations
import json  # For working with JSON data

# Define the 'PasswordSearcher' class
class PasswordSearcher:
    def __init__(self):
        # Initialize method; no necessary attributes to initialize
        pass

    # Method for searching for website information in a provided dictionary
    def search_website(self, website_name):
        # Load password data from the JSON file
        search_dict = self.load_passwords_from_json("./json_passwords.json")
        if search_dict == {}:
            return # Return early if the search dictionary is empty

        if len(website_name) == 0:
            return  # Return if the website name is empty

        if website_name in search_dict:
            # Retrieve information for the found website
            web_info = search_dict[website_name]
            email = web_info.get("email", "N/A")  # Get email or set to "N/A" if not found
            username = web_info.get("username", "N/A")  # Get username or set to "N/A" if not found
            password = web_info.get("password", "N/A")  # Get password or set to "N/A" if not found

            # Copy the password to the clipboard
            pyperclip.copy(password)

            # Prepare a message with the website information
            message = (
                f"Website: {website_name}\n"
                f"Username: {username}\n"
                f"Email: {email}\n"
                f"Password: {password}\n\n"
            )

            # Show an information message box with the search result
            messagebox.showinfo(title="Search Result", message=message)
        else:
            # Show an information message box if the website is not found in the dictionary
            messagebox.showinfo(title="Search Result", message=f"No entry found for '{website_name}'.")

    # Method for loading passwords from a JSON file
    def load_passwords_from_json(self, file_path):
        try:
            # Attempt to open and read the JSON file
            with open(file_path) as json_data:
                return json.load(json_data)  # Load the JSON data and return it
        except FileNotFoundError:
            # Handle the case when the file is not found and show an information message
            messagebox.showinfo(title="Search Result", message="No password file found.")
            return {}  # Return an empty dictionary
        except json.JSONDecodeError:
            # Handle the case when the JSON data is corrupt or improperly formatted
            messagebox.showinfo(title="Search Result", message="Data file is corrupt or improperly formatted.")
            return {}  # Return an empty dictionary
