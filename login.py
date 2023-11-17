import hashlib
import getpass
import sys

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def save_password(self, site):
        password = getpass.getpass("Enter password for " + site + ": ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.passwords[site] = hashed_password
        print("Password saved successfully!")

    def verify_password(self, site):
        hashed_password = self.passwords[site]
        password = getpass.getpass("Enter password for " + site + ": ")
        if hashlib.sha256(password.encode()).hexdigest() == hashed_password:
            print("Password verified successfully!")
        else:
            print("Password verification failed.")

    def get_password(self, site):
        if site in self.passwords:
            print("The password for " + site + " is: " + self.passwords[site])
        else:
            print("No password found for " + site)

def menu():
    password_manager = PasswordManager()

    while True:
        print("\n\nPassword Manager Menu")
        print("1. Save Password")
        print("2. Verify Password")
        print("3. Get Password")
        print("4. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            site = input("Enter the site name: ")
            password_manager.save_password(site)
        elif choice == "2":
            site = input("Enter the site name: ")
            password_manager.verify_password(site)
        elif choice == "3":
            site = input("Enter the site name: ")
            password_manager.get_password(site)
        elif choice == "4":
            sys.exit("Goodbye!")
        else:
            print("Invalid choice. Please try again.")

menu()