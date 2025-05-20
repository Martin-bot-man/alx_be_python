number1 = 5;
number2 = 10;
operation = input("Enter an operation(+, -,*, /)  to perform: ")
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result =number1 - number2
elif operation == "*":
    result = number1* number2
elif operation == number1/number2:
    result=number1/number2
else:

    print("Invalid operation. Please enter one of the following: +, -, *, /")
    exit()
print(f"The result of {number1} {operation} {number2} is: {result}")

