

#!/usr/bin/env python
# CY83R-3X71NC710N Copyright 2023

# Importing necessary libraries
import hashlib
import os
import sys
import getpass
import base64

# Function to generate a secure key
def generate_key(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return base64.b64encode(salt + key)

# Function to encrypt data
def encrypt_data(data, key):
    encrypted_data = hashlib.sha256(data.encode('utf-8') + key).hexdigest()
    return encrypted_data

# Function to decrypt data
def decrypt_data(data, key):
    decrypted_data = hashlib.sha256(data.encode('utf-8') + key).hexdigest()
    return decrypted_data

# Main function
def main():
    # Prompt user for password
    password = getpass.getpass("Please enter a password: ")
    # Generate a secure key
    key = generate_key(password)
    # Prompt user for data
    data = input("Please enter the data you would like to store: ")
    # Encrypt the data
    encrypted_data = encrypt_data(data, key)
    # Print the encrypted data
    print("Your encrypted data is: " + encrypted_data)
    # Prompt user for data to decrypt
    data_to_decrypt = input("Please enter the data you would like to decrypt: ")
    # Decrypt the data
    decrypted_data = decrypt_data(data_to_decrypt, key)
    # Print the decrypted data
    print("Your decrypted data is: " + decrypted_data)

# Run the main function
if __name__ == "__main__":
    main()
