import re

class UserRegistration:
    def __init__(self):
        # List to store users (this would be a database in a real-world app)
        self.users_db = []

    def register_user(self, username, password, email):
        """
        Registers a new user with username, password, and email.
        Validates the inputs before registering the user.

        Args:
        username (str): The username for the new user.
        password (str): The password for the new user.
        email (str): The email for the new user.

        Returns:
        str: A message indicating the result of the registration.
        """
        # Validate user inputs
        if self._is_username_taken(username):
            return "Username already taken"
        if len(password) < 6:
            return "Password is too short"
        if not self._is_valid_email(email):
            return "Invalid email"
        # If all validations pass, register the user
        self.users_db.append({"username": username, "password": password, "email": email})
        return "Registration successful"

    def _is_username_taken(self, username):
        """
        Helper function to check if a username is already taken.

        Args:
        username (str): The username to check.

        Returns:
        bool: True if the username is already taken, otherwise False.
        """
        return any(user["username"] == username for user in self.users_db)

    def is_user_registered(self, username):
        """
        Checks if a user is registered by their username.

        Args:
        username (str): The username to check.

        Returns:
        bool: True if the user is registered, otherwise False.
        """
        return any(user["username"] == username for user in self.users_db)

    def _is_valid_email(self, email):
        """
        Helper function to check if an email is valid.

        Args:
        email (str): The email to check.

        Returns:
        bool: True if the email is valid, otherwise False.
        """
        # Simple regex to check for a valid email format (basic check)
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))
