import re

def password_complexity_checker(password):
    # Define password criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_character_criteria = bool(re.search(r'[\W_]', password))  # \W matches any non-word character
    
    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_character_criteria])
    
    # Determine password strength based on the number of criteria met
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Provide feedback to the user
    print(f"Password strength: {strength}")
    if not length_criteria:
        print("- Password should be at least 8 characters long.")
    if not uppercase_criteria:
        print("- Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        print("- Password should contain at least one lowercase letter.")
    if not number_criteria:
        print("- Password should contain at least one number.")
    if not special_character_criteria:
        print("- Password should contain at least one special character.")
    
    return strength

# Example usage
password = input("Enter your password to check its complexity: ")
password_complexity_checker(password)
