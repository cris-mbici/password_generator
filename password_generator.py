import random 
import string 

# Class for generating passwords with various options
class PasswordGenerator:
  def __init__(self, length, use_uppercase, use_special_chars, pass_number):
    self.length = length  # Length of each password
    self.use_uppercase = use_uppercase  # Whether to include uppercase letters
    self.use_special_chars = use_special_chars  # Whether to include special characters
    self.pass_number = pass_number  # Number of passwords to generate

  def generate_password(self):
    characters = string.ascii_lowercase  # Start with lowercase letters
    
    if self.use_uppercase == True:
      characters += string.ascii_uppercase  # Add uppercase letters if needed
    if self.use_special_chars:
      characters += string.punctuation  # Add special characters if needed

    passwords = []  # List to store generated passwords

    for _ in range(self.pass_number):
      new_password = "".join(random.choices(characters, k=self.length))  # Generate password of given length
      passwords.append(new_password)  # Store password in the list

    # Print passwords one by one
    first, *middle, last = passwords
    print(first)
    for num in middle:
      print(num)
    print(last)

# Prompt user for password length while ensuring valid input
while True:
  password_length = int(input("How many characters should your password be?(1, 2 ,3...) >> "))
  if isinstance(password_length, int):
    break
  else:
    print("Please enter a whole number...")
    continue
    
# Ask if password should contain uppercase letters, ensuring valid input
while True:
  password_uppercase = input("Should your password contain uppercase letters?(y/n) >> ")
  password_uppercase = password_uppercase.strip().lower()
  if password_uppercase == "y":
    password_uppercase = True
    break
  elif password_uppercase == "n":
    password_uppercase = False
    break
  else:
    print("Please enter either y or n...")
    continue

# Ask if password should contain special characters, ensuring valid input
while True:
  password_special = input("Should your password contain special characters?(y/n) >> ")
  password_special = password_special.strip().lower()
  if password_special == "y":
    password_special = True
    break
  elif password_special == "n":
    password_special = False
    break
  else:
    print("Please enter either y or n...")
    continue

# Prompt user for number of passwords to generate while ensuring valid input
while True:
  password_number = int(input("How many passwords would you like to generate?(1, 2 ,3...) >> "))
  if isinstance(password_number, int):
    break
  else:
    print("Please enter a whole number...")
    continue

# Create an instance of PasswordGenerator and generate passwords
generator = PasswordGenerator(password_length, password_uppercase, password_special, password_number)
print("Here are your passwords:")
generator.generate_password()
