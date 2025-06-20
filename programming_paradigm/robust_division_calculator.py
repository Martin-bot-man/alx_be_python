

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        
        result = num / den
        return f"Result: {result}"

    except ZeroDivisionError as e:
        return str(e)
        
    except ValueError as e:
        return "Invalid input: " + str(e)
  

    
