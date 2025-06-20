
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        
        result = num / den
        print (f"result: {result}")

    except ZeroDivisionError as e:
        return str(e)
    
    except TypeError as e:
        return "Invalid input: " + str(e)
    
    except ValueError as e:
        return "Invalid input: " + str(e)
safe_divide()    

    
