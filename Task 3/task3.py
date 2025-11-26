import random
import string

print("Welcome to the Password Generator")

while True:
  try:
    length=int(input("Enter the password length: "))
    if length<=0:
      print("Password length must be greater than 0 !!")
      continue
  except ValueError:
    print("Please enter a valid number !!!")
    continue
    
  print("Select complexity level:")
  print("1. Simple (letters only)")
  print("2. Medium (letters and numbers)")
  print("3. Strong (letters, numbers, symbols)")
  print("4. Exit Program ")

  choice = input("Enter Your Choice :")
  if choice =="1":
    char= string.ascii_letters
  elif choice =="2":
    char= string.ascii_letters + string.digits
  elif choice =="3":
    char= string.ascii_letters + string.digits + string.punctuation
  elif choice =="4":
    print("Program Exited....")
    break
  else:
    print("Invalid Choice")
    continue

  password=''.join(random.choice(char)for _ in range(length))
  print(f"Generated Password: {password}")
  print("---------------------------------")
