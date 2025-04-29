
# Secret Communication Tool

## Overview
This project is an old project I created while learning Python. It's a simple encryption and decryption tool built with Python and Tkinter. The tool uses base64 encoding to encrypt messages, and you can decrypt them using the same key. It's an introduction to basic cryptography and GUI development in Python.

## Key Features
- **Message Encryption**: Encrypt any message by combining it with a user-defined key.
- **Message Decryption**: Decrypt the encrypted message by using the same key.
- **Base64 Encoding**: Uses Python’s `base64` library for encoding and decoding.
- **Simple GUI**: Built with **Tkinter** for a user-friendly interface.

## Why Build a Secret Communication Tool?
- **Simple Encryption**: This app demonstrates how to encrypt and decrypt messages using a custom key, making it useful for educational purposes in cryptography.
- **Learning Project**: The tool helped me practice Python basics, especially handling user input and working with base64 encoding.
- **GUI Development**: Gained experience in building graphical interfaces using Tkinter.

## How It Works
1. **Message Encryption**: The user inputs a message and a key. The tool combines both and encodes them into a base64 string.
2. **Message Decryption**: The user can input the encrypted message and the same key to decode and retrieve the original message.
3. **Feedback**: If the key matches, the original message is displayed; if not, an error message is shown.

## Code Walkthrough
### Imports and Setup
```python
from tkinter import *
import base64
```
- **tkinter**: Used to create the GUI.
- **base64**: Encodes and decodes messages for encryption and decryption.

### Main Functions
- **encrypt_message()**: Encrypts the user's input message by combining it with a key and base64 encoding.
- **decrypt_message()**: Decrypts the encrypted message using the same key.
- **load_question()**: Displays the current question and options.
- **check_answer()**: Checks the user's answer and updates the score.

### GUI Layout
```python
root = Tk()
root.title("Encryption & Decryption Tool")
root.geometry('500x400')
```
- Initializes the main window with the title "Encryption & Decryption Tool" and a defined size.

### Button Setup
```python
Button(root, text="Encrypt Message", font=("Arial", 12), command=encrypt_message, bg="#4CAF50", fg="white").grid(row=3, column=0, columnspan=2, pady=10)
Button(root, text="Decrypt Message", font=("Arial", 12), command=decrypt_message, bg="#2196F3", fg="white").grid(row=7, column=0, columnspan=2, pady=10)
```
- Creates buttons for both encryption and decryption functionalities.

## How to Run
1. **Save the code**: Copy the code above into a Python file, e.g., `secret_communication_tool.py`.
2. **Run the program**:
   ```bash
   python secret_communication_tool.py
   ```
3. **Use the GUI**:
   - Enter a message and a key to encrypt.
   - Enter the encrypted message and the same key to decrypt.

## Example Scenarios
### Scenario 1:
- **Message**: "Hello, World!"
- **Key**: "secretkey"
- **Encrypted Message**: `SGVsbG8sIFdvcmxkIQ==` (Base64 encoded)

### Scenario 2:
- **Encrypted Message**: `SGVsbG8sIFdvcmxkIQ==`
- **Key**: "secretkey"
- **Decrypted Message**: "Hello, World!"

## Screenshot
![Secret Communication Tool Screenshot](https://github.com/IstiakIqbal/Secret-Communication-Tool/blob/main/Secret%20communication.png?raw=true)

## What You'll Learn
- **Basic Cryptography**: Learn how to encode and decode messages using base64 encryption.
- **GUI Development**: Using Tkinter to build interactive user interfaces.
- **String Manipulation**: Handling and manipulating strings in Python for encoding and decoding.
