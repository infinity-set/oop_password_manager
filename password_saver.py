# Import necessary modules
import pandas as pd  # For working with data in tabular format
import os  # For interacting with the operating system
import json  # For working with JSON data
from tkinter import messagebox, END  # Import the tkinter library for building the GUI


# Define the 'PasswordSaver'
class PasswordSaver:
    def __init__(self):
        pass  # There are no attributes to initialize

    # Method for saving password data
    def save(self, website, username, email, password, timestamp_string):

        # Get the text value from the input fields
        self.website = website.get().title()
        self.username = username.get()
        self.email = email.get()
        self.password = password.get()

        # Check if input fields (website, email, password, username) are not empty
        if len(self.website) > 0 and len(self.email) > 0 and len(self.password) > 0 and len(self.username) > 0:
            # Define a list of save functions along with their format names
            save_functions = [
                (self.save_to_csv, "CSV"),
                (self.save_to_json, "JSON"),
                (self.save_to_text_file, "TEXT")
            ]

            # Initialize a status variable to track success or failure of save operations
            status = True

            try:
                # Iterate through the list of save functions
                for save_function, format_name in save_functions:
                    try:
                        # Call the appropriate save function for each format
                        save_function(self.website, self.username, self.email, self.password, timestamp_string)
                    except:
                        # Handle exceptions that may occur during saving and show a warning message
                        messagebox.showwarning(title="Warning", message=f"Could not save {format_name}.")
                        status = False
                    else:
                        # Print a success message on the terminal
                        print(f"Saved {format_name}...\n")

            except:
                # Handle exceptions that may occur during the iteration through save functions
                messagebox.showinfo(title="Incomplete", message="An error occurred while processing your request.")
            else:
                # Check the overall status of save operations
                if status:
                    # Show a success message and clear input fields
                    messagebox.showinfo(title="Complete", message="Files are updated.")
                    self.clear_input_fields(website, email, password, username)
                else:
                    # Show an incomplete message if not all files were updated
                    messagebox.showinfo(title="Incomplete", message="Not all files were updated.")

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

    def clear_input_fields(self, website, email, password, username):
        # Delete the content of the input fields using their indexes
        website.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)
        username.delete(0, END)
