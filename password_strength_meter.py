import re
import string

def analyze_password_strength(password: str) -> tuple[int, list[str]]:
    """
    Analyzes the strength of a password and returns a score and feedback.
    
    Args:
        password: The password to analyze
        
    Returns:
        tuple containing:
            - score (int): Password strength score (0-100)
            - feedback (list): List of feedback messages
    """
    score = 0
    feedback = []
    
    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif len(password) >= 12:
        score += 25
        feedback.append("Good length!")
    else:
        score += 15
        feedback.append("Consider using a longer password (12+ characters).")
    
    # Check for numbers
    if re.search(r"\d", password):
        score += 15
        feedback.append("Good use of numbers!")
    else:
        feedback.append("Add numbers for stronger password.")
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 15
        feedback.append("Good use of lowercase letters!")
    else:
        feedback.append("Add lowercase letters.")
        
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 15
        feedback.append("Good use of uppercase letters!")
    else:
        feedback.append("Add uppercase letters.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
        feedback.append("Good use of special characters!")
    else:
        feedback.append("Add special characters (!@#$%^&*) for stronger password.")
    
    # Check for common patterns
    if password.lower() in ["password", "123456", "qwerty"]:
        score = 0
        feedback = ["This is a commonly used password. Please choose something more secure."]
    
    # Check for repeated characters
    if re.search(r"(.)\1{2,}", password):
        score -= 15
        feedback.append("Avoid using repeated characters.")
    
    # Ensure score stays within 0-100 range
    score = max(0, min(100, score))
    
    return score, feedback

def get_strength_label(score: int) -> str:
    """
    Converts a numerical score to a strength label.
    
    Args:
        score: Password strength score (0-100)
        
    Returns:
        str: Strength label (Weak, Moderate, or Strong)
    """
    if score < 40:
        return "Weak"
    elif score < 70:
        return "Moderate"
    else:
        return "Strong"

def main():
    """Main function to run the password strength meter."""
    print("Welcome to the Password Strength Meter!")
    print("=======================================")
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            break
            
        score, feedback = analyze_password_strength(password)
        strength = get_strength_label(score)
        
        print(f"\nPassword Strength: {strength} (Score: {score}/100)")
        print("\nFeedback:")
        for item in feedback:
            print(f"- {item}")
            
        print("\nPassword complexity meter:")
        meter_length = 20
        filled = int((score / 100) * meter_length)
        meter = f"[{'=' * filled}{'-' * (meter_length - filled)}]"
        print(meter)

if __name__ == "__main__":
    main() 