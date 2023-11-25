# Import necessary modules
import pandas as pd  # For working with data in tabular format
import os  # For interacting with the operating system
import json  # For working with JSON data
from tkinter import messagebox  # For displaying message boxes in the GUI

# Define the 'PasswordSaver' class
class PasswordSaver:
    # Set up requirements in order to call the "clear_input_fields" method from "main"
    def __init__(self, password_manager_ui=None):  # Accept PasswordManagerUI instance as an argument
        self.password_manager_ui = password_manager_ui  # Store the reference to PasswordManagerUI


    # Method for saving password data
    def save(self, website, username, email, password, timestamp_string):
        if len(website) > 0 and len(email) > 0 and len(password) > 0 and len(username) > 0:
            # List of save functions along with their format names
            save_functions = [
                (self.save_to_csv, "CSV"),
                (self.save_to_text_file, "TEXT"),
                (self.save_to_json, "JSON")
            ]
            for save_function, format_name in save_functions:
                try:
                    # Call the appropriate save function for each format
                    save_function(website, username, email, password, timestamp_string)
                    print(f"Saved {format_name}...\n")
                except:
                    # Handle issues that may occur while saving and show a warning message
                    messagebox.showwarning(title="Warning", message=f"Could not save {format_name}.")
                # Clear input fields and show a success message
            self.password_manager_ui.clear_input_fields()  # Call the clear_input_fields method from "main"
            messagebox.showinfo(title="Complete", message="Files are updated.")
        else:
            # Show an error message if any input field is empty
            messagebox.showerror(title="Error", message="You cannot have empty fields.")
            return

    # Method for saving data to a CSV file
    def save_to_csv(self, website, username, email, password, timestamp_string):
        data = {
            "Website": [website],
            "Username": [username],
            "Email": [email],
            "Password": [password],
            "Date Created": [timestamp_string]
        }

        # Create a DataFrame from the 'data' dictionary containing password information
        password_dataframe = pd.DataFrame(data)

        # Determine the file write mode based on whether 'password_doc.csv' exists
        mode = "a" if os.path.isfile("password_doc.csv") else "w"

        # Write the DataFrame to a CSV file named 'password_doc.csv'
        # Use the determined 'mode' for appending or overwriting
        # Set 'header' to 'True' if the file is newly created, else 'False' to avoid writing the header again
        password_dataframe.to_csv("password_doc.csv", mode=mode, header=not os.path.isfile("password_doc.csv"))

    # Method for saving data to a text file
    def save_to_text_file(self, website, username, email, password, timestamp_string):
        with open("./data.txt", mode="a") as f:
            entry = (
                f"Website: {website}  ~  Username: {username}  ~  Email: {email}  ~   Password:|START|>{password}<|FINISH|  ~  Date Created: {timestamp_string}\n\n"
            )

            f.write(entry)

    # Method for saving data to a JSON file
    def save_to_json(self, website, username, email, password, timestamp_string):
        new_data = {
            website: {
                "username": username,
                "email": email,
                "password": password,
                "date": timestamp_string
            }
        }

        try:
            # Try to open an existing JSON file
            with open("./json_passwords.json", mode="r") as json_file:
                contents = json.load(json_file)
        except FileNotFoundError:
            # If the file doesn't exist, create a new one and write the data
            with open("./json_passwords.json", mode="w") as json_file:
                json.dump(new_data, json_file, indent=4)
        else:
            # If the file exists, update its contents with new data
            contents.update(new_data)
            with open("./json_passwords.json", mode="w") as json_file:
                json.dump(contents, json_file, indent=4)
