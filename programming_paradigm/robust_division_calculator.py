
def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        result = numerator / denominator
        print (f"result: {result}")
    except ZeroDivisionError as e:
        return str(e)
    except TypeError as e:
        return "Invalid input: " + str(e)

    
