def check_password_strength(password):
    """
    This function checks the strength of a password based on the following criteria:
    - Password length is at least 8 characters.
    - Password contains at least one uppercase letter.
    - Password contains at least one lowercase letter.
    - Password contains at least one digit.
    - Password contains at least one special character.

    Returns:
    - 0 if the password is weak.
    - 1 if the password is moderate.
    - 2 if the password is strong.
    """
    if len(password) < 8:
        return 0
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    # in boolean...
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()_+-=[]{}|;':\"<>,.?\\/":
            has_special = True
            
    strength = has_uppercase + has_lowercase + has_digit + has_special
    
    if strength <= 2:
        return 1
    else:
        return 2
