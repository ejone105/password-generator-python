import random
import string


def generate_password(length, use_numbers, use_symbols):
    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def check_strength(password):
    length = len(password)

    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if length >= 12 and has_number and has_symbol:
        return "Strong"
    elif length >= 8:
        return "Medium"
    else:
        return "Weak"


def main():
    print("---- PASSWORD GENERATOR ----")

    length = int(input("Enter password length: "))
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_numbers, use_symbols)

    print(f"\nGenerated Password: {password}")
    print(f"Strength: {check_strength(password)}")


if __name__ == "__main__":
    main()