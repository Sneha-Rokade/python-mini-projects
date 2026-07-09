def check_password_strength(password):

    min_length = 8

    upper_found = False
    lower_found = False

    if len(password) > min_length:
        strength = "Strong"
    elif len(password) == min_length:
        strength = "Good"
    else: 
        strength = "Weak"

    for ch in password:
        if ch.isupper():
            upper_found = True
        if ch.islower():
            lower_found = True
    
    if upper_found and lower_found:
        case_msg = "Contains both uppercase and lowercase letters"
    else:
        case_msg = "Should contain at least one uppercase and one lowercase letter"

    return strength, case_msg

if __name__ == "__main__":
    user_password = input("Enter password: ")

    strength, message = check_password_strength(user_password)

    print(f"Password Strength: {strength}")
    print(message)