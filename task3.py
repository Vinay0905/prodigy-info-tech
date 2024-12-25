import re
def check_password_strength(password):
    strength = 0
    feedback = []
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")
    if strength == 5:
        feedback.append("Password is strong.")
    elif strength == 4:
        feedback.append("Password is moderately strong.")
    else:
        feedback.append("Password is weak.")
    return feedback
password = input("Enter a password to check its strength: ")
feedback = check_password_strength(password)
for message in feedback:
    print(message)