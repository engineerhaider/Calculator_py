# Simple Calculator Program in Python

# Define a function to perform addition
def add(num1, num2):
    return num1 + num2

# Define a function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Define a function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Define a function to perform division
def divide(num1, num2):
    return num1 / num2

# Define the main function
def main():
    print("Welcome to the simple calculator program!\n")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operator (+, -, *, /): ")
    
    # Perform the operation based on user input
    if op == '+':
        print("The result is: ", add(num1, num2))
    elif op == '-':
        print("The result is: ", subtract(num1, num2))
    elif op == '*':
        print("The result is: ", multiply(num1, num2))
    elif op == '/':
        print("The result is: ", divide(num1, num2))
    else:
        print("Invalid operator entered. Please try again.")

# Call the main function
if __name__ == "__main__":
    main()
