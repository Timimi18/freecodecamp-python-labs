# Description: Uses structural modular math components via the Luhn validation algorithm to evaluate credit card legitimacy markers.
def verify_card_number(card_number: str) -> str:
    cleaned_number = card_number.replace("-", "").replace(" ", "")
    total_sum = 0
    reverse_digits = cleaned_number[::-1]
    
    for i, digit_char in enumerate(reverse_digits):
        digit = int(digit_char)
        
        if i % 2 == 1:
            doubled_value = digit * 2
            if doubled_value > 9:
                doubled_value -= 9
            total_sum += doubled_value
        else:
            total_sum += digit
            
    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
