from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_text(text):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text):
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    return decrypted_text.decode()

# Example usage
text_to_encrypt = "Hello, World!"
encrypted_text = encrypt_text(text_to_encrypt)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt_text(encrypted_text)
print("Decrypted:", decrypted_text)
