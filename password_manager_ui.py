# Import necessary modules
from tkinter import *  # Import the tkinter library for building the GUI
import datetime as date  # Import the datetime module for working with dates and times
import pyperclip  # Import pyperclip for clipboard operations
from password_saver import PasswordSaver  # Import PasswordSaver class from a custom module
from password_searcher import PasswordSearcher  # Import PasswordSearcher class from a custom module
from password_generator import PasswordGenerator  # Import PasswordGenerator class from a custom module

# Define the PasswordManagerUI class
class PasswordManagerUI:
    def __init__(self, root):
        # Initialize the main window and create instances of helper classes
        self.root = root
        self.password_saver = PasswordSaver()  # Initialize the PasswordSaver class for saving passwords
        self.password_searcher = PasswordSearcher()  # Initialize the PasswordSearcher class for searching passwords
        self.password_generator = PasswordGenerator()  # Initialize the PasswordGenerator class for generating passwords
        root.title("Password Manager")  # Set the title of the main window
        root.minsize(width=420, height=440)  # Set the minimum window size
        root.config(padx=20, pady=20, bg="black")  # Set padding and background color
        # Create the UI elements
        self.create_ui()

    def create_ui(self):
        # Create a canvas for displaying the logo image
        self.canvas = Canvas(width=210, height=220, bg="black", highlightthickness=0, highlightbackground="black")
        self.lock_img = PhotoImage(file="logo.png")
        self.canvas.create_image(125, 110, image=self.lock_img)
        self.canvas.grid(column=1, row=0)  # Place the canvas in the grid

        # Create labels, entry fields, and buttons for various UI elements

        # Website Label and Entry
        self.website_label = Label(text="Website:", fg="white", bg="red", highlightthickness=1, highlightbackground="white")
        self.website_label.grid(column=0, row=1, pady=1)  # Place the label in the grid
        self.website_entry = Entry(width=31, highlightthickness=1, highlightbackground="black")
        self.website_entry.grid(padx=20, column=1, row=1)  # Place the entry field in the grid

        # Search Button
        self.search_button = Button(text="Search", width=16, font=("Arial", 9, "bold"), fg="white", bg="red",
        command=self.search_website) # Call the "search_website" function when "Search" button is clicked
        self.search_button.grid(column=2, row=1)  # Place the button in the grid

        # Username Label and Entry
        self.user_name_label = Label(text="Username:", fg="white", bg="red", highlightthickness=1, highlightbackground="white")
        self.user_name_label.grid(column=0, row=2, pady=10) # Place the label in the grid
        self.username_entry = Entry(width=55, highlightthickness=1, highlightbackground="black")
        self.username_entry.grid(column=1, row=2, columnspan=2) # Place the entry field in the grid

        # Email Label and Entry
        self.email_username_label = Label(text="Email:", fg="white", bg="red", highlightthickness=1, highlightbackground="white")
        self.email_username_label.grid(column=0, row=3) # Place the label in the grid
        self.email_entry = Entry(width=55, highlightthickness=1, highlightbackground="black")
        self.email_entry.grid(column=1, row=3, columnspan=2) # Place the entry field in the grid

        # Password Label and Entry
        self.password_label = Label(text="Password: ", fg="white", bg="red", highlightthickness=1, highlightbackground="white")
        self.password_label.grid(column=0, row=4, pady=10) # Place the label in the grid
        self.password_entry = Entry(width=31, highlightthickness=1, highlightbackground="black")
        self.password_entry.grid(column=1, row=4) # Place the entry field in the grid

        # Generate Password Button
        self.generate_button = Button(text="Generate Password", font=("Arial", 9, "bold"), fg="white", bg="red",
        command=self.generate_password) # Call the "generate_password" function when "Generate Password" button is clicked
        self.generate_button.grid(column=2, row=4, padx=10) # Place the button in the grid

        # Add Button
        self.add_button = Button(padx=8, text="Add", font=("Arial", 9, "bold"), width=46, fg="white", bg="red",
        command=self.save)  # Call the "save" function when "Add" button is clicked
        self.add_button.grid(column=1, row=5, columnspan=2) # Place the button in the grid

        # Exit Button
        self.exit_button = Button(padx=8, text="EXIT", font=("Arial", 9, "bold"), width=46, fg="white", bg="red",
        command=self.exit_program)  # Call the "exit_program" function when the "EXIT" button is clicked
        self.exit_button.grid(column=1, row=6, columnspan=2, pady=20) # Place the button in the grid

    def search_website(self):
        # Get the entered website name from the entry field and convert the input to title case
        website_name = self.website_entry.get().title()

        # Call the search_website method from PasswordSearcher class
        self.password_searcher.search_website(website_name)

    def generate_password(self):
        # Call the generate_password method from PasswordGenerator class
        self.password_generator.generate_password(self.password_entry)

    def save(self):
        # Get the current date and time
        todays_date = date.datetime.now()

        # Convert the date and time to a formatted string (e.g., "Jan-01-2023")
        timestamp_string = todays_date.strftime("%b-%d-%Y")

        # Get the text values from the Entry widgets
        website = self.website_entry.get().title()
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Call the save method from PasswordSaver class
        self.password_saver.save(website, username, email, password, timestamp_string)

    def clear_input_fields(self):
        # Delete the content of the input fields using their indexes
        self.website_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.username_entry.delete(0, END)

    def exit_program(self):
        # Quit the Tkinter application, effectively closing the GUI window
        self.root.quit()



# Verify if the script is running as the main program
if __name__ == "__main__":
    # Create a Tkinter window instance named 'window' to serve as the GUI base
    window = Tk()

    # Initialize the 'PasswordManagerUI' class and create an instance named 'app' to set up the user interface
    app = PasswordManagerUI(window)

    # Establish a connection that enables the 'clear_input_fields' function in the 'PasswordManagerUI' class
    # to be invoked from the 'save' function within the 'PasswordSaver' class without encountering errors.
    password_saver = PasswordSaver(app)
    app.password_saver = password_saver

    # Begin the Tkinter event loop, allowing the GUI to remain responsive to user interactions
    window.mainloop()
