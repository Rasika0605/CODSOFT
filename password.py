import secrets
import string

def generate_password(length, use_digits, use_symbols):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    # Base characters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure minimum requirements
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase)
    ]

    if use_digits:
        password.append(secrets.choice(digits))
    if use_symbols:
        password.append(secrets.choice(symbols))

    # All possible characters
    all_characters = lowercase + uppercase
    if use_digits:
        all_characters += digits
    if use_symbols:
        all_characters += symbols

    # Fill remaining length
    while len(password) < length:
        password.append(secrets.choice(all_characters))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def check_strength(password):
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("======= HIGH-LEVEL PASSWORD GENERATOR =======")

    try:
        length = int(input("Enter password length (minimum 4): "))
        use_digits = input("Include numbers? (yes/no): ").lower() == "yes"
        use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

        count = int(input("How many passwords to generate?: "))

        for i in range(count):
            password = generate_password(length, use_digits, use_symbols)
            strength = check_strength(password)
            print(f"\nPassword {i+1}: {password}")
            print("Strength:", strength)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()