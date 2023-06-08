from cryptography.fernet import Fernet

# Encryption and decryption functions
def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password)
    return decrypted_password.decode()

# Password Keeper class
class PasswordKeeper:
    def __init__(self):
        self.passwords = {}
        self.key = Fernet.generate_key()

    def add_password(self, website, username, password):
        encrypted_password = encrypt_password(password, self.key)
        self.passwords[website] = {
            'username': username,
            'password': encrypted_password
        }

    def update_password(self, website, password):
        if website in self.passwords:
            encrypted_password = encrypt_password(password, self.key)
            self.passwords[website]['password'] = encrypted_password

    def delete_password(self, website):
        if website in self.passwords:
            del self.passwords[website]

    def get_password(self, website):
        if website in self.passwords:
            password_info = self.passwords[website]
            decrypted_password = decrypt_password(password_info['password'], self.key)
            return {
                'website': website,
                'username': password_info['username'],
                'password': decrypted_password
            }
        else:
            return None
