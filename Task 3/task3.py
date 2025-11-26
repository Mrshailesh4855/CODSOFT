import random
import string

print("Welcome to the Password Generator")
try:
  length=int(input("Enter the password length: "))
  if length <= 0:
        print("Password length must be greater than 0")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()

char_pool =string.ascii_letters+string.digits+string.punctuation

password=''.join(random.choice(char_pool)for _ in range(length))
print(f"Generated Password: {password}")
