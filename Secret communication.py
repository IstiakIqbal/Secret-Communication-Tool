from tkinter import *
import base64

def encrypt_message():
    message = entry_message.get()
    key = entry_key.get()
    combined = (message + key).encode('utf-8')
    encrypted = base64.b64encode(combined).decode('utf-8')
    entry_encrypted.delete(0, END)  # Clear previous content
    entry_encrypted.insert(0, encrypted)
    label_copy_instruction.config(text="Copy this and paste below")

def decrypt_message():
    encrypted = entry_encrypted.get()
    key = entry_key.get()
    try:
        decoded = base64.b64decode(encrypted).decode('utf-8')
        if decoded.endswith(key):
            message = decoded[:-len(key)]
            label_decrypted.config(text=f'Decrypted Message: {message}')
        else:
            label_decrypted.config(text="Error: Key doesn't match")
    except Exception:
        label_decrypted.config(text="Error: Invalid input")

root = Tk()
root.title("Encryption & Decryption Tool")
root.geometry('500x400')
root.config(padx=20, pady=20)

Label(root, text="Message Encryption & Decryption", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

Label(root, text="Enter Message:", font=("Arial", 12)).grid(row=1, column=0, sticky=W, pady=5)
entry_message = Entry(root, font=("Arial", 12), width=40)
entry_message.grid(row=1, column=1, pady=5)

Label(root, text="Enter Key:", font=("Arial", 12)).grid(row=2, column=0, sticky=W, pady=5)
entry_key = Entry(root, font=("Arial", 12), width=40)
entry_key.grid(row=2, column=1, pady=5)

Button(root, text="Encrypt Message", font=("Arial", 12), command=encrypt_message, bg="#4CAF50", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

Label(root, text="Encrypted Message:", font=("Arial", 12)).grid(row=4, column=0, sticky=W, pady=5)
entry_encrypted = Entry(root, font=("Arial", 12), width=40)
entry_encrypted.grid(row=4, column=1, pady=5)

label_copy_instruction = Label(root, text="", font=("Arial", 10, "italic"), fg="gray")
label_copy_instruction.grid(row=5, column=0, columnspan=2, pady=5)

Label(root, text="Enter Encrypted Message:", font=("Arial", 12)).grid(row=6, column=0, sticky=W, pady=5)
entry_encryption = Entry(root, font=("Arial", 12), width=40)
entry_encryption.grid(row=6, column=1, pady=5)

Button(root, text="Decrypt Message", font=("Arial", 12), command=decrypt_message, bg="#2196F3", fg="white").grid(row=7, column=0, columnspan=2, pady=10)
label_decrypted = Label(root, text="Decrypted Message:", font=("Arial", 12))
label_decrypted.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
