num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2  
    case "*"  :
        result = num1 * num2
    case "/":
         if num2 != 0:
             result = num1/ num2
         else:
            result = "Error: Division by zero is not allowed."

result = result if isinstance(result, str) else f"The result is: {result}"
print(result)
            
    
