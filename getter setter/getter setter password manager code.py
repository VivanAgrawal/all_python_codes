
class PasswordManager:
    def __init__(self):
        self._password = ""

    def get_password(self):
        return self._password

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self._password = new_password
        else:
            print("Password should be at least 8 characters long.")

# Using the class
manager = PasswordManager()
print(manager.get_password())  # Output: ""
password=(input("Enter your password:"))
manager.set_password(password)
print(manager.get_password())  # Output: securePassword

manager.set_password("weak")  # Output: Password should be at least 8 characters long.