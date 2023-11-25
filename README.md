# Password Manager Project - Object Oriented Programming

![Password Manager Logic](https://github.com/infinity-set/oop_password_manager/assets/142350896/ac4af845-5451-4aee-97fb-0c6b17e96a1a)

## Table of Contents

- [Project Overview](#project-overview)
  - [Non-OOP Version](#non-oop-version)
- [Object-Oriented Programming (OOP) Components](#object-oriented-programming-oop-components)
  - [PasswordManagerUI](#1-passwordmanagerui)
  - [PasswordGenerator](#2-passwordgenerator)
  - [PasswordSaver](#3-passwordsaver)
  - [PasswordSearcher](#4-passwordsearcher)
- [Languages and Utilities Used](#languages-and-utilities-used)
- [Environments Used](#environments-used)
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
<br>

## Project Overview

The Password Manager Project is an Object-Oriented Programming (OOP) version of the project already posted on GitHub. This version maintains the same functionality and features as the original project but achieves them through OOP principles, resulting in a more structured and maintainable codebase.

### Non-OOP Version

If you're interested in the non-OOP version of the Password Manager Project, you can find it on GitHub at the following link:

[Password Manager GUI (Non-OOP Version)](https://github.com/infinity-set/password_manager)

This non-OOP version provides the same password management capabilities but is implemented without the use of OOP principles.
<br><br>

## Object-Oriented Programming (OOP) Components

The project leverages OOP principles to create a structured and maintainable codebase. Here are the main OOP components in the project:
<br><br>

### 1. PasswordManagerUI

- **Summary**: The `PasswordManagerUI` class represents the graphical user interface (GUI) of the application. It encapsulates the UI elements and interactions, providing an abstracted interface for user interaction.

### 2. PasswordGenerator

- **Summary**: The `PasswordGenerator` class encapsulates the functionality for generating random passwords. It abstracts the password generation process, making it reusable and easy to use in various parts of the application.

### 3. PasswordSaver

- **Summary**: The `PasswordSaver` class manages the saving of password data in different formats, such as CSV, text files, and JSON. It demonstrates polymorphism by dynamically calling different save functions based on the selected format, providing an abstracted way to handle data storage.

### 4. PasswordSearcher

- **Summary**: The `PasswordSearcher` class handles the search for website information and loading passwords from a JSON file. It abstracts the search process and uses encapsulation to manage data retrieval and presentation.
<br>

## Languages and Utilities Used

- **Python**
- **PyCharm**

[<img align="center" alt="PyCharm Icon" width="50px" src="https://upload.wikimedia.org/wikipedia/commons/1/1d/PyCharm_Icon.svg" />][pycharm]
[<img align="left" alt="Python Icon" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" />][python]

[pycharm]: https://www.jetbrains.com/pycharm/
[python]: https://www.python.org/

## Environments Used

- **Windows**

[<img align="left" alt="Microsoft Icon" width="35px" src="https://upload.wikimedia.org/wikipedia/commons/3/34/Windows_logo_-_2012_derivative.svg" />][windows]

[windows]: https://www.microsoft.com/
<br /><br />


## Dependencies

The Password Manager application relies on the following Python libraries:

- **Tkinter:** Tkinter is the standard GUI library that comes bundled with Python. It provides the necessary tools to create graphical user interfaces for desktop applications.

- **datetime:** The datetime module is used for working with dates and times. It's used in the application to generate timestamps for saved entries.

- **pandas:** The pandas library is used to work with data in tabular form. It's used to create and manage data in CSV format.

- **os:** The os module provides a way to interact with the operating system. In the application, it's used to check if files exist before saving data.

- **random:** The random module is used to generate random values, such as generating random characters for passwords.

- **pyperclip:** The pyperclip library allows copying and pasting text to and from the clipboard. It's used to copy generated passwords to the clipboard for user convenience.

- **json:** The json module is used to work with JSON (JavaScript Object Notation) data. In the application, it's used to load and save password data in JSON format.

- **sys:** The sys module provides access to some variables used or maintained by the Python interpreter. It's used to gracefully exit the program when the user chooses to quit.
<br>

## Getting Started

To run the Password Manager Project on your local machine, follow these steps:

1. Clone the repository to your computer.
2. Install any required dependencies mentioned in the project documentation.
3. Run the main `password_manager_ui.py` application script.

#
<br>

⬅️ **[Home](https://github.com/infinity-set)**

