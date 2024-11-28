import random
import string

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/" if include_symbols else ""

    # Combine character sets
    all_characters = lowercase + uppercase + numbers + symbols
    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    # Ensure strong passwords by including at least one of each selected type
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password length
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return "".join(password)






