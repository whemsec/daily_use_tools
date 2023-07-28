import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789' + "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

def print_password():
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)

def try_again():
    while True:
        try_again = input("Would you like to try again? (Y/N): ")
        if try_again.lower() == "y":
            print_password()
        elif try_again.lower() == "n":
            print('Goodbye!')
            break
        else:
            print("You need to type 'Y' or 'N' in order to continue or stop.")
            continue

print_password()
try_again()
