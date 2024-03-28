def add(x, y):
    """Function to add two numbers"""
    return x + y
def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y
def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y
def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y
def power(x, y):
    """Function to calculate x raised to the power of y"""
    return x ** y
# Main program loop
while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'power' to raise a number to a power")
    print("Enter 'quit' to end the program")
    user_input = input(": ")
    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", add(num1, num2))
    elif user_input == "subtract":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", subtract(num1, num2))
    elif user_input == "multiply":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", multiply(num1, num2))
    elif user_input == "divide":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", divide(num1, num2))
    elif user_input == "power":
        num1 = float(input("Enter the base number: "))
        num2 = float(input("Enter the exponent: "))
        print("Result: ", power(num1, num2))
    else:
        print("Unknown input, please try again.")
