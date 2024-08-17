import string

def evaluate_password_strength(password):
    score = 0
    
    # Criteria 1: Length of the password
    length = len(password)
    if length >= 8:
        score += 2
    if length >= 12:
        score += 3

    # Criteria 2: Presence of lowercase letters
    has_lower = any(c.islower() for c in password)
    if has_lower:
        score += 1

    # Criteria 3: Presence of uppercase letters
    has_upper = any(c.isupper() for c in password)
    if has_upper:
        score += 2

    # Criteria 4: Presence of digits
    has_digit = any(c.isdigit() for c in password)
    if has_digit:
        score += 2

    # Criteria 5: Presence of symbols
    has_symbol = any(c in string.punctuation for c in password)
    if has_symbol:
        score += 3

    # Criteria 6: Mix of character types
    unique_types = sum([has_lower, has_upper, has_digit, has_symbol])
    if unique_types >= 3:
        score += 2

    return score

# Example usage
password = "StrongPa$$w0rd!"
strength_score = evaluate_password_strength(password)
print(f"Password strength score: {strength_score}")
