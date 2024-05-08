from cryptography.fernet import Fernet
import os

# Generate an encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt data using the key
def encrypt_data(data, key):
    cipher = Fernet(key)
    return cipher.encrypt(data)

# Decrypt data using the key
def decrypt_data(data, key):
    cipher = Fernet(key)
    return cipher.decrypt(data)

# Recursively encrypt a folder
def encrypt_folder(folder_path, key):
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'rb') as file:
                data = file.read()
            encrypted_data = encrypt_data(data, key)
            with open(file_path + '.encrypted', 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

# Recursively decrypt a folder
def decrypt_folder(folder_path, key):
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith('.encrypted'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'rb') as file:
                    encrypted_data = file.read()
                decrypted_data = decrypt_data(encrypted_data, key)
                with open(file_path[:-10], 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)

    # Encrypt a folder
    encrypt_folder('folder_to_encrypt', key)

    # Decrypt a folder
    decrypt_folder('folder_to_decrypt', key)
