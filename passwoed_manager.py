import json
import string
import random

class PasswordManager:
    def __init__(self, filename='passwords.json'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.passwords = json.load(file)
        except FileNotFoundError:
            self.passwords = {}

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def save_password(self, website, username, password):
        if website in self.passwords:
            print(f"Warning: Password for {website} already exists. Overwriting...")
        self.passwords[website] = {'username': username, 'password': password}
        self._save_to_file()
        

    def get_password(self, website):
        if website in self.passwords:
            return self.passwords[website]
        else:
            return None

    def _save_to_file(self):
        with open(self.filename, 'w') as file: 
            json.dump(self.passwords, file, indent=4)

if __name__ == "__main__":
    manager = PasswordManager()

    website = input("Enter website: ")
    username = input("Enter username: ")
    choice = input("Do you want to generate a password? (yes/no): ").lower()

    if choice == "yes":
        generated_password = manager.generate_password()
        print("Generated Password:", generated_password)
        manager.save_password(website, username, generated_password)
    elif choice == "no":
        password = input("Enter password: ")
        manager.save_password(website, username, password)
    else:
        print("Invalid choice.")

    # Retrieve a password~
    retrieved_password = manager.get_password(website)
    if retrieved_password:
        print("Retrieved Password:", retrieved_password['password'])
    else:
        print("Password not found.")
