# Description: Processes string entries to validate ISBN-10 and ISBN-13 checksum strings via custom Try-Except filters.

def calculate_check_digit_10(isbn):
    total = sum((i + 1) * int(num) for i, num in enumerate(isbn[:9]))
    check_digit = total % 11
    return 'X' if check_digit == 10 else str(check_digit)

def calculate_check_digit_13(isbn):
    total = sum((3 if i % 2 else 1) * int(num) for i, num in enumerate(isbn[:12]))
    check_digit = (10 - (total % 10)) % 10
    return str(check_digit)

def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f"ISBN-{length} code should be {length} digits long.")
        return

    check_digits = isbn[:length - 1]
    last_digit = isbn[length - 1]

    try:
        [int(x) for x in check_digits]
    except ValueError:
        print("Invalid character was found.")
        return

    if length == 10:
        if last_digit not in "0123456789X":
            print("Invalid character was found.")
            return
        expected = calculate_check_digit_10(isbn)
    else:
        if last_digit not in "0123456789":
            print("Invalid character was found.")
            return
        expected = calculate_check_digit_13(isbn)

    if last_digit == expected:
        print("Valid ISBN Code.")
    else:
        print("Invalid ISBN Code.")

def main():
    user_input = input("Enter ISBN and length: ")
    try:
        isbn, length_str = user_input.split(",")
    except ValueError:
        print("Enter comma-separated values.")
        return

    try:
        length = int(length_str)
    except ValueError:
        print("Length must be a number.")
        return

    if length not in (10, 13):
        print("Length should be 10 or 13.")
        return

    validate_isbn(isbn.strip(), length)
