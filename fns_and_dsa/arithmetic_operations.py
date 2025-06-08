

def perform_operation(num1:float, num2:float, operation:str):

    
    if operation == 'add':
        return num1 + num2 
    if operation == "subtract":
        return num1 -num2
    if operation == "multiply" :
        return num1 * num2
    if operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation." 
    
    
