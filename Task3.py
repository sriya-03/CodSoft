import random
import string

def generate_password(length=12, complexity="strong"):
    if complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "weak":
        characters = string.ascii_letters
        
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity (weak, medium, strong): ").lower()
    
    if complexity not in ["weak", "medium", "strong"]:
        print("Invalid complexity level. Defaulting to strong.")
        complexity = "strong"
    
    password = generate_password(length, complexity)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
