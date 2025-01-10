import pytest
from registration import UserRegistration

# Test Registration Success
def test_register_user_success():
    reg = UserRegistration()
    result = reg.register_user("john_doe", "password123", "john@example.com")
    assert result == "Registration successful"

# Test Duplicate Username
def test_register_user_duplicate():
    reg = UserRegistration()
    reg.register_user("john_doe", "password123", "john@example.com")
    result = reg.register_user("john_doe", "newpassword456", "john2@example.com")
    assert result == "Username already taken"

# Test Short Password
def test_register_user_short_password():
    reg = UserRegistration()
    result = reg.register_user("john_doe", "short", "john@example.com")
    assert result == "Password is too short"

# Test Invalid Email
def test_register_user_invalid_email():
    reg = UserRegistration()
    result = reg.register_user("john_doe", "password123", "invalid-email")
    assert result == "Invalid email"

# Test User Already Registered
def test_is_user_registered():
    reg = UserRegistration()
    reg.register_user("john_doe", "password123", "john@example.com")
    result = reg.is_user_registered("john_doe")
    assert result is True

# Test User Not Registered
def test_is_user_not_registered():
    reg = UserRegistration()
    result = reg.is_user_registered("non_existent_user")
    assert result is False

# Test Username with Special Characters
def test_register_user_special_chars():
    reg = UserRegistration()
    result = reg.register_user("john_doe$123", "password123", "john@example.com")
    assert result == "Registration successful"

# Test Password with Only Numbers
def test_register_user_password_numbers():
    reg = UserRegistration()
    result = reg.register_user("john_doe", "123456", "john@example.com")
    assert result == "Registration successful"

# Test Invalid Email (No Domain)
def test_register_user_invalid_email_no_domain():
    reg = UserRegistration()
    result = reg.register_user("john_doe", "password123", "john@.com")
    assert result == "Invalid email"
