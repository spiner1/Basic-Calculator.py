from math import*
num1 = float(input("Enter first number: "))
op1 = input("Enter an operator (+,-,*,/, or ^): ")
num2 = float(input("Enter second number: "))

try:
    if op1 == "+":
        print(num1 + num2)
    elif op1 == "-":
        print(num1 - num2)
    elif op1 == "*":
        print(num1 * num2)
    elif op1 == "/":
        print(num1 / num2)
    elif op1 == "^":
        print(pow(num1, num2))
    else:
        print("Invalid operator")
except ZeroDivisionError:
    print("Cannot divide by zero")