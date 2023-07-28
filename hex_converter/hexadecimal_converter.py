hex_value = input("Enter hexadecimal here:")

try:
    decimal_value = int(hex_value, 16)  # Convert hexadecimal string to integer
    char = chr(decimal_value)  # Convert integer to corresponding character

    print("\n\nDecimal Value:", decimal_value)
    print("Char Value:", char,"\n\n")
except ValueError:
    print("Please use a valid hexadecimal value. Example: 0xAF")
