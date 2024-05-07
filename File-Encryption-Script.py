from cryptography.fernet import Fernet
import os

def gen_key():
    return Fernet.generate_key()

def load_key():
    return open("key.key", "rb").read()

def save_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def enc_file(filename, key):
    with open(filename, "rb") as file:
        file_data = file.read()
    enc_data = Fernet(key).encrypt(file_data)
    with open(filename + ".enc", "wb") as file:
        file.write(enc_data)
    os.remove(filename)

def dec_file(filename, key):
    with open(filename, "rb") as file:
        enc_data = file.read()
    dec_data = Fernet(key).decrypt(enc_data)
    with open(filename[:-4], "wb") as file:
        file.write(dec_data)
    os.remove(filename)

def enc_msg(message, key):
    enc_message = Fernet(key).encrypt(message.encode()).decode()
    print("Encrypted message:", enc_message)

def dec_msg(message, key):
    dec_message = Fernet(key).decrypt(message.encode()).decode()
    print("Decrypted message:", dec_message)

def main():
    mode = int(input("Select mode (1: Encrypt file, 2: Decrypt file, 3: Encrypt message, 4: Decrypt message): "))
    
    if mode in [1, 2]:
        file_path = input("Enter file path: ")
        if not os.path.exists(file_path):
            print("File not found.")
            return
        key = gen_key()
        save_key(key)
        if mode == 1:
            enc_file(file_path, key)
            print("Encrypted successfully.")
        else:
            dec_file(file_path, key)
            print("Decrypted successfully.")
        os.remove("key.key")
    
    elif mode in [3, 4]:
        key = load_key()
        if mode == 3:
            enc_msg(input("Message to encrypt: "), key)
        else:
            dec_msg(input("Enter encrypted message: "), key)

if __name__ == "__main__":
    main()
