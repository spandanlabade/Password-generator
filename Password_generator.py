import string
import random

password = ""

try:

    length = int(input("How long do you want your password to be? "))

    include_symbols = input("Do you want symbols (Y/N): ")
    include_numbers = input("Do you want numbers (Y/N): ")

    symbols = "!@#$%&*?"

    all_chars = string.ascii_letters

    if include_numbers == "Y":
        all_chars += string.digits

    if include_symbols == "Y":
        all_chars += symbols

    # Guarantee required character types
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)

    if include_numbers == "Y":
        password += random.choice(string.digits)

    if include_symbols == "Y":
        password += random.choice(symbols)

    # Fill remaining characters
    while len(password) < length:
        password += random.choice(all_chars)

    # Shuffle password
    password_list = list(password)

    random.shuffle(password_list)

    password = ''.join(password_list)

    print("Generated Password:", password)

    # Password strength checker
    has_upper = False
    has_lower = False
    has_number = False
    has_symbol = False

    for char in password:

        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_number = True

        elif char in symbols:
            has_symbol = True

    # Score system
    score = 0

    if len(password) >= 8:
        score += 2

    if len(password) >= 12:
        score += 2

    if has_upper:
        score += 2

    if has_lower:
        score += 2

    if has_number:
        score += 1

    if has_symbol:
        score += 1

    if score > 10:
        score = 10

    print(f"Password Strength: {score}/10")

except:
    print("Invalid input. Please enter a valid number.")
