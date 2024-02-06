import re

def test_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/~`]", password) is None
    
    errors = []
    if length_error:
        errors.append("Password should be at least 8 characters long.")
    if digit_error:
        errors.append("Password should contain at least one digit.")
    if uppercase_error:
        errors.append("Password should contain at least one uppercase letter.")
    if lowercase_error:
        errors.append("Password should contain at least one lowercase letter.")
    if special_char_error:
        errors.append("Password should contain at least one special character.")
    
    if errors:
        return False, errors
    else:
        return True, "Password is strong."

# Example usage:
password = input("Enter your password: ")
is_strong, message = test_password_strength(password)
if is_strong:
    print(message)
else:
    print("Password is weak. Errors:")
    for error in message:
        print(error)
