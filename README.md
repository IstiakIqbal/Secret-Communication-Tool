# Secret Communication Tool

## About
This project is an old project I created while learning Python. It's a simple encryption and decryption tool built with Python and Tkinter. The tool uses base64 encoding to encrypt messages, and you can decrypt them using the same key. It's an introduction to basic cryptography and GUI development in Python.

### Features:
- **Message Encryption:** Encrypt any message by combining it with a user-defined key.
- **Message Decryption:** Decrypt the encrypted message by using the same key.
- **Base64 Encoding:** Uses Python’s `base64` library for encoding and decoding.
- **Simple GUI:** Built with **Tkinter** for a user-friendly interface.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/IstiakIqbal/Secret-Communication-Tool.git
Install dependencies (Tkinter comes pre-installed with Python, so no extra dependencies are needed).

Run the program:

bash
Copy
Edit
python encryption_tool.py
How to Use:
Enter the message you want to encrypt in the "Enter Message" field.

Enter a key that will be used to encrypt and decrypt the message.

Click the Encrypt Message button to generate the encrypted message.

Copy the encrypted message and paste it into the "Enter Encrypted Message" field.

Click the Decrypt Message button to decrypt the message using the same key.

Example:
Message: "Hello, World!"

Key: "secretkey"

Encrypted Message: SGVsbG8sIFdvcmxkIQ== (Base64 encoded)

Contribution
This project is a personal learning project, but feel free to fork it and contribute to improvements or enhancements. Any pull requests or feedback are welcome.
