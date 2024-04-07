import re

def check_password_complexity(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return "Weak: Password should contain at least one uppercase letter."
    
    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return "Weak: Password should contain at least one lowercase letter."
    
    # Check for digits
    if not re.search("[0-9]", password):
        return "Weak: Password should contain at least one digit."
    
    # Check for special characters
    if not re.search("[!@#$%^&*()_+=-]", password):
        return "Weak: Password should contain at least one special character."
    
    return "Strong: Password meets complexity requirements."

def main():
    password = input("Enter your password: ")
    feedback = check_password_complexity(password)
    print(feedback)

if __name__ == "__main__":
    main()
