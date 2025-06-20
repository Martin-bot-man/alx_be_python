

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        
        result = num / den
        return f"Result: {result}"

    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero."
        
    except ValueError as e:
        return "Error: Please enter numeric values only."
  

    
