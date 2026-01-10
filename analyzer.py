import re
import math

def analyze_password(password):
    score = 0
    feedback = []

    length = len(password)

    # Length check
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password is too short")

    #charcter
    if re.search(r"[A-Z]",password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add digits")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 2
    else:
        feedback.append("Add special characters")
        # Entropy calculation
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^A-Za-z0-9]", password):
        charset += 32

    entropy = length * math.log2(charset) if charset else 0

    # Strength label
    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    else:
        strength = "Strong"
    
    return {
        "length": length,
        "score": score,
        "entropy": round(entropy, 2),
        "strength": strength,
        "feedback": feedback
    }