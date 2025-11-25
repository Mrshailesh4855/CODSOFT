def calculator():
    print("Simple Calculator")
    print("-----------------")

    a=input("Enter the first number: ")
    b=input("Enter the second number: ")
    try:
        num1=float(a)
        num2=float(b)
    except:
        print("Please enter valid numbers.")
        return

    print("\nChoose an operation:")
    print("+  for Addition")
    print("-  for Subtraction")
    print("*  for Multiplication")
    print("/  for Division")

    operation=input("Enter your choice: ")

    if operation=="+":
        result= num1+num2
        print("Result:",result)

    elif operation=="-":
        result= num1-num2
        print("Result:",result)

    elif operation=="*":
        result= num1*num2
        print("Result:", result)

    elif operation=="/":
        if num2==0:
            print("Division by zero is not possible.")
        else:
            result=num1/num2
            print("Result:",result)
          
    else:
        print("Unknown operation. Please try again.")

if __name__ == "__main__":
    calculator()
