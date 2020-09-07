from decimal import *

first_number = input("Enter the first number: ")
operator = input("Enter the operator you want to use: ")
second_number = input("Enter the second number: ")

if operator == "+":
    print(Decimal(first_number) + Decimal(second_number))
elif operator == "-":
    print(Decimal(first_number) - Decimal(second_number))
elif operator == "/":
    print(Decimal(first_number) / Decimal(second_number))
elif operator == "*":
    print(Decimal(first_number) * Decimal(second_number))
else:
    print("Invalid operator")

