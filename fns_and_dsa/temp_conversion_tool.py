CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


user_input = float(input('Enter the temperature to convert: " '))
prompt = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()
def convert_to_celsius(fahrenheit):
    
        return(fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR



def convert_to_fahrenheit(celsius):
    
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if prompt  == "F":
      converted_temp = convert_to_celsius(user_input)
      print(f"{user_input}°F is equal to {converted_temp:.2f}°C")
elif prompt == "C":
      converted_temp = convert_to_fahrenheit(user_input)
      print(f"{user_input}°C is equal to {converted_temp:.2f}°F")
else: 
      print("Invalid temperature. Please enter a numeric value")     

