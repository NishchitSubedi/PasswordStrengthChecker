import string

STRENGTH_MESSAGES = {
    0: "Password is too weak.",
    1: "Password is weak.",
    2: "Password is average.",
    3: "Password is fairly strong.",
    4: "Password is strong.",
}

def check_character_types(password: str) -> int:
    character_types = 0
    if any(c.isupper() for c in password):
        character_types += 1
    if any(c.islower() for c in password):
        character_types += 1
    if any(c.isdigit() for c in password):
        character_types += 1
    if any(c in string.punctuation for c in password):
        character_types += 1
    return character_types

def check_length(password: str) -> int:
    length_score = 0
    length = len(password)
    if length >= 8:
        length_score += 1
    if length >= 12:
        length_score += 1
    if length >= 16:
        length_score += 1
    if length >= 20:
        length_score += 1
    return length_score

def check_password_strength(password: str) -> int:
    score = 0
    
    character_types = check_character_types(password)
    score += character_types
    
    if character_types < 4:
        return score
    score += check_length(password)
    
    return score

def check_common_password(password: str) -> bool:
    try:
        with open("common.txt", "r") as f:
            common_passwords = set(f.read().splitlines())
        return password in common_passwords
    except FileNotFoundError:
        print("Warning: 'common.txt' not found. Skipping common password check.")
        return False

def provide_strength_feedback(score: int, password: str):
    if score >= 5:
        print("Password is extremely strong.")
    else:
        print(STRENGTH_MESSAGES[score])
        if score < 4:
            print("Make sure your password contains an uppercase letter, lowercase letter, special character, and at least one digit.")
        if len(password) < 8:
            print("Consider making your password longer (at least 8 characters).")
        elif len(password) < 12:
            print("A password with 12+ characters is considered more secure.")

def check_password(password: str) -> None:
    if check_common_password(password):
        print("Password is too common. Strength: 0.")
        return

    score = check_password_strength(password)
    provide_strength_feedback(score, password)

def main():
    while True:
        password = input("Enter password: ")
        check_password(password)

if __name__ == "__main__":
    main()
