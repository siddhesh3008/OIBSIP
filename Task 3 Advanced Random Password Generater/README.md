# Advanced Password Generator

An advanced password generator application with a graphical user interface (GUI) built using **Tkinter**. This project allows users to generate secure and customizable passwords with features like clipboard integration, security rules, and user-friendly customization options.

## Features

- **Password Complexity Options**: 
  - Include uppercase letters, numbers, and symbols.
  - Customizable password length.
- **Security Rules**: Ensures strong passwords by including at least one character of each selected type.
- **Clipboard Integration**: One-click to copy the generated password to the clipboard.
- **User-Friendly GUI**: Built using **Tkinter** for a simple and intuitive interface.
- **Modular Design**: Password generation logic is separate from the GUI for better maintainability.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [File Structure](#file-structure)
4. [Examples](#examples)
5. [Dependencies](#dependencies)
6. [Enhancements](#enhancements)
   
---

## Installation

### Prerequisites

- Python 3.7 or higher installed on your system.
- Libraries: `pyperclip` for clipboard functionality.

### Steps

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/PasswordGeneratorApp.git
    cd PasswordGeneratorApp
    ```

2. Install the required library:
    ```bash
    pip install pyperclip
    ```

3. Run the application:
    ```bash
    python main.py
    ```

---

## Usage

1. Open the application by running `main.py`.
2. Enter the desired password length (minimum 4 characters).
3. Select options for including uppercase letters, numbers, and symbols.
4. Click **Generate Password** to create a password.
5. Use the **Copy to Clipboard** button to copy the password.

---

## File Structure

PasswordGeneratorApp/ ├── generator.py # Password generation logic ├── main.py # GUI code ├── requirements.txt # Dependencies (optional) └── README.md # Project documentation

---

## Examples

### Default Settings

- **Length**: 12 characters
- **Options**: Uppercase, Numbers, Symbols enabled.

Example output:
Password: d8f3g2a1

---

## Dependencies

- **Python Libraries**:
  - `random` (built-in): For random character generation.
  - `string` (built-in): Provides character sets.
  - `pyperclip`: Clipboard functionality.
  - `tkinter` (built-in): GUI development.

## Enhancements

### Consider adding the following features:

- Save generated passwords to a file.
- Add a password strength meter for visual feedback.
- Include a dark mode toggle for better user experience.

  ---
