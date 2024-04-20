import string
import random

def generate_password(length, use_letters, use_numbers, use_punctuation):
    letters = string.ascii_letters if use_letters else ''
    numbers = string.digits if use_numbers else ''
    punctuation = string.punctuation if use_punctuation else ''
    all_characters = letters + numbers + punctuation
    if not all_characters:
        raise ValueError("At least one character type must be selected.")
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))
use_letters = input("Do you want to use letters? (y/n): ").lower() == 'y'
use_numbers = input("Do you want to use numbers? (y/n): ").lower() == 'y'
use_punctuation = input("Do you want to use punctuation? (y/n): ").lower() == 'y'

password = generate_password(length, use_letters, use_numbers, use_punctuation)
print("Generated password:", password)