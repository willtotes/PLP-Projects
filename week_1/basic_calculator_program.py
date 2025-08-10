
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter math operation (+, -, *, /): ")

if operation == "+":
    print(f"The addition of {num1} and {num2} is {num1 + num2}")
elif operation == "-":
    print(f"The subtraction of {num1} and {num2} is {num1 - num2}")
elif operation == "*":
    print(f"The multiplication of {num1} and {num2} is {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"The division of {num1} and {num2} is {num1 / num2}")
    else:
        print("Cannot be divided by a zero!")
else:
    print("The input is invalid.")

